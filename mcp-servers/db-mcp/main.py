#!/usr/bin/env python

import os
import json
import logging
import sys
from typing import List, Dict, Any, Optional, Tuple
from datetime import date

import psycopg2
import psycopg2.extras
import pgvector.psycopg2
from dotenv import load_dotenv

# Attempt to import the MCP SDK - handle potential import errors gracefully
try:
    from modelcontextprotocol.server import (
        McpServer,
        StdioServerTransport,
        McpToolHandler,
        McpError,
        McpToolContext,
        ErrorCode,
    )
    MCP_SDK_AVAILABLE = True
except ImportError:
    print("Error: modelcontextprotocol-sdk not found. Please install it.", file=sys.stderr)
    MCP_SDK_AVAILABLE = False
    # Define dummy classes/decorators if SDK is not available to allow basic script parsing
    class McpServer: pass
    class StdioServerTransport: pass
    class McpToolContext: pass
    class McpError(Exception): pass
    class ErrorCode:
        InternalError = -32603
        InvalidParams = -32602
        MethodNotFound = -32601
    def McpToolHandler(**kwargs):
        def decorator(func):
            return func
        return decorator

# --- Configuration ---
# Load environment variables from .env file (optional, for local development)
load_dotenv()

# Configure logging
logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO").upper(),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    stream=sys.stderr,  # Log to stderr for MCP stdio transport
)
logger = logging.getLogger("DbMcpServer")

# Database connection details from environment variables
DB_HOST = os.getenv("PGHOST", "localhost")
DB_PORT = os.getenv("PGPORT", "5432")
DB_NAME = os.getenv("PGDATABASE", "philosophy_rag") # Default DB name from architecture
DB_USER = os.getenv("PGUSER", "rag_agent_user") # Default user from RAG doc example
DB_PASSWORD = os.getenv("PGPASSWORD") # No default password for security

# Check if required DB password is set
if not DB_PASSWORD:
    logger.error("FATAL: PGPASSWORD environment variable is not set.")
    # Exit if essential config is missing, preventing RooCode from repeatedly trying to start a broken server
    sys.exit("DB Password not configured")

# --- Server Implementation ---

