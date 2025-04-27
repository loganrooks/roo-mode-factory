#!/usr/bin/env python

import os
import sys
import json
import argparse
import logging
import time
from typing import List, Dict, Any, Optional, Tuple

# Attempt to import dependencies
try:
    import tiktoken
    from openai import OpenAI, APIError
    from dotenv import load_dotenv
except ImportError as e:
    print(f"Error: Missing dependency - {e}. Please install requirements from scripts/requirements.txt", file=sys.stderr)
    sys.exit(1)

# --- Configuration ---
load_dotenv() # Load .env file if present

# Configure logging to stderr
logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO").upper(),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    stream=sys.stderr,
)
logger = logging.getLogger("ChunkEmbedStoreScript")

# --- Script Constants & Config ---
EMBEDDING_API_KEY = os.getenv("OPENAI_API_KEY")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL_NAME", "text-embedding-3-large") # Changed default to match test
DB_MCP_SERVER_NAME = os.getenv("DB_MCP_SERVER_NAME", "db-mcp") # Name used in MCP calls

# Default values, potentially overridden by args or env vars later
DEFAULT_CHUNK_SIZE = 1000
DEFAULT_CHUNK_OVERLAP = 100
DEFAULT_EMBEDDING_BATCH_SIZE = 1000 # Default for embedding API calls

# --- Argument Parser ---
def create_arg_parser():
    """Creates and returns the argument parser."""
    parser = argparse.ArgumentParser(description="Chunk text, generate embeddings, and store in DB via DB-MCP.")
    parser.add_argument("--input", required=True, help="Path to the processed text file.")
    parser.add_argument("--doc-metadata", required=True, help="JSON string containing document metadata (e.g., source_uri, title).")
    parser.add_argument(
        "--chunk-size",
        type=int,
        default=int(os.getenv("CHUNK_SIZE", DEFAULT_CHUNK_SIZE)),
        help=f"Target chunk size in tokens (default: {DEFAULT_CHUNK_SIZE}, or CHUNK_SIZE env var)."
    )
    parser.add_argument(
        "--overlap",
        type=int,
        default=int(os.getenv("CHUNK_OVERLAP", DEFAULT_CHUNK_OVERLAP)),
        help=f"Token overlap between chunks (default: {DEFAULT_CHUNK_OVERLAP}, or CHUNK_OVERLAP env var)."
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=int(os.getenv("EMBEDDING_BATCH_SIZE", DEFAULT_EMBEDDING_BATCH_SIZE)),
        help=f"Batch size for embedding API calls (default: {DEFAULT_EMBEDDING_BATCH_SIZE}, or EMBEDDING_BATCH_SIZE env var)."
    )
    return parser

# --- Global Variables (initialized after parsing args) ---
tokenizer = None
openai_client = None
# Chunk size/overlap/batch size will be set in main() after parsing args

# --- OpenAI Client Initialization Function ---
def initialize_openai_client():
    """Initializes and returns the OpenAI client."""
    global openai_client
    if not EMBEDDING_API_KEY:
        logger.warning("OPENAI_API_KEY environment variable not set. Embedding generation will fail.")
        return None
    try:
        client = OpenAI(api_key=EMBEDDING_API_KEY)
        logger.info(f"Initialized OpenAI client for model: {EMBEDDING_MODEL}")
        return client
    except Exception as e:
        logger.error(f"Failed to initialize OpenAI client: {e}")
        return None # Allow script to continue but embedding will fail later

# --- Tokenizer Initialization Function ---
def initialize_tokenizer():
    """Initializes and returns the tiktoken tokenizer."""
    global tokenizer
    try:
        tokenizer = tiktoken.encoding_for_model(EMBEDDING_MODEL)
        logger.info(f"Initialized tokenizer for model: {EMBEDDING_MODEL}")
        return tokenizer
    except Exception as e:
        logger.error(f"Failed to initialize tokenizer for model '{EMBEDDING_MODEL}': {e}")
        sys.exit(1) # Tokenizer is essential

