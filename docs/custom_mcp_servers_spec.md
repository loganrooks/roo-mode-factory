# Specification: Custom MCP Servers for Philosophical Research Assistant

**Version:** 1.0
**Date:** 2025-04-16

## 1. Introduction

This document provides detailed specifications and pseudocode for the Python implementation of three custom MCP (Model Context Protocol) servers required for the Philosophical Research Assistant RooCode system:

1.  **`DB-MCP`**: Manages interactions with the PostgreSQL/pgvector database storing RAG documents and embeddings.
2.  **`PhilAPI-MCP`**: Provides access to external philosophy-specific APIs like PhilPapers, Open Library, and DOAB.
3.  **`ChunkerEmbedder-MCP`**: Handles the text chunking and embedding generation steps of the RAG ingestion pipeline (as an optional alternative to a shell script).

These specifications are based on the architecture defined in `docs/philosophy_assistant_architecture.md` and related documents (`docs/roomodes/roocode-rag-research-assistant.md`, `docs/roomodes/programmatic_access_to_philosophy_databases.md`), general MCP guidelines (`docs/roomodes/guide-for-building-mcp-server.md`), and analysis of the existing `DB-MCP` implementation (`mcp-servers/db-mcp/main.py`).

## 2. Common Considerations

*   **Technology Stack:** All servers are intended to be implemented in Python 3.x.
*   **MCP SDK:** Servers will utilize the `@modelcontextprotocol/sdk` (Python version, assumed available as `modelcontextprotocol-sdk` via pip) for handling MCP communication, server setup, and tool registration.
*   **Transport:** All servers will use `StdioServerTransport` for communication with RooCode.
*   **Configuration & Security:**
    *   Credentials (DB passwords, API keys) MUST be read from environment variables passed via RooCode's MCP configuration (`env` property). No hardcoding.
    *   Servers should log informational messages and errors to `stderr` for visibility in RooCode.
    *   Error handling should utilize `McpError` with appropriate `ErrorCode` values (e.g., `InvalidParams`, `InternalError`, `MethodNotFound`) for clear communication back to the agent.
*   **Dependencies:** Each server will have its own `requirements.txt`.

## 3. DB-MCP Server Specification

*   **Purpose:** Acts as the sole, secure interface between RooCode modes (primarily `Researcher` and `Librarian`/`ChunkerEmbedder-MCP`) and the PostgreSQL database containing the RAG knowledge base (documents, chunks, embeddings). Encapsulates all database logic and connection details.
*   **Based On:** `mcp-servers/db-mcp/main.py`, `docs/philosophy_assistant_architecture.md`, `docs/roomodes/roocode-rag-research-assistant.md`.
*   **Dependencies:** `modelcontextprotocol-sdk`, `psycopg2-binary`, `pgvector`, `python-dotenv`.

### 3.1. Setup and Initialization

*   **Environment Variables:** Reads the following from `env` (set in RooCode MCP config):
    *   `PGHOST` (default: `localhost`)
    *   `PGPORT` (default: `5432`)
    *   `PGDATABASE` (default: `philosophy_rag`)
    *   `PGUSER` (default: `rag_agent_user`)
    *   `PGPASSWORD` (**Required**)
    *   `LOG_LEVEL` (optional, default: `INFO`)
*   **Connection:**
    *   Establishes a connection to PostgreSQL using `psycopg2.connect()` on initialization.
    *   Registers the `pgvector` type handler using `pgvector.psycopg2.register_vector()`.
    *   Sets `autocommit = False` to manage transactions explicitly.
    *   Implements reconnection logic if the connection is lost.
    *   Raises `McpError` if the initial connection fails (especially if `PGPASSWORD` is missing).
*   **Transaction Management:** Uses a private helper method (`_get_cursor`) acting as a context manager to provide cursors (`psycopg2.extras.DictCursor`) and handle `commit()` or `rollback()` automatically.

```pseudocode
# --- DB-MCP: Initialization ---
IMPORT os, sys, logging, json, psycopg2, psycopg2.extras, pgvector.psycopg2
IMPORT date from datetime
IMPORT load_dotenv from dotenv
IMPORT McpServer, StdioServerTransport, McpToolHandler, McpError, McpToolContext, ErrorCode from modelcontextprotocol.server

# Load .env (optional for local dev)
load_dotenv()

# Setup logging to stderr
logger = configure_logging(level=os.getenv("LOG_LEVEL", "INFO"))

# Read DB config from environment variables
DB_HOST = os.getenv("PGHOST", "localhost")
DB_PORT = os.getenv("PGPORT", "5432")
DB_NAME = os.getenv("PGDATABASE", "philosophy_rag")
DB_USER = os.getenv("PGUSER", "rag_agent_user")
DB_PASSWORD = os.getenv("PGPASSWORD")

IF NOT DB_PASSWORD:
    logger.error("FATAL: PGPASSWORD environment variable is not set.")
    sys.exit("DB Password not configured")

CLASS DbMcpServer inherits McpServer:
    FUNCTION __init__(self):
        super().__init__(name="db-mcp", title="Database MCP Server", description="Provides tools to interact with the RAG vector database.", capabilities={"tools": {}})
        self.db_conn = None
        TRY
            self._connect_db()
        CATCH McpError as e:
            logger.critical(f"Failed to initialize DB connection: {e.message}")
            RAISE e # Propagate to prevent server start

    FUNCTION _connect_db(self):
        TRY
            logger.info(f"Connecting to DB {DB_NAME} at {DB_HOST}:{DB_PORT}...")
            self.db_conn = psycopg2.connect(
                dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
            )
            pgvector.psycopg2.register_vector(self.db_conn)
            self.db_conn.autocommit = False
            logger.info("DB connection successful.")
        CATCH psycopg2.Error as e:
            logger.error(f"DB connection failed: {e}")
            RAISE McpError(ErrorCode.InternalError, f"Database connection failed: {e}") from e

    # Context manager for cursor and transaction handling
    @contextlib.contextmanager # Use contextlib for easier context manager creation
    FUNCTION _get_cursor(self, commit=False):
        IF self.db_conn IS None OR self.db_conn.closed != 0:
            logger.warning("DB connection lost. Reconnecting...")
            self._connect_db() # Raises McpError on failure

        cursor = self.db_conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        TRY
            YIELD cursor
            IF commit:
                self.db_conn.commit()
                logger.debug("Transaction committed.")
        CATCH psycopg2.Error as db_err:
            logger.error(f"DB operation failed: {db_err}")
            self.db_conn.rollback()
            RAISE McpError(ErrorCode.InternalError, f"Database error: {db_err}") from db_err
        CATCH Exception as e:
            logger.error(f"Unexpected error during DB operation: {e}")
            self.db_conn.rollback()
            RAISE McpError(ErrorCode.InternalError, f"Unexpected server error: {e}") from e
        FINALLY
            cursor.close()

    # ... Tool handlers defined below ...

    ASYNC FUNCTION start(self):
        IF self.db_conn IS None OR self.db_conn.closed != 0:
             logger.error("Cannot start server, DB connection failed on init.")
             RETURN
        transport = StdioServerTransport()
        transport.on_close = self.shutdown # Graceful shutdown
        logger.info('DB MCP Server starting to listen on stdio...')
        AWAIT self.listen(transport)
        logger.info('DB MCP Server listening.')

    ASYNC FUNCTION shutdown(self):
        logger.info("Shutting down DB MCP server...")
        IF self.db_conn AND self.db_conn.closed == 0:
            self.db_conn.close()
            logger.info("Database connection closed.")
        AWAIT super().close()
        logger.info("DB MCP Server shut down complete.")

# --- Entry Point ---
IF __name__ == "__main__":
    TRY
        server_instance = DbMcpServer()
        import asyncio
        asyncio.run(server_instance.start())
    CATCH McpError as e:
        logger.critical(f"Failed to initialize DbMcpServer: {e.message}")
        sys.exit(f"Server Initialization Failed: {e.message}")
    CATCH Exception as e:
        logger.critical(f"Unexpected error during server startup: {e}", exc_info=True)
        sys.exit(f"Unexpected Startup Error: {e}")
```