# Only define the server if the SDK was successfully imported
if MCP_SDK_AVAILABLE:
    class DbMcpServer(McpServer):
        """
        MCP Server for interacting with the PostgreSQL/pgvector database
        for the RAG system, based on docs/philosophy_assistant_architecture.md
        and docs/roomodes/roocode-rag-research-assistant.md.
        """

        def __init__(self):
            super().__init__(
                name="db-mcp", # Consistent name
                title="Database MCP Server (PostgreSQL/pgvector)",
                description="Provides tools to interact with the RAG vector database.",
                capabilities={"tools": {}} # Declare tool capability
            )
            self.db_conn = None
            self._connect_db() # Connect on initialization

        def _connect_db(self) -> None:
            """Establishes the database connection."""
            try:
                logger.info(f"Connecting to database '{DB_NAME}' at {DB_HOST}:{DB_PORT} as user '{DB_USER}'...")
                self.db_conn: Optional[psycopg2.connection] = psycopg2.connect(
                    dbname=DB_NAME,
                    user=DB_USER,
                    password=DB_PASSWORD,
                    host=DB_HOST,
                    port=DB_PORT,
                )
                pgvector.psycopg2.register_vector(self.db_conn) # Register pgvector type handler
                self.db_conn.autocommit = False # Ensure transactions are managed explicitly
                logger.info("Database connection successful.")
            except psycopg2.Error as e:
                logger.error(f"Database connection failed: {e}")
                # Raise McpError to signal failure clearly to RooCode/MCP Hub
                raise McpError(ErrorCode.InternalError, f"Database connection failed: {e}") from e

        def _get_cursor(self, commit: bool = False) -> psycopg2.extras.DictCursor:
            """
            Context manager for acquiring a database cursor and handling transactions.
            Ensures connection is valid and handles commit/rollback.
            """
            if self.db_conn is None or self.db_conn.closed != 0:
                logger.warning("Database connection lost or closed. Reconnecting...")
                self._connect_db() # This will raise McpError if reconnection fails

            if not self.db_conn:
                 # Should not happen if _connect_db raises error, but as safeguard:
                raise McpError(ErrorCode.InternalError, "Database connection is not available.")

            # Use DictCursor for easy access to columns by name
            cursor = self.db_conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            try:
                yield cursor
                if commit:
                    self.db_conn.commit()
                    logger.debug("Transaction committed.")
            except psycopg2.Error as db_err:
                logger.error(f"Database operation failed: {db_err}")
                self.db_conn.rollback()
                logger.warning("Transaction rolled back.")
                # Re-raise as McpError for the handler
                raise McpError(ErrorCode.InternalError, f"Database error: {db_err}") from db_err
            except Exception as e:
                logger.error(f"Unexpected error during DB operation: {e}")
                self.db_conn.rollback()
                logger.warning("Transaction rolled back due to unexpected error.")
                 # Re-raise as McpError
                raise McpError(ErrorCode.InternalError, f"Unexpected server error: {e}") from e
            finally:
                cursor.close()


        @McpToolHandler(
            name="add_document",
            description="Adds metadata for a new document to the database. Returns the new doc_id.",
            input_schema={
                "type": "object",
                "properties": {
                    "source_uri": {"type": "string", "description": "Unique URI identifying the source document (e.g., file path, URL)."},
                    "title": {"type": ["string", "null"], "description": "Title of the document."},
                    "authors": {"type": ["string", "null"], "description": "Author(s) of the document (comma-separated or similar)."},
                    "publication_date": {"type": ["string", "null"], "format": "date", "description": "Publication date (YYYY-MM-DD)."},
                    "metadata_jsonb": {"type": ["object", "null"], "description": "Flexible JSON object for additional metadata (e.g., abstract, journal)."},
                    "extracted_text_hash": {"type": ["string", "null"], "description": "Optional SHA-256 hash of the extracted text content."},
                },
                "required": ["source_uri"],
            },
            output_schema={
                "type": "object",
                "properties": {
                    "success": {"type": "boolean"},
                    "doc_id": {"type": ["integer", "null"], "description": "The ID of the newly inserted document if successful."},
                    "error": {"type": "string", "description": "Error message if the operation failed."},
                },
                "required": ["success"],
            },
        )
        async def add_document(self, context: McpToolContext, params: Dict[str, Any]) -> Dict[str, Any]:
            """Handles the add_document tool request."""
            source_uri = params.get("source_uri")
            title = params.get("title")
            authors = params.get("authors")
            pub_date_str = params.get("publication_date")
            metadata = params.get("metadata_jsonb")
            text_hash = params.get("extracted_text_hash")

            # Validate date format if provided
            pub_date: Optional[date] = None
            if pub_date_str:
                try:
                    pub_date = date.fromisoformat(pub_date_str)
                except ValueError:
                    raise McpError(ErrorCode.InvalidParams, f"Invalid date format for publication_date: '{pub_date_str}'. Use YYYY-MM-DD.")

            sql = """
                INSERT INTO documents (source_uri, title, authors, publication_date, metadata_jsonb, extracted_text_hash)
                VALUES (%s, %s, %s, %s, %s, %s)
                -- If a document with the same source_uri exists, update its fields instead of inserting a duplicate.
                ON CONFLICT (source_uri) DO UPDATE SET
                    title = EXCLUDED.title,
                    authors = EXCLUDED.authors,
                    publication_date = EXCLUDED.publication_date,
                    metadata_jsonb = EXCLUDED.metadata_jsonb,
                    extracted_text_hash = EXCLUDED.extracted_text_hash,
                    last_processed_at = NOW()
                RETURNING doc_id;
            """
            try:
                # Use context manager for cursor and transaction
                with self._get_cursor(commit=True) as cur:
                    cur.execute(sql, (
                        source_uri,
                        title,
                        authors,
                        pub_date,
                        json.dumps(metadata) if metadata else None, # Standardize: Use json.dumps for JSONB
                        text_hash
                    ))
                    result = cur.fetchone()
                    doc_id = result["doc_id"] if result else None
                    if doc_id:
                        logger.info(f"Added/Updated document '{source_uri}', doc_id: {doc_id}")
                        return {"success": True, "doc_id": doc_id}
                    else:
                        # Should not happen with RETURNING clause but handle defensively
                        logger.error(f"Failed to get doc_id after inserting/updating '{source_uri}'")
                        return {"success": False, "error": "Failed to retrieve doc_id after insert/update."}
            except McpError as e: # Catch errors raised by _get_cursor
                return {"success": False, "error": e.message}
            # No need for broad Exception catch here, _get_cursor handles it


        @McpToolHandler(
            name="batch_insert_chunks",
            description="Inserts multiple text chunks and their embeddings for a given document efficiently.",
            input_schema={
                "type": "object",
                "properties": {
                    "document_id": {"type": "integer", "description": "The ID of the document these chunks belong to."},
                    "chunks": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "chunk_text": {"type": "string", "description": "The text content of the chunk."},
                                "chunk_index": {"type": "integer", "description": "The sequential index of the chunk within the document (0-based or 1-based)."},
                                "embedding": {"type": "array", "items": {"type": "number"}, "description": "The vector embedding of the chunk text."},
                            },
                            "required": ["chunk_text", "chunk_index", "embedding"],
                        },
                        "description": "An array of chunk objects to insert.",
                        "minItems": 1
                    },
                },
                "required": ["document_id", "chunks"],
            },
            output_schema={
                "type": "object",
                "properties": {
                    "success": {"type": "boolean"},
                    "inserted_count": {"type": "integer", "description": "Number of chunks successfully inserted."},
                    "error": {"type": "string", "description": "Error message if the operation failed."},
                },
                "required": ["success"],
            },
        )
        async def batch_insert_chunks(self, context: McpToolContext, params: Dict[str, Any]) -> Dict[str, Any]:
            """Handles the batch_insert_chunks tool request using execute_values."""
            document_id = params.get("document_id")
            chunks_data = params.get("chunks", []) # Should have minItems: 1 from schema

            # Prepare data tuples for execute_values: (document_id, chunk_index, chunk_text, embedding)
            # The embedding needs to be passed as a list/tuple, pgvector adapter handles conversion
            values_list: List[Tuple[int, int, str, List[float]]] = [
                (document_id, chunk["chunk_index"], chunk["chunk_text"], chunk["embedding"])
                for chunk in chunks_data
            ]

            # Use ON CONFLICT to handle potential re-runs or updates. If a chunk with the
            # same document_id and chunk_index exists, update its text and embedding.
            sql = """
                INSERT INTO chunks (document_id, chunk_index, chunk_text, embedding)
                VALUES %s
                ON CONFLICT (document_id, chunk_index) DO UPDATE SET
                    chunk_text = EXCLUDED.chunk_text,
                    embedding = EXCLUDED.embedding;
            """

            try:
                 # Use context manager for cursor and transaction
                with self._get_cursor(commit=True) as cur:
                    # execute_values efficiently inserts multiple rows
                    psycopg2.extras.execute_values(cur, sql, values_list, page_size=100) # Adjust page_size as needed
                    inserted_count = cur.rowcount # Note: rowcount might be -1 or unreliable depending on driver/DB for ON CONFLICT
                    logger.info(f"Attempted batch insert/update for {len(values_list)} chunks for document_id: {document_id}. cursor.rowcount={inserted_count}")
                    # Since rowcount is unreliable with ON CONFLICT, we report success based on lack of exceptions
                    return {"success": True, "inserted_count": len(values_list)} # Report attempted count
            except McpError as e: # Catch errors raised by _get_cursor
                return {"success": False, "error": e.message, "inserted_count": 0}
            # No need for broad Exception catch here, _get_cursor handles it


        @McpToolHandler(
            name="query_similar_chunks",
            description="Performs vector similarity search (cosine distance) to find relevant chunks and their metadata.",
            input_schema={
                "type": "object",
                "properties": {
                    "query_embedding": {"type": "array", "items": {"type": "number"}, "description": "The vector embedding of the query."},
                    "top_k": {"type": "integer", "default": 5, "description": "Number of top similar chunks to retrieve."},
                    "filters": {"type": ["object", "null"], "description": "Optional key-value pairs to filter document metadata (JSONB field). Example: {'authors': 'Kant', 'publication_date_after': '1780-01-01'}"},
                },
                "required": ["query_embedding"],
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
                                "chunk_id": {"type": "integer"},
                                "document_id": {"type": "integer"},
                                "chunk_text": {"type": "string"},
                                "score": {"type": "number", "description": "Similarity score (lower is more similar for cosine distance <=>)."},
                                "metadata": {"type": "object", "description": "Metadata from the associated document (title, authors, date, source_uri, etc.)."},
                            },
                            "required": ["chunk_id", "document_id", "chunk_text", "score", "metadata"],
                        },
                         "description": "Array of matching chunks, ordered by similarity.",
                    },
                    "error": {"type": "string", "description": "Error message if the operation failed."},
                },
                "required": ["success"],
            },
        )
        async def query_similar_chunks(self, context: McpToolContext, params: Dict[str, Any]) -> Dict[str, Any]:
            """Handles the query_similar_chunks tool request."""
            query_embedding = params.get("query_embedding")
            top_k = params.get("top_k", 5)
            filters = params.get("filters") # Optional metadata filters

            # Base SQL query using cosine distance operator <=>
            base_sql = """
                SELECT
                    c.chunk_id,
                    c.document_id,
                    c.chunk_text,
                    c.embedding <=> %s AS score, -- Cosine distance: smaller is more similar
                    d.source_uri,
                    d.title,
                    d.authors,
                    d.publication_date,
                    d.metadata_jsonb -- Select the whole metadata JSONB field
                FROM chunks c
                JOIN documents d ON c.document_id = d.doc_id
            """
            where_clauses = []
            sql_params: list[Any] = [query_embedding] # Start with the embedding for the distance calculation (renamed from query_params)

            # Add metadata filters if provided
            if filters:
                for key, value in filters.items():
                    # Handle specific filter types if needed (e.g., date ranges)
                    if key == "publication_date_after":
                        try:
                            date_val = date.fromisoformat(str(value))
                            where_clauses.append("d.publication_date > %s")
                            sql_params.append(date_val)
                        except ValueError:
                             raise McpError(ErrorCode.InvalidParams, f"Invalid date format for filter '{key}': '{value}'. Use YYYY-MM-DD.")
                    elif key == "publication_date_before":
                         try:
                            date_val = date.fromisoformat(str(value))
                            where_clauses.append("d.publication_date < %s")
                            sql_params.append(date_val)
                         except ValueError:
                             raise McpError(ErrorCode.InvalidParams, f"Invalid date format for filter '{key}': '{value}'. Use YYYY-MM-DD.")
                    # Add more specific filters as needed (e.g., title ILIKE %s)
                    # Default: Assume filter applies to metadata_jsonb using @>
                    else:
                        where_clauses.append("d.metadata_jsonb @> %s")
                        # psycopg2 needs the filter value wrapped in a JSON string for @>
                        sql_params.append(json.dumps({key: value}))

            # Construct the final query
            if where_clauses:
                sql = f"{base_sql} WHERE {' AND '.join(where_clauses)}"
            else:
                sql = base_sql

            sql += " ORDER BY score ASC LIMIT %s;" # Order by distance, limit results
            sql_params.append(top_k)

            try:
                 # Use context manager for cursor (no commit needed for SELECT)
                with self._get_cursor() as cur:
                    logger.debug(f"Executing similarity query: {cur.mogrify(sql, sql_params)}")
                    cur.execute(sql, sql_params)
                    rows = cur.fetchall()

                    results = []
                    for row in rows:
                        # Combine document metadata fields into a single object
                        doc_metadata = {
                            "source_uri": row["source_uri"],
                            "title": row["title"],
                            "authors": row["authors"],
                            "publication_date": str(row["publication_date"]) if row["publication_date"] else None,
                            # Add fields from the 'metadata_jsonb' column
                            **(row["metadata_jsonb"] if row["metadata_jsonb"] else {})
                        }
                        results.append({
                            "chunk_id": row["chunk_id"],
                            "document_id": row["document_id"],
                            "chunk_text": row["chunk_text"],
                            "score": row["score"],
                            "metadata": doc_metadata,
                        })

                    logger.info(f"Found {len(results)} similar chunks for query.")
                    return {"success": True, "results": results}
            except McpError as e: # Catch errors raised by _get_cursor or validation
                return {"success": False, "error": e.message}
            # No need for broad Exception catch here, _get_cursor handles it


        @McpToolHandler(
            name="get_document_metadata",
            description="Retrieves metadata for a specific document by its ID.",
            input_schema={
                "type": "object",
                "properties": {
                    "doc_id": {"type": "integer", "description": "The ID of the document to retrieve metadata for."},
                },
                "required": ["doc_id"],
            },
            output_schema={
                "type": "object",
                "properties": {
                    "success": {"type": "boolean"},
                    "metadata": {"type": ["object", "null"], "description": "The document's metadata if found, otherwise null."},
                    "error": {"type": "string", "description": "Error message if the operation failed."},
                },
                "required": ["success"],
            },
        )
        async def get_document_metadata(self, context: McpToolContext, params: Dict[str, Any]) -> Dict[str, Any]:
            """Handles the get_document_metadata tool request."""
            doc_id = params.get("doc_id")

            sql = """
                SELECT
                    doc_id,
                    source_uri,
                    title,
                    authors,
                    publication_date,
                    metadata_jsonb,
                    last_processed_at
                FROM documents
                WHERE doc_id = %s;
            """
            try:
                 # Use context manager for cursor (no commit needed for SELECT)
                with self._get_cursor() as cur:
                    cur.execute(sql, (doc_id,))
                    row = cur.fetchone()

                    if row:
                        metadata = {
                            "doc_id": row["doc_id"],
                            "source_uri": row["source_uri"],
                            "title": row["title"],
                            "authors": row["authors"],
                            "publication_date": str(row["publication_date"]) if row["publication_date"] else None,
                            "last_processed_at": str(row["last_processed_at"]) if row["last_processed_at"] else None,
                            **(row["metadata_jsonb"] if row["metadata_jsonb"] else {})
                        }
                        logger.info(f"Retrieved metadata for doc_id: {doc_id}")
                        return {"success": True, "metadata": metadata}
                    else:
                        logger.warning(f"Metadata not found for doc_id: {doc_id}")
                        return {"success": False, "metadata": None, "error": f"Document with doc_id {doc_id} not found."}
            except McpError as e: # Catch errors raised by _get_cursor
                return {"success": False, "metadata": None, "error": e.message}
            # No need for broad Exception catch here, _get_cursor handles it

        async def start(self):
            """Starts the MCP server listening on the transport."""
            if not self.db_conn or self.db_conn.closed != 0:
                 logger.error("Cannot start server, database connection is not established.")
                 return # Prevent starting if initial connection failed

            transport = StdioServerTransport()
            logger.info('DB MCP Server starting to listen on stdio...')
            # Setup graceful shutdown
            # Note: Signal handling might be tricky depending on how RooCode manages the process
            # Relying on RooCode sending close/disconnect might be more robust
            transport.on_close = self.shutdown
            await self.listen(transport)
            logger.info('DB MCP Server listening.')

        async def shutdown(self):
            """Gracefully shuts down the server and database connection."""
            logger.info("Shutting down DB MCP server...")
            if self.db_conn and self.db_conn.closed == 0:
                self.db_conn.close()
                logger.info("Database connection closed.")
            await super().close() # Close MCP server itself
            logger.info("DB MCP Server shut down complete.")


# --- Entry Point ---
if __name__ == "__main__":
    if not MCP_SDK_AVAILABLE:
        sys.exit("MCP SDK not available. Cannot start server.")

    try:
        server_instance = DbMcpServer()
        # Use asyncio.run() if the SDK's listen is async, otherwise just call start()
        # Assuming listen is async based on typical patterns
        import asyncio
        asyncio.run(server_instance.start())
    except McpError as e:
        # Catch connection errors during init
        logger.critical(f"Failed to initialize DbMcpServer: {e.message}")
        sys.exit(f"Server Initialization Failed: {e.message}")
    except Exception as e:
        logger.critical(f"An unexpected error occurred during server startup: {e}", exc_info=True)
        sys.exit(f"Unexpected Startup Error: {e}")

else:
     # Log if not run as main, although typically MCP servers are run directly
     logger.debug("DB MCP Server script loaded as a module, not starting automatically.")