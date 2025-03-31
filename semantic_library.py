import os
import chromadb
import google.generativeai as genai
from chromadb.utils import embedding_functions as chroma_ef
from chromadb.api.types import Documents, EmbeddingFunction, Embeddings
from langchain_community.document_loaders import DirectoryLoader, UnstructuredMarkdownLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer # Explicit import for clarity, though Chroma uses it internally
from dotenv import load_dotenv
from typing import List, Optional, Literal

# --- Constants ---
LIBRARY_PATH = "./library"
PERSIST_DIRECTORY = "./chroma_db"
COLLECTION_NAME = "semantic_library_collection"
# Embedding Model Configuration
DEFAULT_EMBEDDING_PROVIDER: Literal['local', 'gemini'] = os.getenv('EMBEDDING_PROVIDER', 'local').lower() # Default to local
LOCAL_EMBEDDING_MODEL = "all-mpnet-base-v2"
GEMINI_EMBEDDING_MODEL = "models/embedding-001" # Or other suitable Gemini embedding model
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150
SEARCH_RESULTS_COUNT = 5

# --- Environment Variables & API Keys ---
load_dotenv() # Load variables from .env file
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# --- Embedding Functions ---

# Local Sentence Transformer (using Chroma's utility)
def get_local_embedding_function(model_name: str = LOCAL_EMBEDDING_MODEL) -> chroma_ef.SentenceTransformerEmbeddingFunction:
    print(f"Using Local Sentence Transformer: {model_name}")
    return chroma_ef.SentenceTransformerEmbeddingFunction(model_name=model_name)

# Google Gemini Embedding Function (Custom Class for ChromaDB)
class GeminiEmbeddingFunction(EmbeddingFunction):
    """Custom embedding function using Google Gemini."""
    def __init__(self, api_key: str, model_name: str = GEMINI_EMBEDDING_MODEL, task_type: str = "retrieval_document"):
        if not api_key:
            raise ValueError("Google API Key not provided. Set GOOGLE_API_KEY environment variable.")
        genai.configure(api_key=api_key)
        self._model_name = model_name
        self._task_type = task_type
        print(f"Using Google Gemini Embedding: {model_name} (Task Type: {task_type})")

    def __call__(self, input: Documents) -> Embeddings:
        try:
            # Note: Gemini API might have batch size limits, handle if necessary
            # For simplicity, embedding one by one here, but batching is preferred for large scale
            embeddings = genai.embed_content(
                model=self._model_name,
                content=input,
                task_type=self._task_type
            )
            return embeddings['embedding']
        except Exception as e:
            print(f"Error generating Gemini embeddings: {e}")
            # Return empty list or handle error appropriately
            # Returning empty list might cause issues downstream in ChromaDB add/query
            # Consider returning list of None or zero vectors of correct dimensionality if known
            # For now, re-raising might be safer to halt the process
            raise RuntimeError(f"Failed to get embeddings from Gemini: {e}") from e

def get_gemini_embedding_function(api_key: str = GOOGLE_API_KEY, model_name: str = GEMINI_EMBEDDING_MODEL) -> Optional[GeminiEmbeddingFunction]:
    if not api_key:
        print("Warning: GOOGLE_API_KEY not found in environment. Cannot use Gemini embeddings.")
        return None
    return GeminiEmbeddingFunction(api_key=api_key, model_name=model_name)

# --- Function to select Embedding Function based on provider ---
def get_embedding_function(provider: Literal['local', 'gemini'] = DEFAULT_EMBEDDING_PROVIDER) -> EmbeddingFunction:
    if provider == 'gemini':
        gemini_ef = get_gemini_embedding_function()
        if gemini_ef:
            return gemini_ef
        else:
            print("Falling back to local embedding function due to missing Gemini API key.")
            # Fallback to local if Gemini setup fails
            return get_local_embedding_function()
    elif provider == 'local':
        return get_local_embedding_function()
    else:
        print(f"Warning: Unknown embedding provider '{provider}'. Defaulting to local.")
        return get_local_embedding_function()

# --- Core Functions ---

def initialize_db(persist_directory: str = PERSIST_DIRECTORY,
                  collection_name: str = COLLECTION_NAME,
                  embedding_function: EmbeddingFunction = None) -> chromadb.Collection:
    """
    Initializes a persistent ChromaDB client and gets/creates a collection.

    Args:
        persist_directory: Path to store the database files.
        collection_name: Name of the collection to use.
        embedding_function: The embedding function instance to use. If None, determined by EMBEDDING_PROVIDER env var.

    Returns:
        The ChromaDB collection object.
    """
    # Determine embedding function if not provided
    if embedding_function is None:
        embedding_function = get_embedding_function() # Uses default provider from env or 'local'

    print(f"Initializing ChromaDB client at: {persist_directory}")
    client = chromadb.PersistentClient(path=persist_directory)

    print(f"Getting or creating collection: {collection_name}")
    collection = client.get_or_create_collection(
        name=collection_name,
        embedding_function=embedding_function,
        metadata={"hnsw:space": "cosine"} # Explicitly set cosine distance
    )
    print("Database and collection initialized.")
    return collection