### 3.2. Tool: `add_document`

*   **Purpose:** Adds or updates metadata for a document in the `documents` table. Uses `ON CONFLICT (source_uri)` to handle updates gracefully if a document with the same source URI is re-processed.
*   **Input Parameters:** `source_uri` (string, required), `title` (string|null), `authors` (string|null), `publication_date` (string|null, YYYY-MM-DD format), `metadata_jsonb` (object|null), `extracted_text_hash` (string|null).
*   **Core Logic:**
    *   Validates `publication_date` format if provided.
    *   Constructs an `INSERT ... ON CONFLICT ... DO UPDATE ... RETURNING doc_id` SQL query.
    *   Converts `metadata_jsonb` object to a JSON string using `json.dumps()` for insertion.
    *   Executes the query within a transaction using the `_get_cursor` context manager (with `commit=True`).
    *   Retrieves the `doc_id` from the `RETURNING` clause.
*   **External Interactions:** Executes SQL INSERT/UPDATE on `documents` table.
*   **Success Output:** `{"success": True, "doc_id": <integer>}`
*   **Error Handling:**
    *   Catches `ValueError` for invalid date format, returns `McpError(InvalidParams)`.
    *   Catches `psycopg2.Error` during DB execution (via `_get_cursor`), rolls back transaction, returns `McpError(InternalError)`.
    *   Handles cases where `RETURNING doc_id` might fail (though unlikely).

```pseudocode
# --- DB-MCP: add_document Handler ---
@McpToolHandler(
    name="add_document",
    description="Adds/updates document metadata.",
    input_schema={...}, # As defined in main.py
    output_schema={...} # As defined in main.py
)
ASYNC FUNCTION add_document(self, context: McpToolContext, params: Dict) -> Dict:
    source_uri = params.get("source_uri")
    title = params.get("title")
    authors = params.get("authors")
    pub_date_str = params.get("publication_date")
    metadata = params.get("metadata_jsonb")
    text_hash = params.get("extracted_text_hash")

    # TDD: Test date validation (valid, invalid, null)
    pub_date = None
    IF pub_date_str:
        TRY
            pub_date = date.fromisoformat(pub_date_str)
        CATCH ValueError:
            RAISE McpError(ErrorCode.InvalidParams, f"Invalid date format: '{pub_date_str}'. Use YYYY-MM-DD.")

    sql = """
        INSERT INTO documents (source_uri, title, authors, publication_date, metadata_jsonb, extracted_text_hash)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON CONFLICT (source_uri) DO UPDATE SET
            title = EXCLUDED.title, authors = EXCLUDED.authors, publication_date = EXCLUDED.publication_date,
            metadata_jsonb = EXCLUDED.metadata_jsonb, extracted_text_hash = EXCLUDED.extracted_text_hash,
            last_processed_at = NOW()
        RETURNING doc_id;
    """
    query_params = (
        source_uri, title, authors, pub_date,
        json.dumps(metadata) IF metadata ELSE None,
        text_hash
    )

    TRY
        # TDD: Test successful insertion
        # TDD: Test successful update (ON CONFLICT)
        # TDD: Test DB connection error during insert/update
        WITH self._get_cursor(commit=True) as cur:
            cur.execute(sql, query_params)
            result = cur.fetchone()
            doc_id = result["doc_id"] IF result ELSE None

            IF doc_id:
                logger.info(f"Added/Updated document '{source_uri}', doc_id: {doc_id}")
                RETURN {"success": True, "doc_id": doc_id}
            ELSE:
                logger.error(f"Failed to get doc_id after inserting/updating '{source_uri}'")
                RETURN {"success": False, "error": "Failed to retrieve doc_id after insert/update."}
    CATCH McpError as e: # Handles DB errors from _get_cursor or validation errors
        # TDD: Test handling of McpError (e.g., InvalidParams from date validation)
        RETURN {"success": False, "error": e.message}

```
#### TDD Anchors: `add_document`
*   Test successful insertion of a new document.
*   Test successful update of an existing document (triggering `ON CONFLICT`).
*   Test insertion/update with null values for optional fields (title, authors, date, metadata, hash).
*   Test handling of invalid `publication_date` format (expect `InvalidParams` error).
*   Test handling of database connection errors during the operation (expect `InternalError`).
*   Test handling of other `psycopg2.Error` exceptions during execution (expect `InternalError`).
*   Test insertion with complex nested `metadata_jsonb`.

### 3.3. Tool: `batch_insert_chunks`

*   **Purpose:** Efficiently inserts multiple chunks (text and embeddings) for a single document into the `chunks` table. Uses `ON CONFLICT (document_id, chunk_index)` to allow re-running ingestion or updating chunks.
*   **Input Parameters:** `document_id` (integer, required), `chunks` (array of objects, required, minItems: 1). Each chunk object contains `chunk_text` (string, required), `chunk_index` (integer, required), `embedding` (array of numbers, required).
*   **Core Logic:**
    *   Prepares a list of tuples `(document_id, chunk_index, chunk_text, embedding)` from the input `chunks` array.
    *   Constructs an `INSERT ... ON CONFLICT ... DO UPDATE` SQL query using `%s` placeholder for `psycopg2.extras.execute_values`.
    *   Executes the batch insertion using `psycopg2.extras.execute_values` within a transaction (`_get_cursor` with `commit=True`).
*   **External Interactions:** Executes SQL batch INSERT/UPDATE on `chunks` table.
*   **Success Output:** `{"success": True, "inserted_count": <integer>}` (Reports the number of chunks *attempted*, as `rowcount` is unreliable with `ON CONFLICT`).
*   **Error Handling:**
    *   Catches `psycopg2.Error` during DB execution (via `_get_cursor`), rolls back transaction, returns `McpError(InternalError)`.
    *   Handles potential errors during data preparation (though less likely with schema validation).

```pseudocode
# --- DB-MCP: batch_insert_chunks Handler ---
@McpToolHandler(
    name="batch_insert_chunks",
    description="Inserts multiple chunks efficiently.",
    input_schema={...}, # As defined in main.py
    output_schema={...} # As defined in main.py
)
ASYNC FUNCTION batch_insert_chunks(self, context: McpToolContext, params: Dict) -> Dict:
    document_id = params.get("document_id")
    chunks_data = params.get("chunks", [])

    # TDD: Test with empty chunks_data list (schema should prevent, but test defensively)
    IF NOT chunks_data:
         RAISE McpError(ErrorCode.InvalidParams, "Input 'chunks' array cannot be empty.")

    # Prepare list of tuples for execute_values
    values_list = []
    FOR chunk IN chunks_data:
        # TDD: Test handling of missing required fields in a chunk object (schema should prevent)
        # TDD: Test handling of non-numeric values in embedding list (schema should prevent)
        values_list.append((
            document_id,
            chunk["chunk_index"],
            chunk["chunk_text"],
            chunk["embedding"] # Pass as list/tuple
        ))

    sql = """
        INSERT INTO chunks (document_id, chunk_index, chunk_text, embedding)
        VALUES %s
        ON CONFLICT (document_id, chunk_index) DO UPDATE SET
            chunk_text = EXCLUDED.chunk_text,
            embedding = EXCLUDED.embedding;
    """

    TRY
        # TDD: Test successful batch insertion
        # TDD: Test successful batch update (ON CONFLICT)
        # TDD: Test insertion with large number of chunks (performance, memory)
        # TDD: Test DB connection error during batch insert
        WITH self._get_cursor(commit=True) as cur:
            # Use execute_values for efficiency
            psycopg2.extras.execute_values(cur, sql, values_list, page_size=100) # page_size can be tuned
            # rowcount is unreliable with ON CONFLICT, report attempted count
            inserted_count = len(values_list)
            logger.info(f"Attempted batch insert/update for {inserted_count} chunks for doc_id: {document_id}.")
            RETURN {"success": True, "inserted_count": inserted_count}
    CATCH McpError as e: # Handles DB errors from _get_cursor
        # TDD: Test handling of McpError (e.g., constraint violation if unique_chunk_order fails)
        RETURN {"success": False, "error": e.message, "inserted_count": 0}

```
#### TDD Anchors: `batch_insert_chunks`
*   Test successful insertion of multiple chunks for a valid `document_id`.
*   Test successful update of existing chunks (triggering `ON CONFLICT`).
*   Test insertion with a large batch of chunks (e.g., > 1000) to check performance and `page_size` behavior.
*   Test handling of invalid `document_id` (foreign key constraint violation, expect `InternalError`).
*   Test handling of duplicate `chunk_index` for the same `document_id` within a *single* batch (if DB constraint allows, `ON CONFLICT` should handle; if constraint prevents, expect `InternalError`).
*   Test handling of database connection errors during the batch operation (expect `InternalError`).
*   Test handling of embedding vectors with incorrect dimensions (if DB enforces, expect `InternalError`).

