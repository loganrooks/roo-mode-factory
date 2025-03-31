import os
import chromadb
from chromadb.utils import embedding_functions
from langchain.document_loaders import DirectoryLoader, UnstructuredMarkdownLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer # Explicit import for clarity, though Chroma uses it internally

# --- Constants ---
LIBRARY_PATH = "./library"
PERSIST_DIRECTORY = "./chroma_db"
COLLECTION_NAME = "semantic_library_collection"
EMBEDDING_MODEL_NAME = "all-mpnet-base-v2"
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150
SEARCH_RESULTS_COUNT = 5

# --- Embedding Function ---
# Using Chroma's utility, but could also instantiate SentenceTransformer directly
# This ensures consistency between ingestion and search query embedding
sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name=EMBEDDING_MODEL_NAME
)

# --- Core Functions ---

def initialize_db(persist_directory: str = PERSIST_DIRECTORY,
                  collection_name: str = COLLECTION_NAME,
                  embedding_function = sentence_transformer_ef) -> chromadb.Collection:
    """
    Initializes a persistent ChromaDB client and gets/creates a collection.

    Args:
        persist_directory: Path to store the database files.
        collection_name: Name of the collection to use.
        embedding_function: The embedding function for the collection.

    Returns:
        The ChromaDB collection object.
    """
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

    # 1. Initialize Database
    db_collection = initialize_db()

    # 2. Ingest Documents (run this to populate/update the DB)
    # Comment out if you only want to search an existing DB
    ingest_documents(db_collection)

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