# --- Conceptual MCP Client for Stdio JSON-RPC ---
# This is a simplified client assuming the target MCP server (DB-MCP)
# reads JSON-RPC requests from stdin and writes responses to stdout.
class McpStdioClient:
    def __init__(self):
        self._request_id = 0

    def _send_request(self, method: str, params: Dict[str, Any]) -> Dict[str, Any]:
        self._request_id += 1
        request = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params,
            "id": self._request_id,
        }
        request_json = json.dumps(request)
        logger.debug(f"Sending MCP Request: {request_json}")
        print(request_json, flush=True) # Send to stdout

        # Read response from stdin
        response_line = sys.stdin.readline()
        if not response_line:
            raise ConnectionError("No response received from MCP server (stdin closed).")

        logger.debug(f"Received MCP Response line: {response_line.strip()}")
        try:
            response = json.loads(response_line)
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to decode JSON response from MCP server: {e}. Response line: {response_line.strip()}")

        if "error" in response:
            error_data = response["error"]
            logger.error(f"MCP Error Response: Code={error_data.get('code')}, Message={error_data.get('message')}")
            raise McpError(error_data.get('code', -1), error_data.get('message', 'Unknown MCP error'))

        if "result" not in response:
             raise ValueError(f"Invalid MCP response format (missing 'result'): {response}")

        return response["result"]

    def call_tool(self, server_name: str, tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Calls a tool on a specified MCP server."""
        params = {
            "server_name": server_name,
            "tool_name": tool_name,
            "arguments": arguments,
        }
        return self._send_request("call_tool", params)

class McpError(Exception):
    """Custom exception for MCP errors."""
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message
        super().__init__(f"MCP Error {code}: {message}")

# --- Core Logic Functions ---

def chunk_text(text: str, chunk_size: int, chunk_overlap: int) -> List[str]:
    """Chunks text using recursive character splitting based on token count."""
    if not tokenizer:
        raise RuntimeError("Tokenizer not initialized.")

    tokens = tokenizer.encode(text)
    chunks_tokens = []
    start_index = 0
    while start_index < len(tokens):
        end_index = min(start_index + chunk_size, len(tokens))
        chunks_tokens.append(tokens[start_index:end_index])

        next_start = start_index + chunk_size - chunk_overlap
        # Ensure progress and prevent infinite loops if overlap is large or chunk size is small
        if next_start <= start_index:
            next_start = start_index + 1 # Ensure progress
        start_index = next_start

        # Break if we've processed all tokens
        if start_index >= len(tokens):
            break

    # Decode token chunks back to text
    text_chunks = [tokenizer.decode(chunk_tokens) for chunk_tokens in chunks_tokens]
    logger.info(f"Chunked text into {len(text_chunks)} chunks (size: {chunk_size}, overlap: {chunk_overlap}).")
    return text_chunks

def get_embeddings(texts: List[str], batch_size: int) -> List[List[float]]:
    """Generates embeddings for a list of texts using the configured API client."""
    if not openai_client:
        raise RuntimeError("OpenAI client not initialized. Cannot generate embeddings.")

    all_embeddings = []
    # Use the provided batch_size argument
    total_batches = (len(texts) + batch_size - 1) // batch_size

    logger.info(f"Generating embeddings for {len(texts)} chunks in {total_batches} batches (size: {batch_size})...")
    for i in range(0, len(texts), batch_size):
        batch_num = (i // batch_size) + 1
        batch_texts = texts[i:i + batch_size]
        # Replace newlines as recommended by OpenAI API docs
        batch_texts = [t.replace("\n", " ") for t in batch_texts]

        try:
            logger.debug(f"Sending batch {batch_num}/{total_batches} ({len(batch_texts)} chunks) to embedding API...")
            response = openai_client.embeddings.create(input=batch_texts, model=EMBEDDING_MODEL)
            batch_embeddings = [item.embedding for item in response.data]
            all_embeddings.extend(batch_embeddings)
            logger.debug(f"Received embeddings for batch {batch_num}/{total_batches}.")
            # Optional: Add a small delay between batches if rate limits are an issue
            # time.sleep(0.5)
        except APIError as e:
            logger.error(f"OpenAI API error during embedding generation (batch {batch_num}): {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error during embedding generation (batch {batch_num}): {e}")
            raise

    logger.info(f"Successfully generated {len(all_embeddings)} embeddings.")
    return all_embeddings

def store_in_db(mcp_client: McpStdioClient, doc_metadata: Dict[str, Any], chunks: List[Dict[str, Any]], batch_size: int) -> Tuple[Optional[int], Optional[int]]:
    """Stores document metadata and chunks in the database via DB-MCP, respecting batch size."""
    doc_id = None
    total_inserted_count = 0

    # 1. Add Document Metadata
    try:
        logger.info(f"Calling DB-MCP add_document for source: {doc_metadata.get('source_uri')}")
        add_doc_result = mcp_client.call_tool(
            server_name=DB_MCP_SERVER_NAME,
            tool_name="add_document",
            arguments=doc_metadata
        )
        # Check for explicit success=False or error presence
        if not add_doc_result.get("success", True) or "error" in add_doc_result:
             error_msg = add_doc_result.get("error", "Unknown error from add_document")
             logger.error(f"DB-MCP add_document failed: {error_msg}")
             # Ensure McpError is raised for consistent handling
             raise McpError(add_doc_result.get("code", -1), f"add_document failed: {error_msg}")

        doc_id = add_doc_result.get("doc_id")
        if not doc_id:
             logger.error("DB-MCP add_document succeeded but did not return a doc_id.")
             raise ValueError("Failed to obtain document ID from DB-MCP add_document success response.")
        logger.info(f"DB-MCP add_document successful. Document ID: {doc_id}")

    except (McpError, ConnectionError, ValueError) as e:
        logger.error(f"Error calling DB-MCP add_document: {e}")
        raise # Re-raise to be caught by main handler
    except Exception as e: # Catch unexpected errors during the call
        logger.error(f"Unexpected error during DB-MCP add_document call: {e}")
        raise McpError(-1, f"Unexpected error during add_document: {e}")


    # 2. Batch Insert Chunks
    if not chunks:
        logger.warning("No chunks provided to store.")
        return doc_id, 0

    num_chunks = len(chunks)
    total_batches = (num_chunks + batch_size - 1) // batch_size
    logger.info(f"Starting batch insert of {num_chunks} chunks into doc_id {doc_id} in {total_batches} batches (size: {batch_size})...")

    for i in range(0, num_chunks, batch_size):
        batch_num = (i // batch_size) + 1
        chunk_batch = chunks[i:i + batch_size]
        logger.debug(f"Processing batch {batch_num}/{total_batches} ({len(chunk_batch)} chunks) for doc_id {doc_id}")

        try:
            insert_chunks_result = mcp_client.call_tool(
                server_name=DB_MCP_SERVER_NAME,
                tool_name="batch_insert_chunks",
                arguments={"document_id": doc_id, "chunks": chunk_batch}
            )
            # Check for explicit success=False or error presence
            if not insert_chunks_result.get("success", True) or "error" in insert_chunks_result:
                error_msg = insert_chunks_result.get("error", "Unknown error from batch_insert_chunks")
                logger.error(f"DB-MCP batch_insert_chunks failed for batch {batch_num}: {error_msg}")
                # Raise McpError to ensure consistent failure handling and exit code 1
                raise McpError(insert_chunks_result.get("code", -1), f"batch_insert_chunks failed for batch {batch_num}: {error_msg}")

            batch_inserted_count = insert_chunks_result.get("inserted_count", len(chunk_batch))
            total_inserted_count += batch_inserted_count
            logger.debug(f"DB-MCP batch_insert_chunks successful for batch {batch_num}. Inserted: {batch_inserted_count} chunks.")
            # Optional delay if rate limiting is a concern
            # time.sleep(0.1)

        except (McpError, ConnectionError, ValueError) as e:
            logger.error(f"Error calling DB-MCP batch_insert_chunks for batch {batch_num}: {e}")
            raise # Re-raise to be caught by main handler
        except Exception as e: # Catch unexpected errors during the call
             logger.error(f"Unexpected error during DB-MCP batch_insert_chunks call for batch {batch_num}: {e}")
             raise McpError(-1, f"Unexpected error during batch_insert_chunks: {e}")


    logger.info(f"Finished batch insert. Total chunks attempted: {total_inserted_count} for doc_id {doc_id}.")
    return doc_id, total_inserted_count

# --- Main Execution ---
def main():
    global openai_client, tokenizer # Allow main to set global clients/config

    parser = create_arg_parser()
    args = parser.parse_args()

    # --- 0. Initialize Globals based on Args/Env ---
    openai_client = initialize_openai_client() # Initialize based on env key
    tokenizer = initialize_tokenizer() # Initialize based on env model name

    # Validate chunking parameters
    if args.overlap >= args.chunk_size:
        logger.error(f"Invalid configuration: Overlap ({args.overlap}) must be less than chunk size ({args.chunk_size}).")
        sys.exit(1)

    logger.info(f"Starting processing for input file: {args.input}")
    logger.info(f"Chunk Size: {args.chunk_size}, Overlap: {args.overlap}, Embedding Batch Size: {args.batch_size}")

    # --- 1. Parse Metadata ---
    try:
        doc_metadata = json.loads(args.doc_metadata)
        if not isinstance(doc_metadata, dict) or "source_uri" not in doc_metadata:
             raise ValueError("Invalid --doc-metadata format. Must be a JSON object with at least a 'source_uri' key.")
        logger.debug(f"Parsed document metadata: {doc_metadata}")
    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse --doc-metadata JSON string: {e}")
        sys.exit(1)
    except ValueError as e:
        logger.error(str(e))
        sys.exit(1)

    # --- 2. Read Input File ---
    try:
        with open(args.input, 'r', encoding='utf-8') as f:
            text_content = f.read()
        logger.info(f"Successfully read input file: {args.input} ({len(text_content)} chars)")
    except FileNotFoundError:
        logger.error(f"Input file not found: {args.input}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Error reading input file {args.input}: {e}")
        sys.exit(1)

    if not text_content:
        logger.warning("Input file is empty. Nothing to process.")
        # Consider exiting successfully or with a specific code? Exit 0 for now.
        print(json.dumps({"success": True, "doc_id": None, "inserted_count": 0, "message": "Input file empty."}))
        sys.exit(0)

    # --- 3. Chunk Text ---
    try:
        # Pass chunk_size and overlap from args
        text_chunks = chunk_text(text_content, args.chunk_size, args.overlap)
    except Exception as e:
        logger.error(f"Error during text chunking: {e}")
        sys.exit(1)

    if not text_chunks:
        logger.warning("Chunking resulted in zero chunks.")
        print(json.dumps({"success": True, "doc_id": None, "inserted_count": 0, "message": "No chunks generated."}))
        sys.exit(0)

    # --- 4. Generate Embeddings ---
    try:
        # Pass batch_size from args
        embeddings = get_embeddings(text_chunks, args.batch_size)
    except (RuntimeError, APIError, Exception) as e:
        logger.error(f"Error during embedding generation: {e}")
        sys.exit(1) # Exit if embeddings fail

    if len(embeddings) != len(text_chunks):
        logger.error(f"Mismatch between number of chunks ({len(text_chunks)}) and generated embeddings ({len(embeddings)}).")
        sys.exit(1)

    # --- 5. Prepare Chunk Data for DB ---
    chunks_for_db = [
        {
            "chunk_text": text,
            "chunk_index": i,
            "embedding": embedding,
        }
        for i, (text, embedding) in enumerate(zip(text_chunks, embeddings))
    ]

    # --- 6. Store in Database via MCP ---
    final_doc_id = None
    final_inserted_count = 0
    try:
        mcp_client = McpStdioClient()
        # Pass args.batch_size to store_in_db
        final_doc_id, final_inserted_count = store_in_db(mcp_client, doc_metadata, chunks_for_db, args.batch_size)
        logger.info("Successfully stored document metadata and chunks in DB.")
        # Output success details to stdout for the calling process (Librarian mode)
        print(json.dumps({
            "success": True,
            "doc_id": final_doc_id,
            "chunks_processed": final_inserted_count # Use the accumulated count
        }))
        sys.exit(0) # Success
    # Ensure all relevant exceptions lead to exit code 1 and error JSON output
    except (McpError, ConnectionError, ValueError, RuntimeError, APIError, Exception) as e:
        error_type = type(e).__name__
        error_message = str(e)
        logger.error(f"Script failed due to {error_type}: {error_message}")
        # Output failure details to stdout
        print(json.dumps({
            "success": False,
            "doc_id": final_doc_id, # May be None or have a value depending on when error occurred
            "chunks_processed": total_inserted_count if 'total_inserted_count' in locals() else 0, # Report count up to failure point if available
            "error": f"{error_type}: {error_message}"
        }))
        sys.exit(1) # Ensure non-zero exit code on ANY exception during processing

if __name__ == "__main__":
    main()