### 3.4. Tool: `query_similar_chunks`

*   **Purpose:** Finds the `top_k` chunks most similar to a given `query_embedding` using cosine distance (`<=>` operator), optionally filtering by document metadata.
*   **Input Parameters:** `query_embedding` (array of numbers, required), `top_k` (integer, default: 5), `filters` (object|null, optional key-value pairs for filtering `documents` table).
*   **Core Logic:**
    *   Constructs a base SQL query joining `chunks` and `documents` tables.
    *   Calculates distance using `embedding <=> %s`.
    *   Dynamically adds `WHERE` clauses based on the `filters` parameter:
        *   Handles specific keys like `publication_date_after`/`_before` by comparing `d.publication_date`.
        *   Handles generic keys by querying the `d.metadata_jsonb` field using the JSONB containment operator `@>`. Requires wrapping filter values in `json.dumps()`.
    *   Appends `ORDER BY score ASC LIMIT %s`.
    *   Executes the query using `_get_cursor` (no commit needed).
    *   Formats results, combining document metadata (including fields from `metadata_jsonb`) into a nested `metadata` object for each chunk.
*   **External Interactions:** Executes SQL SELECT query on `chunks` and `documents` tables, utilizing `pgvector` index for similarity search.
*   **Success Output:** `{"success": True, "results": [ { "chunk_id": ..., "document_id": ..., "chunk_text": ..., "score": ..., "metadata": { ... } }, ... ]}`
*   **Error Handling:**
    *   Catches `ValueError` for invalid date formats in filters, returns `McpError(InvalidParams)`.
    *   Catches `psycopg2.Error` during DB execution (via `_get_cursor`), returns `McpError(InternalError)`.
    *   Handles cases where no results are found (returns empty `results` array).

```pseudocode
# --- DB-MCP: query_similar_chunks Handler ---
@McpToolHandler(
    name="query_similar_chunks",
    description="Finds similar chunks via vector search.",
    input_schema={...}, # As defined in main.py
    output_schema={...} # As defined in main.py
)
ASYNC FUNCTION query_similar_chunks(self, context: McpToolContext, params: Dict) -> Dict:
    query_embedding = params.get("query_embedding")
    top_k = params.get("top_k", 5)
    filters = params.get("filters")

    # TDD: Test with invalid query_embedding format (e.g., wrong dimension, non-numeric) - DB might raise error
    IF NOT isinstance(query_embedding, list) OR NOT all(isinstance(n, (int, float)) for n in query_embedding):
         RAISE McpError(ErrorCode.InvalidParams, "Invalid query_embedding format. Expected array of numbers.")

    base_sql = """
        SELECT c.chunk_id, c.document_id, c.chunk_text, c.embedding <=> %s AS score,
               d.source_uri, d.title, d.authors, d.publication_date, d.metadata_jsonb
        FROM chunks c JOIN documents d ON c.document_id = d.doc_id
    """
    where_clauses = []
    query_params = [query_embedding] # Embedding is the first parameter for <=>

    # TDD: Test various filter combinations (single, multiple, date, jsonb)
    IF filters:
        FOR key, value IN filters.items():
            IF key == "publication_date_after":
                TRY: date_val = date.fromisoformat(str(value))
                CATCH ValueError: RAISE McpError(ErrorCode.InvalidParams, f"Invalid date format for filter '{key}': '{value}'. Use YYYY-MM-DD.")
                where_clauses.append("d.publication_date > %s")
                query_params.append(date_val)
            ELSE IF key == "publication_date_before":
                TRY: date_val = date.fromisoformat(str(value))
                CATCH ValueError: RAISE McpError(ErrorCode.InvalidParams, f"Invalid date format for filter '{key}': '{value}'. Use YYYY-MM-DD.")
                where_clauses.append("d.publication_date < %s")
                query_params.append(date_val)
            # TDD: Add tests for other specific filter keys if implemented (e.g., author ILIKE)
            ELSE: # Default: filter metadata_jsonb using @>
                # TDD: Test filtering on nested JSONB fields
                where_clauses.append("d.metadata_jsonb @> %s")
                query_params.append(json.dumps({key: value})) # Wrap filter in JSON string

    sql = base_sql
    IF where_clauses:
        sql += " WHERE " + " AND ".join(where_clauses)

    sql += " ORDER BY score ASC LIMIT %s;" # Cosine distance: smaller is better
    query_params.append(top_k)

    TRY
        # TDD: Test successful query with results
        # TDD: Test successful query with no results
        # TDD: Test DB connection error during query
        WITH self._get_cursor() as cur:
            logger.debug(f"Executing similarity query: {cur.mogrify(sql, query_params)}")
            cur.execute(sql, query_params)
            rows = cur.fetchall()

            results = []
            FOR row IN rows:
                doc_metadata = {
                    "source_uri": row["source_uri"], "title": row["title"], "authors": row["authors"],
                    "publication_date": str(row["publication_date"]) IF row["publication_date"] ELSE None,
                    **(row["metadata_jsonb"] IF row["metadata_jsonb"] ELSE {}) # Merge JSONB fields
                }
                results.append({
                    "chunk_id": row["chunk_id"], "document_id": row["document_id"],
                    "chunk_text": row["chunk_text"], "score": row["score"],
                    "metadata": doc_metadata,
                })

            logger.info(f"Found {len(results)} similar chunks.")
            RETURN {"success": True, "results": results}
    CATCH McpError as e: # Handles DB errors from _get_cursor or validation
        # TDD: Test handling of McpError (e.g., InvalidParams from date filter)
        RETURN {"success": False, "error": e.message}

```
#### TDD Anchors: `query_similar_chunks`
*   Test successful query returning `top_k` results.
*   Test query returning fewer than `top_k` results.
*   Test query returning zero results.
*   Test query with various metadata filters:
    *   Single JSONB field filter.
    *   Multiple JSONB field filters.
    *   `publication_date_after` filter.
    *   `publication_date_before` filter.
    *   Combination of date and JSONB filters.
*   Test handling of invalid date format in filters (expect `InvalidParams` error).
*   Test handling of invalid `query_embedding` format/dimension (expect `InternalError` from DB).
*   Test handling of database connection errors during the query (expect `InternalError`).
*   Verify the structure of the returned `metadata` object, including fields from `metadata_jsonb`.
*   Verify results are ordered by `score` ascending.

### 3.5. Tool: `get_document_metadata`

*   **Purpose:** Retrieves all metadata fields for a specific document given its `doc_id`.
*   **Input Parameters:** `doc_id` (integer, required).
*   **Core Logic:**
    *   Constructs a `SELECT * FROM documents WHERE doc_id = %s` SQL query.
    *   Executes the query using `_get_cursor` (no commit needed).
    *   If a row is found, formats the result, combining base fields and the `metadata_jsonb` content into a single `metadata` object.
    *   If no row is found, returns success: False with an error message.
*   **External Interactions:** Executes SQL SELECT query on `documents` table.
*   **Success Output:** `{"success": True, "metadata": { ... }}` or `{"success": False, "metadata": null, "error": "Document not found."}`
*   **Error Handling:**
    *   Catches `psycopg2.Error` during DB execution (via `_get_cursor`), returns `McpError(InternalError)`.
    *   Handles the case where `doc_id` does not exist.