def ingest_documents(collection: chromadb.Collection,
                     library_path: str = LIBRARY_PATH,
                     chunk_size: int = CHUNK_SIZE,
                     chunk_overlap: int = CHUNK_OVERLAP):
    """
    Loads, chunks, embeds, and stores documents from a directory into ChromaDB.

    Args:
        collection: The ChromaDB collection to add documents to.
        library_path: Path to the directory containing Markdown documents.
        chunk_size: Maximum size of text chunks.
        chunk_overlap: Overlap between consecutive chunks.
    """
    print(f"\nStarting ingestion from: {library_path}")
    if not os.path.exists(library_path):
        print(f"Error: Library path '{library_path}' does not exist.")
        return

    # Use UnstructuredMarkdownLoader for potentially better Markdown parsing
    loader = DirectoryLoader(
        library_path,
        glob="**/*.md",
        loader_cls=UnstructuredMarkdownLoader,
        show_progress=True,
        use_multithreading=True # Speed up loading if many files
    )
    documents = loader.load()

    if not documents:
        print("No Markdown documents found to ingest.")
        return

    print(f"Loaded {len(documents)} documents.")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split documents into {len(chunks)} chunks.")

    # Prepare data for ChromaDB batch insertion
    ids = []
    docs_to_embed = []
    metadatas = []

    print("Preparing chunks for ChromaDB...")
    for i, chunk in enumerate(chunks):
        # Create a unique ID for each chunk
        source_filename = chunk.metadata.get('source', 'unknown_source').split('/')[-1]
        chunk_id = f"{source_filename}:{i}"

        ids.append(chunk_id)
        docs_to_embed.append(chunk.page_content)
        metadatas.append({'source': source_filename}) # Store original filename

    if not ids:
        print("No chunks generated.")
        return

    # Batch add to ChromaDB (more efficient)
    # Note: ChromaDB automatically handles embedding generation using the collection's EF
    print(f"Adding {len(ids)} chunks to collection '{collection.name}'...")
    try:
        # Check if collection is empty or if we should clear it first (overwrite strategy)
        # For simplicity, we'll just add. Chroma handles duplicates based on ID.
        # If an ID exists, it might update or ignore based on implementation details.
        # To ensure overwrite, one might delete existing docs from the same source first.
        # Let's assume adding with the same ID updates the entry.
        collection.add(
            ids=ids,
            documents=docs_to_embed,
            metadatas=metadatas
        )
        print("Ingestion complete.")
    except Exception as e:
        print(f"Error during ChromaDB add operation: {e}")


def search_library(collection: chromadb.Collection,
                   query: str,
                   n_results: int = SEARCH_RESULTS_COUNT) -> list[str]:
    """
    Performs a semantic search on the ChromaDB collection.

    Args:
        collection: The ChromaDB collection to search within.
        query: The text query string.
        n_results: The number of top results to return.

    Returns:
        A list of the text content of the most relevant chunks.
    """
    print(f"\nSearching for: '{query}'")
    if not query:
        print("Search query cannot be empty.")
        return []

    results = collection.query(
        query_texts=[query],
        n_results=n_results,
        include=['documents'] # Only fetch the document content
    )

    # Extract the document texts from the results
    # Results['documents'] is a list containing one list (for the one query)
    document_list = results.get('documents', [[]])[0]

    if not document_list:
        print("No relevant documents found.")
        return []

    print(f"Found {len(document_list)} relevant chunks:")
    # for i, doc in enumerate(document_list):
    #     print(f"  {i+1}. {doc[:100]}...") # Print snippet

    return document_list

# --- Example Usage ---
if __name__ == "__main__":
    print("Semantic Library Script")
    print(f"Selected Embedding Provider: {DEFAULT_EMBEDDING_PROVIDER}")
    if DEFAULT_EMBEDDING_PROVIDER == 'gemini' and not GOOGLE_API_KEY:
        print("\n*** WARNING: EMBEDDING_PROVIDER is 'gemini' but GOOGLE_API_KEY is not set in .env! ***")
        print("*** Script will likely fail or fall back to local embeddings if possible. ***\n")

    # 1. Initialize Database (embedding function determined by env var)
    # The get_embedding_function handles selection and potential fallback
    selected_ef = get_embedding_function(DEFAULT_EMBEDDING_PROVIDER)
    db_collection = initialize_db(embedding_function=selected_ef)

    # --- Optional: Command Line Arguments for Actions ---
    # Example: python semantic_library.py --action ingest
    # Example: python semantic_library.py --action search --query "your query"
    # For simplicity, keeping the original flow for now.

    # 2. Ingest Documents (run this to populate/update the DB)
    # Consider adding a check or argument to skip ingestion if DB already exists/populated
    print("\n--- Ingestion Phase ---")
    # Check if collection exists and has items - rudimentary check
    if db_collection.count() == 0:
         print("Collection is empty. Running ingestion...")
         ingest_documents(db_collection)
    else:
         print(f"Collection '{db_collection.name}' already contains {db_collection.count()} items. Skipping ingestion.")
         print("To re-ingest, delete the './chroma_db' directory or modify this script.")

    # 3. Perform a Search
    print("\n--- Example Search ---")
    search_query = "What are the principles of clean architecture?"
    top_results = search_library(db_collection, search_query)

    if top_results:
        print(f"\nTop {len(top_results)} results for '{search_query}':")
        for i, result in enumerate(top_results):
            print(f"\n--- Result {i+1} ---")
            print(result)
    else:
        print(f"No results found for '{search_query}'.")

    print("\nScript finished.")