```pseudocode
# --- DB-MCP: get_document_metadata Handler ---
@McpToolHandler(
    name="get_document_metadata",
    description="Retrieves metadata for a specific document.",
    input_schema={...}, # As defined in main.py
    output_schema={...} # As defined in main.py
)
ASYNC FUNCTION get_document_metadata(self, context: McpToolContext, params: Dict) -> Dict:
    doc_id = params.get("doc_id")

    # TDD: Test with invalid doc_id type (e.g., string) - schema should prevent
    IF NOT isinstance(doc_id, int):
         RAISE McpError(ErrorCode.InvalidParams, "Invalid doc_id format. Expected integer.")

    sql = """
        SELECT doc_id, source_uri, title, authors, publication_date, metadata_jsonb, last_processed_at
        FROM documents WHERE doc_id = %s;
    """
    TRY
        # TDD: Test successful retrieval for existing doc_id
        # TDD: Test retrieval for non-existent doc_id
        # TDD: Test DB connection error during retrieval
        WITH self._get_cursor() as cur:
            cur.execute(sql, (doc_id,))
            row = cur.fetchone()

            IF row:
                metadata = {
                    "doc_id": row["doc_id"], "source_uri": row["source_uri"], "title": row["title"],
                    "authors": row["authors"],
                    "publication_date": str(row["publication_date"]) IF row["publication_date"] ELSE None,
                    "last_processed_at": str(row["last_processed_at"]) IF row["last_processed_at"] ELSE None,
                    **(row["metadata_jsonb"] IF row["metadata_jsonb"] ELSE {}) # Merge JSONB fields
                }
                logger.info(f"Retrieved metadata for doc_id: {doc_id}")
                RETURN {"success": True, "metadata": metadata}
            ELSE:
                logger.warning(f"Metadata not found for doc_id: {doc_id}")
                RETURN {"success": False, "metadata": None, "error": f"Document with doc_id {doc_id} not found."}
    CATCH McpError as e: # Handles DB errors from _get_cursor
        RETURN {"success": False, "metadata": None, "error": e.message}

```
#### TDD Anchors: `get_document_metadata`
*   Test successful retrieval of metadata for an existing `doc_id`.
*   Test retrieval attempt for a non-existent `doc_id` (expect `success: False`, `metadata: null`, specific error message).
*   Test handling of database connection errors during the query (expect `InternalError`).
*   Verify the structure of the returned `metadata` object, including fields from `metadata_jsonb`.
*   Test with a document that has null values for optional fields.

## 4. PhilAPI-MCP Server Specification

*   **Purpose:** Provides a dedicated interface for RooCode modes (primarily `Researcher`) to interact with external philosophy-specific APIs, starting with PhilPapers and potentially extending to Open Library and DOAB. Abstracts API complexities and manages API keys securely.
*   **Based On:** `docs/philosophy_assistant_architecture.md`, `docs/roomodes/programmatic_access_to_philosophy_databases.md`.
*   **Dependencies (Potential):** `modelcontextprotocol-sdk`, `requests` (or `httpx` for async), `python-dotenv`.

### 4.1. Setup and Initialization

*   **Environment Variables:** Reads the following from `env` (set in RooCode MCP config):
    *   `PHILPAPERS_API_KEY` (Optional, depending on PhilPapers API requirements - documentation suggests not strictly needed but recommended to inform them).
    *   `OPENLIBRARY_API_KEY` (Optional, if needed for higher rate limits or specific features).
    *   `DOAB_API_KEY` (Optional, if needed).
    *   `LOG_LEVEL` (optional, default: `INFO`)
    *   `REQUESTS_TIMEOUT` (optional, default: 30 seconds).
*   **HTTP Client:** Initializes an HTTP client instance (e.g., `requests.Session` or `httpx.AsyncClient`) for making API calls. Configure base URLs and default headers if applicable. Set timeout based on env var.

```pseudocode
# --- PhilAPI-MCP: Initialization ---
IMPORT os, sys, logging, json
IMPORT requests # Or httpx for async
IMPORT load_dotenv from dotenv
IMPORT McpServer, StdioServerTransport, McpToolHandler, McpError, McpToolContext, ErrorCode from modelcontextprotocol.server

load_dotenv()
logger = configure_logging(level=os.getenv("LOG_LEVEL", "INFO"))

# Read API keys from environment variables (optional, based on actual API needs)
PHILPAPERS_API_KEY = os.getenv("PHILPAPERS_API_KEY")
# OPENLIBRARY_API_KEY = os.getenv("OPENLIBRARY_API_KEY")
# DOAB_API_KEY = os.getenv("DOAB_API_KEY")
REQUESTS_TIMEOUT = int(os.getenv("REQUESTS_TIMEOUT", 30))

# Base URLs (Confirm actual endpoints from documentation)
PHILPAPERS_BASE_URL = "https://philpapers.org/oai.json" # Example, confirm actual JSON API endpoint
OPENLIBRARY_BASE_URL = "https://openlibrary.org"
DOAB_BASE_URL = "https://directory.doabooks.org/rest/search" # Example, confirm actual endpoint

CLASS PhilApiMcpServer inherits McpServer:
    FUNCTION __init__(self):
        super().__init__(name="philapi-mcp", title="Philosophy APIs MCP Server", description="Provides tools to query external philosophy APIs.", capabilities={"tools": {}})
        # Initialize HTTP client (using requests for simplicity in pseudocode)
        self.http_session = requests.Session()
        self.http_session.headers.update({"User-Agent": "RooCodePhilApiMcpServer/1.0"})
        # Add API keys to headers if needed, e.g.:
        # IF PHILPAPERS_API_KEY: self.http_session.headers.update({"Authorization": f"Bearer {PHILPAPERS_API_KEY}"})

    # ... Tool handlers defined below ...

    # Helper for making API requests and handling common errors
    FUNCTION _make_api_request(self, method, url, params=None, data=None, headers=None):
        TRY
            response = self.http_session.request(
                method=method,
                url=url,
                params=params,
                json=data, # Assuming JSON data if POST/PUT
                headers=headers,
                timeout=REQUESTS_TIMEOUT
            )
            response.raise_for_status() # Raises HTTPError for 4xx/5xx status codes
            TRY
                RETURN response.json()
            CATCH json.JSONDecodeError:
                 logger.error(f"Failed to decode JSON response from {url}")
                 RAISE McpError(ErrorCode.InternalError, f"Invalid JSON response received from API: {url}")
        CATCH requests.exceptions.Timeout as e:
            logger.error(f"API request timed out: {url}")
            RAISE McpError(ErrorCode.InternalError, f"API request timed out: {e}") from e
        CATCH requests.exceptions.RequestException as e:
            logger.error(f"API request failed: {url} - {e}")
            status_code = e.response.status_code IF e.response IS NOT None ELSE None
            # Customize error based on status code if needed
            IF status_code == 429: # Too Many Requests
                 RAISE McpError(ErrorCode.InternalError, f"API rate limit exceeded for {url}. Please try again later.") from e
            ELSE IF status_code == 404: # Not Found
                 # Let specific handlers deal with 404 if needed, otherwise raise generic
                 RAISE McpError(ErrorCode.InternalError, f"API resource not found (404): {url}") from e
            ELSE:
                 RAISE McpError(ErrorCode.InternalError, f"API request failed: {e}") from e

    ASYNC FUNCTION start(self):
        transport = StdioServerTransport()
        transport.on_close = self.shutdown
        logger.info('PhilAPI MCP Server starting to listen on stdio...')
        AWAIT self.listen(transport)
        logger.info('PhilAPI MCP Server listening.')

    ASYNC FUNCTION shutdown(self):
        logger.info("Shutting down PhilAPI MCP server...")
        self.http_session.close()
        AWAIT super().close()
        logger.info("PhilAPI MCP Server shut down complete.")

# --- Entry Point ---
# Similar to DB-MCP entry point
```

### 4.2. Tool: `search_philpapers`

*   **Purpose:** Searches the PhilPapers database via its JSON API.
*   **Input Parameters:** `query` (string, required), `filters` (object|null, optional - specific filter keys depend on PhilPapers API capabilities, e.g., `publicationYear`, `author`).
*   **Core Logic:**
    *   Constructs the API request URL and parameters for the PhilPapers JSON API endpoint. Include `apiKey` if required/available. Map input `filters` to API query parameters.
    *   Makes an HTTP GET request using the `_make_api_request` helper.
    *   Parses the JSON response.
    *   Maps the relevant fields from the API response (e.g., title, authors, abstract, URL, ID) to the specified output schema.
*   **External Interactions:** HTTP GET request to PhilPapers JSON API.
*   **Success Output:** `{"success": True, "results": [ { "title": ..., "authors": [...], "abstract": ..., "url": ..., "source_id": ... }, ... ]}`
*   **Error Handling:** Uses `_make_api_request` which handles timeouts, connection errors, non-2xx status codes (including rate limits), and JSON parsing errors, returning appropriate `McpError`.

```pseudocode
# --- PhilAPI-MCP: search_philpapers Handler ---
@McpToolHandler(
    name="search_philpapers",
    description="Searches the PhilPapers database.",
    input_schema={
        "type": "object",
        "properties": {
            "query": {"type": "string", "description": "Search query terms."},
            "filters": {"type": ["object", "null"], "description": "Optional filters (e.g., {'publicationYear': 2023, 'author': 'Kant'}). Keys depend on PhilPapers API."}
        },
        "required": ["query"]
    },
    output_schema={
        "type": "object",
        "properties": {
            "success": {"type": "boolean"},
            "results": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "title": {"type": ["string", "null"]},
                        "authors": {"type": "array", "items": {"type": "string"}},
                        "abstract": {"type": ["string", "null"]},
                        "url": {"type": ["string", "null"]},
                        "source_id": {"type": ["string", "integer", "null"], "description": "Unique ID from PhilPapers."}
                    },
                    "required": ["title", "authors", "source_id"]
                }
            },
            "error": {"type": "string"}
        },
        "required": ["success"]
    }
)
ASYNC FUNCTION search_philpapers(self, context: McpToolContext, params: Dict) -> Dict:
    query = params.get("query")
    filters = params.get("filters", {})

    # TDD: Test query construction with various filters
    # Confirm actual PhilPapers JSON API parameters
    api_params = {"q": query}
    IF PHILPAPERS_API_KEY: api_params["apiKey"] = PHILPAPERS_API_KEY # Add key if needed
    # Map input filters to PhilPapers API query parameters (example)
    IF "publicationYear" IN filters: api_params["pubYear"] = filters["publicationYear"] # Assuming 'pubYear' is the API param
    IF "author" IN filters: api_params["author"] = filters["author"]
    # Add other filter mappings as supported by the API

    TRY
        # TDD: Test successful API call and response parsing
        # TDD: Test API call with filters applied
        # TDD: Test handling of API errors (4xx, 5xx, timeout, rate limit) via _make_api_request
        # TDD: Test handling of empty results from API
        api_response = self._make_api_request("GET", PHILPAPERS_BASE_URL, params=api_params) # Confirm endpoint

        # TDD: Test mapping of various API response structures to output schema
        results = []
        # Assuming api_response is a list of result objects based on PhilPapers JSON API structure
        IF isinstance(api_response, list):
             FOR item IN api_response:
                  # Extract and map fields carefully based on actual API response
                  results.append({
                      "title": item.get("title"),
                      "authors": item.get("authors", []), # Assuming authors is a list
                      "abstract": item.get("abstract"),
                      "url": item.get("url"),
                      "source_id": item.get("id") # Assuming 'id' is the unique identifier
                  })

        logger.info(f"PhilPapers search for '{query}' returned {len(results)} results.")
        RETURN {"success": True, "results": results}
    CATCH McpError as e:
        # TDD: Test propagation of McpError from _make_api_request
        RETURN {"success": False, "error": e.message}

```
#### TDD Anchors: `search_philpapers`
*   Test successful search with a simple query, verifying response structure.
*   Test search yielding zero results.
*   Test search using various supported `filters` (e.g., year, author), verifying API parameters are constructed correctly based on actual PhilPapers API documentation.
*   Test handling of PhilPapers API errors (e.g., 400 Bad Request, 403 Forbidden/API Key issue, 429 Rate Limit, 500 Internal Server Error) via `_make_api_request`.
*   Test handling of network errors (timeout, connection refused) via `_make_api_request`.
*   Test handling of invalid JSON responses from the API via `_make_api_request`.
*   Test mapping logic for different variations in the API response structure (e.g., missing optional fields like abstract or url).

### 4.3. Tool: `get_philpapers_details`

*   **Purpose:** Retrieves detailed information for a specific PhilPapers entry using its unique ID.
*   **Input Parameters:** `source_id` (string, required).
*   **Core Logic:**
    *   Constructs the API request URL for fetching details by ID (endpoint needs confirmation from PhilPapers API docs).
    *   Makes an HTTP GET request using `_make_api_request`.
    *   Parses the JSON response containing the detailed record.
*   **External Interactions:** HTTP GET request to PhilPapers JSON API (details endpoint).
*   **Success Output:** `{"success": True, "details": { ... }}` (Structure depends on API response).
*   **Error Handling:** Uses `_make_api_request`. Handles cases where the ID is not found (e.g., 404 error).

```pseudocode
# --- PhilAPI-MCP: get_philpapers_details Handler ---
@McpToolHandler(
    name="get_philpapers_details",
    description="Gets details for a PhilPapers entry by ID.",
    input_schema={
        "type": "object",
        "properties": {"source_id": {"type": "string", "description": "The unique ID from PhilPapers."}},
        "required": ["source_id"]
    },
    output_schema={
        "type": "object",
        "properties": {
            "success": {"type": "boolean"},
            "details": {"type": ["object", "null"], "description": "Detailed information object."},
            "error": {"type": "string"}
        },
        "required": ["success"]
    }
)
ASYNC FUNCTION get_philpapers_details(self, context: McpToolContext, params: Dict) -> Dict:
    source_id = params.get("source_id")

    # TDD: Confirm correct endpoint structure from PhilPapers API docs
    # Example: Assuming endpoint is like /record/{id} relative to a base API URL
    details_url = f"https://philpapers.org/rec/{source_id}.json" # Needs verification
    api_params = {}
    IF PHILPAPERS_API_KEY: api_params["apiKey"] = PHILPAPERS_API_KEY

    TRY
        # TDD: Test successful retrieval for valid ID
        # TDD: Test retrieval for invalid/non-existent ID (expect 404 -> McpError)
        # TDD: Test handling of API/network errors via _make_api_request
        api_response = self._make_api_request("GET", details_url, params=api_params)

        # Assuming api_response is the details object
        logger.info(f"Retrieved details for PhilPapers ID: {source_id}")
        RETURN {"success": True, "details": api_response}
    CATCH McpError as e:
        # Modify error message for 404 specifically if possible
        IF "404" IN e.message: # Basic check, refine based on actual error format
             RETURN {"success": False, "error": f"PhilPapers entry with ID '{source_id}' not found."}
        ELSE:
             RETURN {"success": False, "error": e.message}

```
#### TDD Anchors: `get_philpapers_details`
*   Test successful retrieval for a known, valid `source_id`.
*   Test retrieval attempt for an invalid or non-existent `source_id` (expect `success: False`, specific "not found" error).
*   Test handling of PhilPapers API errors (e.g., 403, 429, 500) via `_make_api_request`.
*   Test handling of network errors (timeout, connection refused) via `_make_api_request`.
*   Verify the structure of the returned `details` object matches the expected API response based on PhilPapers documentation.

### 4.4. Tool: `search_other_apis` (Optional Extension)

*   **Purpose:** Searches other relevant APIs like Open Library or DOAB.
*   **Input Parameters:** `query` (string, required), `source` (enum: 'openlibrary' | 'doab', required), `filters` (object|null, optional).
*   **Core Logic:**
    *   Uses a `switch` or `if/elif` based on the `source` parameter.
    *   **Open Library:** Constructs request to Open Library Search API (e.g., `http://openlibrary.org/search.json`). Maps `query` and `filters` (e.g., `title`, `author`) to API parameters. Makes GET request via `_make_api_request`. Parses response (list of docs) and maps fields (`title`, `author_name`, `key` as `source_id`, `seed` for URL).
    *   **DOAB:** Constructs request to DOAB REST API (`/rest/search`). Maps `query` and `filters` to API parameters (e.g., `q`, `fq`). Makes GET request via `_make_api_request`. Parses response and maps fields (`dc.title`, `dc.creator`, `handle` as `source_id`, URL).
*   **External Interactions:** HTTP GET requests to Open Library API or DOAB API.
*   **Success Output:** `{"success": True, "results": [ { "title": ..., "authors": [...], "source_id": ..., "url": ... }, ... ]}`
*   **Error Handling:** Uses `_make_api_request`. Handles source-specific API errors or response formats. Returns `McpError(InvalidParams)` if `source` is unsupported.

```pseudocode
# --- PhilAPI-MCP: search_other_apis Handler ---
@McpToolHandler(
    name="search_other_apis",
    description="Searches Open Library or DOAB.",
    input_schema={
        "type": "object",
        "properties": {
            "query": {"type": "string"},
            "source": {"type": "string", "enum": ["openlibrary", "doab"]},
            "filters": {"type": ["object", "null"], "description": "API-specific filters."}
        },
        "required": ["query", "source"]
    },
    output_schema={
        "type": "object",
        "properties": {
            "success": {"type": "boolean"},
            "results": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "title": {"type": ["string", "null"]},
                        "authors": {"type": "array", "items": {"type": "string"}},
                        "source_id": {"type": ["string", "null"], "description": "Unique ID from the source API."},
                        "url": {"type": ["string", "null"]}
                    },
                    "required": ["title", "authors", "source_id"]
                }
            },
            "error": {"type": "string"}
        },
        "required": ["success"]
    }
)
ASYNC FUNCTION search_other_apis(self, context: McpToolContext, params: Dict) -> Dict:
    query = params.get("query")
    source = params.get("source") # 'openlibrary' or 'doab'
    filters = params.get("filters", {})

    results = []
    TRY
        IF source == "openlibrary":
            # TDD: Test Open Library search (query, filters)
            ol_params = {"q": query}
            IF "title" IN filters: ol_params["title"] = filters["title"]
            IF "author" IN filters: ol_params["author"] = filters["author"]
            # Add other relevant Open Library filters based on their API docs
            ol_url = f"{OPENLIBRARY_BASE_URL}/search.json"
            api_response = self._make_api_request("GET", ol_url, params=ol_params)

            # TDD: Test parsing of Open Library response structure ('docs' array)
            IF api_response AND "docs" IN api_response:
                FOR doc IN api_response["docs"]:
                     # Construct URL: https://openlibrary.org{key}
                     ol_url = f"{OPENLIBRARY_BASE_URL}{doc.get('key')}" if doc.get('key') else None
                     results.append({
                         "title": doc.get("title"),
                         "authors": doc.get("author_name", []),
                         "source_id": doc.get("key"), # Open Library key
                         "url": ol_url
                     })

        ELSE IF source == "doab":
            # TDD: Test DOAB search (query, filters)
            # Confirm DOAB API parameters from documentation
            doab_params = {"q": query}
            # Map filters to DOAB 'fq' parameters if needed
            # Example: IF "subject" IN filters: doab_params["fq"] = f"dc.subject:{filters['subject']}"
            api_response = self._make_api_request("GET", DOAB_BASE_URL, params=doab_params) # Confirm endpoint

            # TDD: Test parsing of DOAB response structure (likely a list)
            IF isinstance(api_response, list): # Assuming DOAB returns a list
                 FOR item IN api_response:
                      # Extract fields based on DOAB API response structure (e.g., dc.* fields)
                      # Construct URL from handle if possible
                      handle = item.get("handle") # Example field name
                      doab_url = f"https://doi.org/{handle}" IF handle AND handle.startswith("10.") ELSE handle # Example URL construction
                      results.append({
                          "title": item.get("dc.title", [None])[0], # Assuming title is in a list
                          "authors": item.get("dc.creator", []), # Assuming creators is a list
                          "source_id": handle,
                          "url": doab_url
                      })
        ELSE:
            # TDD: Test invalid source parameter
            RAISE McpError(ErrorCode.InvalidParams, f"Unsupported source specified: '{source}'. Use 'openlibrary' or 'doab'.")

        logger.info(f"{source} search for '{query}' returned {len(results)} results.")
        RETURN {"success": True, "results": results}

    CATCH McpError as e:
        # TDD: Test propagation of McpError from _make_api_request or validation
        RETURN {"success": False, "error": e.message}

```
#### TDD Anchors: `search_other_apis`
*   Test successful search on Open Library with a simple query.
*   Test successful search on DOAB with a simple query.
*   Test search on Open Library using supported `filters` based on their API documentation.
*   Test search on DOAB using supported `filters` (e.g., `fq` parameter) based on their API documentation.
*   Test handling of invalid `source` parameter (expect `InvalidParams` error).
*   Test handling of API errors (4xx, 5xx, timeout, rate limit) for both Open Library and DOAB via `_make_api_request`.
*   Test handling of network errors for both APIs via `_make_api_request`.
*   Test parsing logic for different response structures from Open Library (`docs` array) and DOAB (likely a list with `dc.*` fields).
*   Test handling of empty results from both APIs.
*   Verify the structure of the returned `results` array for both sources, including correct URL construction.

## 5. ChunkerEmbedder-MCP Server Specification

*   **Purpose:** (Optional Alternative to Shell Script) Encapsulates the logic for reading a processed text file, chunking its content, generating vector embeddings for the chunks, and coordinating with `DB-MCP` to store the document metadata and chunk data.
*   **Based On:** `docs/philosophy_assistant_architecture.md`, `docs/roomodes/roocode-rag-research-assistant.md`.
*   **Dependencies (Potential):** `modelcontextprotocol-sdk`, `tiktoken` (for chunk size estimation), `openai` (or other embedding API client), `python-dotenv`, potentially `httpx` (if calling `DB-MCP` via HTTP, though less likely for stdio-based MCPs). **Crucially, this server needs a way to call the `DB-MCP` server.**

### 5.1. Setup and Initialization

*   **Environment Variables:** Reads the following from `env`:
    *   `EMBEDDING_API_KEY` (e.g., `OPENAI_API_KEY`, **Required** if using API).
    *   `EMBEDDING_MODEL_NAME` (optional, default: e.g., `text-embedding-3-small`).
    *   `CHUNK_SIZE` (optional, default: e.g., 1000 tokens).
    *   `CHUNK_OVERLAP` (optional, default: e.g., 100 tokens).
    *   `LOG_LEVEL` (optional, default: `INFO`).
    *   `DB_MCP_SERVER_NAME` (optional, default: `db-mcp`, needed if calling DB-MCP via MCP client - Option A).
*   **Embedding Client:** Initializes the client for the chosen embedding model (e.g., `openai.OpenAI()`). Handles missing API key gracefully (logs warning, tool calls will fail).
*   **Chunking Parameters:** Stores chunk size and overlap from env vars. Validates that overlap < size. Uses `tiktoken` to get tokenizer for the specified embedding model.
*   **DB-MCP Client (Challenge):** This server needs to *call* `DB-MCP`.
    *   **Option A (Recommended if feasible):** Instantiate an MCP *Client* within this server process to communicate with `DB-MCP` (assuming `DB-MCP` is running). This requires the `modelcontextprotocol-sdk` client components and a mechanism to discover/connect to the `DB-MCP` stdio process (potentially complex).
    *   **Option B (Alternative):** Directly use `psycopg2` within this server to connect to the database, duplicating the connection logic from `DB-MCP`. This violates the principle of `DB-MCP` being the *sole* interface but might be simpler to implement initially. **The spec will assume Option A for better architecture, but acknowledge Option B as a fallback.**

```pseudocode
# --- ChunkerEmbedder-MCP: Initialization ---
IMPORT os, sys, logging, json
IMPORT tiktoken # For chunking by tokens
IMPORT openai # Example embedding provider
IMPORT load_dotenv from dotenv
IMPORT McpServer, StdioServerTransport, McpToolHandler, McpError, McpToolContext, ErrorCode from modelcontextprotocol.server
# Potentially import MCP Client components if using Option A
# from modelcontextprotocol.client import Client, StdioClientTransport # Example

load_dotenv()
logger = configure_logging(level=os.getenv("LOG_LEVEL", "INFO"))

# Embedding Config
EMBEDDING_API_KEY = os.getenv("EMBEDDING_API_KEY")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL_NAME", "text-embedding-3-small")
embedding_client_initialized = False
IF NOT EMBEDDING_API_KEY:
    logger.warning("EMBEDDING_API_KEY not set. Embedding generation will fail.")
ELSE:
    TRY:
        # Initialize OpenAI client (or other provider)
        embedding_client = openai.OpenAI(api_key=EMBEDDING_API_KEY) # Assuming sync client for simplicity here
        logger.info(f"Initialized embedding client for model: {EMBEDDING_MODEL}")
        embedding_client_initialized = True
    CATCH Exception as e:
         logger.error(f"Failed to initialize embedding client: {e}")
         # Allow server to start but log error

# Chunking Config
TRY:
    CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 1000))
    CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 100))
    IF CHUNK_OVERLAP >= CHUNK_SIZE: RAISE ValueError("Overlap must be less than size.")
    tokenizer = tiktoken.encoding_for_model(EMBEDDING_MODEL) # Or appropriate tokenizer
CATCH ValueError as e:
    logger.error(f"Invalid chunking parameters: {e}")
    sys.exit(f"Invalid Chunking Config: {e}")
CATCH Exception as e: # Handle errors getting tokenizer
    logger.error(f"Failed to get tokenizer for model {EMBEDDING_MODEL}: {e}")
    sys.exit(f"Tokenizer Error: {e}")


# DB-MCP Client Config (for Option A)
DB_MCP_SERVER_NAME = os.getenv("DB_MCP_SERVER_NAME", "db-mcp")

CLASS ChunkerEmbedderMcpServer inherits McpServer:
    FUNCTION __init__(self):
        super().__init__(name="chunker-embedder-mcp", title="Chunking & Embedding MCP Server", description="Processes text files into chunks and embeddings, storing via DB-MCP.", capabilities={"tools": {}})
        self.tokenizer = tokenizer # Store tokenizer instance
        self.embedding_client = embedding_client if embedding_client_initialized else None

        # DB-MCP Client (Option A - Conceptual, requires SDK support/clarification)
        # self.db_mcp_client = Client()
        # self.db_mcp_transport = StdioClientTransport(command="...", args=["..."]) # How to find/start DB-MCP? Complex.
        # Need to handle async connection if required by SDK

        # DB Connection (Option B - Fallback, duplicates DB-MCP logic)
        # self.db_conn = None
        # self._connect_db_direct() # Implement connection logic similar to DB-MCP

    # --- Helper: Chunking Logic ---
    FUNCTION _chunk_text(self, text: str) -> List[str]:
        # Simple token-based chunking with overlap
        tokens = self.tokenizer.encode(text)
        chunks_tokens = []
        start_index = 0
        WHILE start_index < len(tokens):
            end_index = min(start_index + CHUNK_SIZE, len(tokens))
            chunks_tokens.append(tokens[start_index:end_index])
            # Move start index forward, considering overlap
            next_start = start_index + CHUNK_SIZE - CHUNK_OVERLAP
            IF next_start <= start_index: # Prevent infinite loop if overlap >= size
                 next_start = start_index + 1 # Ensure progress
            start_index = next_start
            IF start_index >= len(tokens): BREAK # Ensure termination

        # Decode token chunks back to text
        text_chunks = [self.tokenizer.decode(chunk) for chunk in chunks_tokens]
        RETURN text_chunks

    # --- Helper: Embedding Logic ---
    # Assuming sync client for simplicity in pseudocode, use async/await if client is async
    FUNCTION _get_embeddings(self, texts: List[str]) -> List[List[float]]:
        IF self.embedding_client IS None:
             RAISE McpError(ErrorCode.InternalError, "Embedding client not initialized (missing API key?).")

        all_embeddings = []
        batch_size = 100 # Or provider-specific limit (e.g., OpenAI allows up to 2048)
        FOR i IN range(0, len(texts), batch_size):
            batch = texts[i:i + batch_size]
            # Replace newlines as recommended by OpenAI API docs
            batch = [t.replace("\n", " ") for t in batch]
            TRY
                # Use sync client call here
                response = self.embedding_client.embeddings.create(input=batch, model=EMBEDDING_MODEL)
                batch_embeddings = [item.embedding for item in response.data]
                all_embeddings.extend(batch_embeddings)
            CATCH Exception as e: # Catch specific API errors if possible (e.g., openai.APIError)
                logger.error(f"Embedding API call failed: {e}")
                RAISE McpError(ErrorCode.InternalError, f"Embedding generation failed: {e}") from e
        RETURN all_embeddings

    # --- Helper: Call DB-MCP (Option A - Conceptual) ---
    # ASYNC FUNCTION _call_db_mcp(self, tool_name: str, args: Dict) -> Dict:
    #     # Implementation depends heavily on how MCP client works within server
    #     # Needs to locate and communicate with the running DB-MCP process
    #     logger.debug(f"Calling DB-MCP tool '{tool_name}' with args: {args}")
    #     # ... logic to send request and receive response ...
    #     # Placeholder:
    #     IF tool_name == "add_document": RETURN {"success": True, "doc_id": 123}
    #     IF tool_name == "batch_insert_chunks": RETURN {"success": True, "inserted_count": len(args.get("chunks",[]))}
    #     RAISE McpError(ErrorCode.InternalError, "DB-MCP client interaction not implemented.")

    # ... Tool handler defined below ...

    ASYNC FUNCTION start(self):
        transport = StdioServerTransport()
        transport.on_close = self.shutdown
        logger.info('ChunkerEmbedder MCP Server starting to listen on stdio...')
        AWAIT self.listen(transport)
        logger.info('ChunkerEmbedder MCP Server listening.')

    ASYNC FUNCTION shutdown(self):
        logger.info("Shutting down ChunkerEmbedder MCP server...")
        # Close DB-MCP client connection if using Option A
        # Close direct DB connection if using Option B
        AWAIT super().close()
        logger.info("ChunkerEmbedder MCP Server shut down complete.")

# --- Entry Point ---
# Similar to DB-MCP entry point
```

### 5.2. Tool: `process_text_file`

*   **Purpose:** Orchestrates the chunking, embedding, and storage process for a single text file.
*   **Input Parameters:** `file_path` (string, required), `doc_metadata` (object, required - contains `source_uri` and potentially other fields like `title`, `authors` needed by `DB-MCP`).
*   **Core Logic:**
    1.  **Read File:** Open and read the content of the text file specified by `file_path`. Handle potential `FileNotFoundError` or permission errors.
    2.  **Chunk Text:** Call the internal `_chunk_text` helper function to split the content into chunks based on configured size and overlap.
    3.  **Generate Embeddings:** Call the internal `_get_embeddings` helper function to get vector embeddings for all chunks (using batching).
    4.  **Store Document Metadata (via DB-MCP - Option A):**
        *   Call the `DB-MCP` server's `add_document` tool using the conceptual `_call_db_mcp` helper, passing the `doc_metadata` received as input.
        *   Extract the returned `doc_id`. Handle potential errors from the `DB-MCP` call.
    5.  **Store Chunks (via DB-MCP - Option A):**
        *   Prepare the list of chunk objects required by `DB-MCP`'s `batch_insert_chunks` tool (including the `doc_id`, `chunk_index`, `chunk_text`, and `embedding`).
        *   Call the `DB-MCP` server's `batch_insert_chunks` tool using the conceptual `_call_db_mcp` helper.
        *   Handle potential errors from the `DB-MCP` call.
    6.  **(Alternative DB Interaction - Option B):** If not calling `DB-MCP`, perform steps 4 & 5 using direct `psycopg2` calls, similar to the logic within `DB-MCP` itself (requires adding DB connection logic to this server).
*   **External Interactions:**
    *   File system read operations.
    *   HTTP requests to the embedding API (e.g., OpenAI).
    *   MCP requests to `DB-MCP` server (Option A) OR Direct PostgreSQL connection (Option B).
*   **Success Output:** `{"success": True, "doc_id": <integer>, "chunk_count": <integer>}`
*   **Error Handling:**
    *   Catches file I/O errors (FileNotFound, Permissions), returns `McpError(InvalidParams)` or `InternalError`.
    *   Catches embedding API errors (via `_get_embeddings`), returns `McpError(InternalError)`.
    *   Catches errors during calls to `DB-MCP` (Option A) or direct DB interaction (Option B), returns `McpError(InternalError)`.

```pseudocode
# --- ChunkerEmbedder-MCP: process_text_file Handler ---
@McpToolHandler(
    name="process_text_file",
    description="Chunks, embeds, and stores a text file via DB-MCP.",
    input_schema={
        "type": "object",
        "properties": {
            "file_path": {"type": "string", "description": "Path to the processed text file."},
            "doc_metadata": {"type": "object", "description": "Metadata object including source_uri, title, authors etc."}
        },
        "required": ["file_path", "doc_metadata"]
    },
    output_schema={
        "type": "object",
        "properties": {
            "success": {"type": "boolean"},
            "doc_id": {"type": ["integer", "null"]},
            "chunk_count": {"type": ["integer", "null"]},
            "error": {"type": "string"}
        },
        "required": ["success"]
    }
)
# Assuming sync handler for simplicity, use async/await if helpers are async
FUNCTION process_text_file(self, context: McpToolContext, params: Dict) -> Dict:
    file_path = params.get("file_path")
    doc_metadata = params.get("doc_metadata") # Must contain source_uri etc.

    # TDD: Test with non-existent file_path
    # TDD: Test with file_path having read permission issues
    TRY:
        WITH open(file_path, 'r', encoding='utf-8') as f:
            text_content = f.read()
        logger.info(f"Read {len(text_content)} characters from '{file_path}'.")
    CATCH FileNotFoundError:
        RAISE McpError(ErrorCode.InvalidParams, f"Input file not found: {file_path}")
    CATCH IOError as e:
        RAISE McpError(ErrorCode.InternalError, f"Failed to read file {file_path}: {e}")

    # TDD: Test chunking with various text lengths (empty, small, large)
    # TDD: Test chunking respects CHUNK_SIZE and CHUNK_OVERLAP
    chunks = self._chunk_text(text_content)
    IF NOT chunks:
         logger.warning(f"No chunks generated for file: {file_path}")
         RETURN {"success": True, "doc_id": None, "chunk_count": 0} # Handle empty file case
    logger.info(f"Generated {len(chunks)} chunks.")

    # TDD: Test embedding generation (success, API key error, rate limit, other API errors)
    TRY:
        embeddings = self._get_embeddings(chunks) # Assuming sync helper
        IF len(embeddings) != len(chunks):
             RAISE McpError(ErrorCode.InternalError, "Mismatch between chunk count and embedding count.")
    CATCH McpError as e:
        RETURN {"success": False, "error": f"Embedding failed: {e.message}"}

    # --- Store via DB-MCP (Option A - Conceptual) ---
    doc_id = None
    inserted_chunk_count = 0
    TRY:
        # TDD: Test calling DB-MCP add_document (success, failure)
        # Ensure doc_metadata contains required fields like source_uri
        IF "source_uri" NOT IN doc_metadata:
             RAISE McpError(ErrorCode.InvalidParams, "doc_metadata must include 'source_uri'.")

        # --- This assumes self._call_db_mcp is implemented ---
        # add_doc_result = self._call_db_mcp("add_document", doc_metadata) # Assuming sync helper
        # IF NOT add_doc_result.get("success"):
        #      RAISE McpError(ErrorCode.InternalError, f"DB-MCP add_document failed: {add_doc_result.get('error')}")
        # doc_id = add_doc_result.get("doc_id")
        # IF doc_id IS None: RAISE McpError(ErrorCode.InternalError, "DB-MCP add_document did not return doc_id.")

        # logger.info(f"DB-MCP returned doc_id: {doc_id}")

        # chunks_payload = []
        # FOR index, (text, embedding) IN enumerate(zip(chunks, embeddings)):
        #     chunks_payload.append({
        #         "chunk_index": index, # Assuming 0-based index
        #         "chunk_text": text,
        #         "embedding": embedding
        #     })

        # TDD: Test calling DB-MCP batch_insert_chunks (success, failure)
        # insert_chunks_result = self._call_db_mcp("batch_insert_chunks", {"document_id": doc_id, "chunks": chunks_payload}) # Assuming sync helper
        # IF NOT insert_chunks_result.get("success"):
        #      RAISE McpError(ErrorCode.InternalError, f"DB-MCP batch_insert_chunks failed: {insert_chunks_result.get('error')}")
        # inserted_chunk_count = insert_chunks_result.get("inserted_count", 0) # Use reported count

        # --- Placeholder for Option A ---
        logger.warning("DB-MCP client interaction not fully implemented in pseudocode (Option A).")
        # Simulate success for pseudocode flow
        doc_id = 123 # Dummy ID
        inserted_chunk_count = len(chunks)
        # --- End Placeholder ---


        # --- Store Directly (Option B - Fallback) ---
        # IF using Option B, implement direct DB calls here similar to DB-MCP's handlers
        # WITH self._get_cursor_direct(commit=True) as cur:
        #      # Execute INSERT for document RETURNING doc_id
        #      # Execute batch INSERT for chunks using execute_values
        #      pass # Placeholder

        logger.info(f"Successfully processed and stored {inserted_chunk_count} chunks for doc_id {doc_id}.")
        RETURN {"success": True, "doc_id": doc_id, "chunk_count": inserted_chunk_count}

    CATCH McpError as e:
        # TDD: Test handling of errors during DB interaction phase
        RETURN {"success": False, "error": e.message}
    CATCH Exception as e:
        logger.error(f"Unexpected error during DB storage phase: {e}", exc_info=True)
        RETURN {"success": False, "error": f"Unexpected error during storage: {e}"}

```
#### TDD Anchors: `process_text_file`
*   Test with a valid `file_path` and `doc_metadata`.
*   Test with a `file_path` that does not exist (expect `InvalidParams` error).
*   Test with a `file_path` that the server lacks read permissions for (expect `InternalError`).
*   Test with an empty input file (verify `chunk_count` is 0).
*   Test with a very large input file to check chunking and embedding batching performance/memory usage.
*   Test chunking logic correctly handles text boundaries and overlap based on `CHUNK_SIZE` and `CHUNK_OVERLAP`.
*   Test embedding generation failure due to missing/invalid API key (expect `InternalError`).
*   Test embedding generation failure due to API rate limits (expect `InternalError`).
*   **If using Option A (Call DB-MCP):**
    *   Test failure during `add_document` call to `DB-MCP` (expect `InternalError`).
    *   Test failure during `batch_insert_chunks` call to `DB-MCP` (expect `InternalError`).
    *   Test scenario where `add_document` succeeds but `batch_insert_chunks` fails.
    *   Test handling of missing `source_uri` in `doc_metadata` (expect `InvalidParams` error).
*   **If using Option B (Direct DB):**
    *   Test direct DB insertion failures (connection, constraints) for both document and chunks.
*   Verify the `doc_id` and `chunk_count` in the success response match expectations.

## 6. Conclusion

This specification provides a detailed blueprint for implementing the `DB-MCP`, `PhilAPI-MCP`, and `ChunkerEmbedder-MCP` servers in Python. Adherence to these specifications, particularly regarding secure credential handling, robust error management, and efficient processing (batching), will be crucial for the successful operation of the Philosophical Research Assistant within the RooCode framework. The TDD anchors provide guidance for ensuring the correctness and reliability of each server's functionality.