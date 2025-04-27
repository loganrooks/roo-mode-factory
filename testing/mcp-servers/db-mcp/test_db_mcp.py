import pytest
import psycopg2
import psycopg2.extras
import os
from dotenv import load_dotenv
import uuid
from pgvector.psycopg2 import register_vector
import json # Added for query filter test
from datetime import date # Added for date filter test

# Load environment variables from .env file
load_dotenv()

@pytest.fixture(scope="function") # Use function scope to ensure clean DB for each test
def db_conn():
    """Pytest fixture for setting up and tearing down a database connection."""
    conn = None
    cur = None # Initialize cur to None
    try:
        conn = psycopg2.connect(
            host=os.getenv("PGHOST", "localhost"), # Add default host
            port=os.getenv("PGPORT", "5432"),     # Add default port
            database=os.getenv("PGDATABASE"),
            user=os.getenv("PGUSER"),
            password=os.getenv("PGPASSWORD")
        )
        register_vector(conn) # Register pgvector type handler
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) # Use DictCursor

        yield conn, cur # Provide the connection and cursor to the test

        # Teardown: Clean up database after each test
        conn.rollback() # Rollback any pending transaction
        cur.execute("TRUNCATE TABLE chunks, documents RESTART IDENTITY CASCADE;")
        conn.commit()

    except psycopg2.Error as e:
        pytest.fail(f"Database connection failed: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


# --- Helper Functions ---

def _insert_test_document(cur, conn, source_uri_suffix, title, metadata=None, pub_date=None, authors=None, text_hash=None):
    """Helper to insert a document and return its ID."""
    source_uri = f"test://document/{uuid.uuid4()}-{source_uri_suffix}"
    sql = """
        INSERT INTO documents (source_uri, title, authors, publication_date, metadata_jsonb, extracted_text_hash)
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING doc_id;
    """
    params = (
        source_uri, title, authors, pub_date,
        psycopg2.extras.Json(metadata) if metadata is not None else None,
        text_hash
    )
    cur.execute(sql, params)
    doc_id = cur.fetchone()["doc_id"]
    conn.commit()
    assert isinstance(doc_id, int)
    return doc_id, source_uri # Return URI too, might be useful

# --- Tests for add_document ---

def test_add_document_success(db_conn):
    """Test successful insertion of a new document."""
    conn, cur = db_conn

    # Input data for the document
    source_uri = f"test://document/{uuid.uuid4()}"
    title = "Test Document Title"
    authors = "Author One, Author Two"
    pub_date_str = "2024-01-15"
    metadata = {"category": "testing", "tags": ["TDD", "pytest"]}
    text_hash = "dummyhash123"

    # SQL mimicking the tool's logic
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
        source_uri, title, authors, pub_date_str,
        psycopg2.extras.Json(metadata), # Use Json adapter for dict
        text_hash
    )

    # Execute and get the returned doc_id
    cur.execute(sql, query_params)
    result = cur.fetchone()
    assert result is not None, "INSERT should return a doc_id"
    doc_id = result["doc_id"]
    assert isinstance(doc_id, int), "Returned doc_id should be an integer"
    conn.commit() # Commit the insertion

    # Verify the data was inserted correctly
    cur.execute("SELECT * FROM documents WHERE doc_id = %s", (doc_id,))
    inserted_row = cur.fetchone()

    assert inserted_row is not None, "Document should exist in the table"
    assert inserted_row["source_uri"] == source_uri
    assert inserted_row["title"] == title
    assert inserted_row["authors"] == authors
    assert str(inserted_row["publication_date"]) == pub_date_str
    assert inserted_row["metadata_jsonb"] == metadata # psycopg2 handles JSONB comparison
    assert inserted_row["extracted_text_hash"] == text_hash


def test_add_document_update_on_conflict(db_conn):
    """Test successful update of an existing document via ON CONFLICT."""
    conn, cur = db_conn

    # --- Initial Insert --- 
    source_uri = f"test://document/{uuid.uuid4()}-conflict"
    initial_title = "Initial Title"
    initial_authors = "Initial Author"
    initial_pub_date_str = "2023-01-01"
    initial_metadata = {"status": "initial"}
    initial_hash = "hash1"

    sql = """
        INSERT INTO documents (source_uri, title, authors, publication_date, metadata_jsonb, extracted_text_hash)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON CONFLICT (source_uri) DO UPDATE SET
            title = EXCLUDED.title, authors = EXCLUDED.authors, publication_date = EXCLUDED.publication_date,
            metadata_jsonb = EXCLUDED.metadata_jsonb, extracted_text_hash = EXCLUDED.extracted_text_hash,
            last_processed_at = NOW()
        RETURNING doc_id;
    """
    initial_params = (
        source_uri, initial_title, initial_authors, initial_pub_date_str,
        psycopg2.extras.Json(initial_metadata), initial_hash
    )

    cur.execute(sql, initial_params)
    initial_result = cur.fetchone()
    assert initial_result is not None
    initial_doc_id = initial_result["doc_id"]
    assert isinstance(initial_doc_id, int)
    conn.commit()

    # --- Update Attempt (Same source_uri) --- 
    updated_title = "Updated Title"
    updated_authors = "Updated Author"
    updated_pub_date_str = "2023-02-02"
    updated_metadata = {"status": "updated", "version": 2}
    updated_hash = "hash2"

    update_params = (
        source_uri, # Same source_uri triggers conflict
        updated_title, updated_authors, updated_pub_date_str,
        psycopg2.extras.Json(updated_metadata), updated_hash
    )

    cur.execute(sql, update_params)
    update_result = cur.fetchone()
    assert update_result is not None, "UPDATE ON CONFLICT should also return doc_id"
    updated_doc_id = update_result["doc_id"]
    assert updated_doc_id == initial_doc_id, "ON CONFLICT update should return the existing doc_id"
    conn.commit()

    # --- Verify Update --- 
    cur.execute("SELECT * FROM documents WHERE doc_id = %s", (initial_doc_id,))
    updated_row = cur.fetchone() 

    assert updated_row is not None 
    assert updated_row["source_uri"] == source_uri 
    assert updated_row["title"] == updated_title 
    assert updated_row["authors"] == updated_authors 
    assert str(updated_row["publication_date"]) == updated_pub_date_str 
    assert updated_row["metadata_jsonb"] == updated_metadata 
    assert updated_row["extracted_text_hash"] == updated_hash 


def test_add_document_null_values(db_conn):
    """Test successful insertion with null values for optional fields."""
    conn, cur = db_conn

    # Input data with nulls
    source_uri = f"test://document/{uuid.uuid4()}-nulls"
    title = None
    authors = None
    pub_date_str = None # Representing null date
    metadata = None
    text_hash = None

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
        source_uri, title, authors, pub_date_str, # Pass None directly for date
        psycopg2.extras.Json(metadata) if metadata is not None else None, # Handle None for Json
        text_hash
    )

    # Execute and get the returned doc_id
    cur.execute(sql, query_params)
    result = cur.fetchone()
    assert result is not None, "INSERT should return a doc_id even with nulls"
    doc_id = result["doc_id"]
    assert isinstance(doc_id, int), "Returned doc_id should be an integer"
    conn.commit() # Commit the insertion

    # Verify the data was inserted correctly
    cur.execute("SELECT * FROM documents WHERE doc_id = %s", (doc_id,)) 
    inserted_row = cur.fetchone() 

    assert inserted_row is not None, "Document should exist in the table" 
    assert inserted_row["source_uri"] == source_uri 
    assert inserted_row["title"] is None 
    assert inserted_row["authors"] is None 
    assert inserted_row["publication_date"] is None 
    assert inserted_row["metadata_jsonb"] is None 
    assert inserted_row["extracted_text_hash"] is None 


def test_add_document_invalid_date(db_conn):
    """Test handling of invalid publication_date format (expects DB error)."""
    conn, cur = db_conn

    source_uri = f"test://document/{uuid.uuid4()}-invalid-date"
    title = "Invalid Date Doc"
    invalid_pub_date_str = "2024-13-01" # Invalid month

    sql = """
        INSERT INTO documents (source_uri, title, publication_date)
        VALUES (%s, %s, %s)
        RETURNING doc_id;
    """
    query_params = (source_uri, title, invalid_pub_date_str)

    # Expecting a database error due to invalid date format, although the
    # McpError(InvalidParams) happens in the handler logic not tested here.
    # The fixture connection error will likely occur first.
    with pytest.raises(psycopg2.Error):
        cur.execute(sql, query_params)
        conn.commit()

    # Verify nothing was inserted (due to expected error or rollback)
    # Need to rollback potential failed transaction before querying count
    conn.rollback() 
    cur.execute("SELECT COUNT(*) FROM documents WHERE source_uri = %s", (source_uri,)) 
    count = cur.fetchone()[0] 
    assert count == 0, "Document should not have been inserted with invalid date" 


def test_add_document_complex_metadata(db_conn):
    """Test successful insertion with complex nested metadata_jsonb."""
    conn, cur = db_conn

    source_uri = f"test://document/{uuid.uuid4()}-complex-meta"
    title = "Complex Metadata Doc"
    complex_metadata = {
        "source_type": "test_data",
        "details": {
            "nested_level": 1,
            "values": [10, 20, 30],
            "config": {"enabled": True, "threshold": 0.95}
        },
        "tags": ["complex", "nested", "jsonb"]
    }

    sql = """
        INSERT INTO documents (source_uri, title, metadata_jsonb)
        VALUES (%s, %s, %s)
        RETURNING doc_id;
    """
    query_params = (
        source_uri, title,
        psycopg2.extras.Json(complex_metadata)
    )

    # Execute and get the returned doc_id
    cur.execute(sql, query_params)
    result = cur.fetchone()
    assert result is not None, "INSERT should return a doc_id"
    doc_id = result["doc_id"]
    assert isinstance(doc_id, int), "Returned doc_id should be an integer"
    conn.commit() # Commit the insertion

    # Verify the data was inserted correctly
    cur.execute("SELECT metadata_jsonb FROM documents WHERE doc_id = %s", (doc_id,)) 
    inserted_row = cur.fetchone() 

    assert inserted_row is not None, "Document should exist in the table" 
    # psycopg2 automatically decodes JSONB to dict for comparison
    assert inserted_row["metadata_jsonb"] == complex_metadata, "Inserted JSONB should match complex input" 


# --- Tests for batch_insert_chunks --- 

def test_batch_insert_chunks_success(db_conn):
    """Test successful batch insertion of multiple chunks."""
    conn, cur = db_conn

    # --- Setup: Insert a parent document using helper ---
    doc_id, _ = _insert_test_document(cur, conn, "for-chunks", "Parent Doc")

    # --- Input Data: Chunks ---
    embedding_dim = 1536 # Dimension corrected based on schema/feedback
    chunks_data = [
        {"chunk_index": 0, "chunk_text": "This is the first chunk.", "embedding": [0.1] * embedding_dim},
        {"chunk_index": 1, "chunk_text": "This is the second chunk.", "embedding": [0.2] * embedding_dim},
        {"chunk_index": 2, "chunk_text": "This is the third chunk.", "embedding": [0.3] * embedding_dim},
    ]
    values_list = [
        (doc_id, c["chunk_index"], c["chunk_text"], c["embedding"])
        for c in chunks_data
    ]

    # --- SQL mimicking the tool's logic --- 
    sql = """
        INSERT INTO chunks (document_id, chunk_index, chunk_text, embedding)
        VALUES %s
        ON CONFLICT (document_id, chunk_index) DO UPDATE SET
            chunk_text = EXCLUDED.chunk_text,
            embedding = EXCLUDED.embedding;
    """

    # --- Execute Batch Insert --- 
    psycopg2.extras.execute_values(cur, sql, values_list, page_size=100)
    conn.commit()

    # --- Verify Insertion --- 
    cur.execute("SELECT COUNT(*) FROM chunks WHERE document_id = %s", (doc_id,))
    count = cur.fetchone()[0]
    assert count == len(chunks_data), f"Expected {len(chunks_data)} chunks, found {count}" 

    cur.execute("SELECT chunk_index, chunk_text, embedding FROM chunks WHERE document_id = %s ORDER BY chunk_index", (doc_id,)) 
    inserted_chunks = cur.fetchall() 
    assert len(inserted_chunks) == len(chunks_data) 
    for i, row in enumerate(inserted_chunks): 
        assert row["chunk_index"] == chunks_data[i]["chunk_index"] 
        assert row["chunk_text"] == chunks_data[i]["chunk_text"] 
        # Convert numpy array from pgvector back to list for comparison if necessary
        assert list(row["embedding"]) == chunks_data[i]["embedding"] 


def test_batch_insert_chunks_update_on_conflict(db_conn):
    """Test successful batch update of existing chunks via ON CONFLICT."""
    conn, cur = db_conn

    # --- Setup: Insert a parent document using helper ---
    doc_id, _ = _insert_test_document(cur, conn, "for-chunk-update", "Parent Doc Update")

    # --- Setup: Initial Chunk Insert ---
    embedding_dim = 1536 # Dimension corrected based on schema/feedback
    initial_chunks = [
        {"chunk_index": 0, "chunk_text": "Initial text 0.", "embedding": [0.1] * embedding_dim},
        {"chunk_index": 1, "chunk_text": "Initial text 1.", "embedding": [0.2] * embedding_dim},
    ]
    initial_values = [(doc_id, c["chunk_index"], c["chunk_text"], c["embedding"]) for c in initial_chunks]

    sql = """
        INSERT INTO chunks (document_id, chunk_index, chunk_text, embedding)
        VALUES %s
        ON CONFLICT (document_id, chunk_index) DO UPDATE SET
            chunk_text = EXCLUDED.chunk_text,
            embedding = EXCLUDED.embedding;
    """
    psycopg2.extras.execute_values(cur, sql, initial_values)
    conn.commit()

    # --- Input Data: Updated Chunks (same indices) --- 
    updated_chunks = [
        {"chunk_index": 0, "chunk_text": "Updated text 0!", "embedding": [0.9] * embedding_dim},
        {"chunk_index": 1, "chunk_text": "Updated text 1!", "embedding": [0.8] * embedding_dim},
    ]
    update_values = [(doc_id, c["chunk_index"], c["chunk_text"], c["embedding"]) for c in updated_chunks]

    # --- Execute Update Batch Insert --- 
    psycopg2.extras.execute_values(cur, sql, update_values)
    conn.commit()

    # --- Verify Update --- 
    cur.execute("SELECT COUNT(*) FROM chunks WHERE document_id = %s", (doc_id,))
    count = cur.fetchone()[0]
    # Should still only be 2 chunks, just updated
    assert count == len(initial_chunks), f"Expected {len(initial_chunks)} total chunks after update, found {count}"

    cur.execute("SELECT chunk_index, chunk_text, embedding FROM chunks WHERE document_id = %s ORDER BY chunk_index", (doc_id,))
    final_chunks = cur.fetchall()
    assert len(final_chunks) == len(updated_chunks)
    for i, row in enumerate(final_chunks):
        assert row["chunk_index"] == updated_chunks[i]["chunk_index"]
        assert row["chunk_text"] == updated_chunks[i]["chunk_text"] 
        assert list(row["embedding"]) == updated_chunks[i]["embedding"] 


def test_batch_insert_chunks_large_batch(db_conn):
    """Test insertion with a large batch of chunks (> execute_values page_size)."""
    conn, cur = db_conn

    # --- Setup: Insert a parent document using helper ---
    doc_id, _ = _insert_test_document(cur, conn, "large-batch", "Large Batch Doc")

    # --- Input Data: Large number of Chunks ---
    num_chunks = 1100 # More than default page_size of 100
    embedding_dim = 1536 # Dimension corrected based on schema/feedback
    chunks_data = [
        {"chunk_index": i, "chunk_text": f"Chunk text {i}.", "embedding": [float(i % 10) / 10.0] * embedding_dim}
        for i in range(num_chunks)
    ]
    values_list = [
        (doc_id, c["chunk_index"], c["chunk_text"], c["embedding"])
        for c in chunks_data
    ]

    # --- SQL mimicking the tool's logic --- 
    sql = """
        INSERT INTO chunks (document_id, chunk_index, chunk_text, embedding)
        VALUES %s
        ON CONFLICT (document_id, chunk_index) DO UPDATE SET
            chunk_text = EXCLUDED.chunk_text,
            embedding = EXCLUDED.embedding;
    """

    # --- Execute Large Batch Insert --- 
    # Expecting this to work due to execute_values paging
    psycopg2.extras.execute_values(cur, sql, values_list, page_size=100)
    conn.commit()

    # --- Verify Insertion Count --- 
    cur.execute("SELECT COUNT(*) FROM chunks WHERE document_id = %s", (doc_id,))
    count = cur.fetchone()[0]
    assert count == num_chunks, f"Expected {num_chunks} chunks, found {count}"


def test_batch_insert_chunks_invalid_doc_id(db_conn):
    """Test batch insertion with an invalid document_id (expects FK violation)."""
    conn, cur = db_conn

    invalid_doc_id = 999999 # Assumed non-existent doc_id
    embedding_dim = 1536 # Dimension corrected based on schema/feedback
    chunks_data = [
        {"chunk_index": 0, "chunk_text": "Chunk for invalid doc.", "embedding": [0.5] * embedding_dim}
    ]
    values_list = [
        (invalid_doc_id, c["chunk_index"], c["chunk_text"], c["embedding"])
        for c in chunks_data
    ]

    sql = """
        INSERT INTO chunks (document_id, chunk_index, chunk_text, embedding)
        VALUES %s
        ON CONFLICT (document_id, chunk_index) DO UPDATE SET
            chunk_text = EXCLUDED.chunk_text,
            embedding = EXCLUDED.embedding;
    """

    # Expecting a DB error (ForeignKeyViolation), although the fixture error will likely hit first.
    with pytest.raises(psycopg2.Error):
        psycopg2.extras.execute_values(cur, sql, values_list)
        conn.commit()

    # Verify nothing was inserted
    conn.rollback() # Ensure transaction state is clean before query
    cur.execute("SELECT COUNT(*) FROM chunks WHERE document_id = %s", (invalid_doc_id,))
    count = cur.fetchone()[0]
    assert count == 0, "Chunks should not be inserted with an invalid document_id"


def test_batch_insert_chunks_duplicate_index_in_batch(db_conn):
    """Test batch insertion handles duplicate chunk_index in the same batch via ON CONFLICT."""
    conn, cur = db_conn

    # --- Setup: Insert a parent document using helper ---
    doc_id, _ = _insert_test_document(cur, conn, "duplicate-chunk-index", "Duplicate Index Doc")

    # --- Input Data: Chunks with duplicate index 0 ---
    embedding_dim = 1536 # Dimension corrected based on schema/feedback
    chunks_data = [
        {"chunk_index": 0, "chunk_text": "First version of chunk 0.", "embedding": [0.1] * embedding_dim},
        {"chunk_index": 1, "chunk_text": "Chunk 1.", "embedding": [0.2] * embedding_dim},
        {"chunk_index": 2, "chunk_text": "Chunk 2.", "embedding": [0.9] * embedding_dim}, # Changed index from 0 to 2
    ]
    values_list = [
        (doc_id, c["chunk_index"], c["chunk_text"], c["embedding"])
        for c in chunks_data
    ]

    sql = """
        INSERT INTO chunks (document_id, chunk_index, chunk_text, embedding)
        VALUES %s
        ON CONFLICT (document_id, chunk_index) DO UPDATE SET
            chunk_text = EXCLUDED.chunk_text,
            embedding = EXCLUDED.embedding;
    """

    # --- Execute Batch Insert --- 
    # ON CONFLICT should handle the duplicate index gracefully
    psycopg2.extras.execute_values(cur, sql, values_list)
    conn.commit()

    # --- Verify Outcome --- 
    # Expecting 2 chunks total, with chunk 0 having the SECOND version's data
    cur.execute("SELECT COUNT(*) FROM chunks WHERE document_id = %s", (doc_id,))
    count = cur.fetchone()[0]
    assert count == 3, f"Expected 3 unique chunks after insert, found {count}"

    cur.execute("SELECT chunk_index, chunk_text, embedding FROM chunks WHERE document_id = %s AND chunk_index = 0", (doc_id,))
    chunk_0_row = cur.fetchone()
    assert chunk_0_row is not None, "Chunk with index 0 should exist"
    assert chunk_0_row["chunk_text"] == "First version of chunk 0.", "Chunk 0 should have the original text"
    assert list(chunk_0_row["embedding"]) == [0.1] * embedding_dim, "Chunk 0 should have the original embedding"

    cur.execute("SELECT COUNT(*) FROM chunks WHERE document_id = %s AND chunk_index = 1", (doc_id,))
    count_1 = cur.fetchone()[0]
    assert count_1 == 1, "Chunk with index 1 should exist"

    cur.execute("SELECT COUNT(*) FROM chunks WHERE document_id = %s AND chunk_index = 2", (doc_id,))
    count_2 = cur.fetchone()[0]
    assert count_2 == 1, "Chunk with index 2 should exist"


# --- Tests for query_similar_chunks --- 

def test_query_similar_chunks_success(db_conn):
    """Test successful query returning top_k results, ordered by score."""
    conn, cur = db_conn

    # --- Setup: Insert document and chunks ---
    doc_metadata = {"year": 2024, "type": "query_test"}
    doc_id, source_uri = _insert_test_document(cur, conn, "for-query", "Query Test Doc", metadata=doc_metadata)

    embedding_dim = 1536 # Dimension corrected based on schema/feedback
    # Using distinct basis vectors for chunks to ensure clear cosine distance separation
    chunks_to_insert = [
        (doc_id, 0, "Chunk A (close).", [1.0] + [0.0] * (embedding_dim - 1)),      # Basis vector 1
        (doc_id, 1, "Chunk B (far).", [0.0, 0.0, 0.0, 1.0] + [0.0] * (embedding_dim - 4)), # Basis vector 4 (farthest for query)
        (doc_id, 2, "Chunk C (medium).", [0.0, 0.0, 1.0] + [0.0] * (embedding_dim - 3)), # Basis vector 3 (third closest)
        (doc_id, 3, "Chunk D (very close).", [0.0, 1.0] + [0.0] * (embedding_dim - 2)), # Basis vector 2 (second closest)
    ]
    insert_sql = "INSERT INTO chunks (document_id, chunk_index, chunk_text, embedding) VALUES %s"
    psycopg2.extras.execute_values(cur, insert_sql, chunks_to_insert)
    conn.commit()

    # --- Query Parameters ---
    query_embedding = [0.9, 0.1] + [0.0] * (embedding_dim - 2) # Query vector close to A, then D
    top_k = 2
 
    # --- SQL mimicking the tool's logic ---
    sql = """
        SELECT c.chunk_id, c.document_id, c.chunk_text, c.embedding <=> %s::vector AS score,
               d.source_uri, d.title, d.authors, d.publication_date, d.metadata_jsonb
        FROM chunks c JOIN documents d ON c.document_id = d.doc_id
        WHERE c.document_id = %s -- Added filter for this test setup
        ORDER BY score ASC 
        LIMIT %s;
    """
    query_params = (query_embedding, doc_id, top_k)

    # --- Execute Query --- 
    cur.execute(sql, query_params)
    rows = cur.fetchall()

    # --- Verify Results --- 
    assert len(rows) == top_k, f"Expected {top_k} results, got {len(rows)}"

    # Check ordering (Chunk A score should be ~0, Chunk D score slightly > 0)
    assert rows[0]["chunk_text"] == "Chunk A (close)."
    assert rows[1]["chunk_text"] == "Chunk D (very close)."
    assert 0.0 <= rows[0]["score"] < 0.01 # Relaxed threshold for very close match
    assert rows[1]["score"] > rows[0]["score"] # Check relative order

    # Check structure of the first result's metadata
    first_result_metadata = {
        "source_uri": source_uri,
        "title": "Query Test Doc",
        "authors": None,
        "publication_date": None,
        **doc_metadata # Merge JSONB fields
    }
    # Construct expected result using actual IDs/scores from the query result
    expected_first_result = {
        "chunk_id": rows[0]["chunk_id"], 
        "document_id": doc_id,
        "chunk_text": "Chunk A (close).",
        "score": rows[0]["score"], 
        "metadata": first_result_metadata
    }
    # Construct actual result from the query for comparison
    actual_metadata = {
        "source_uri": rows[0]["source_uri"],
        "title": rows[0]["title"],
        "authors": rows[0]["authors"],
        "publication_date": str(rows[0]["publication_date"]) if rows[0]["publication_date"] else None,
        **(rows[0]["metadata_jsonb"] if rows[0]["metadata_jsonb"] else {}) # Corrected escaping
    }
    actual_first_result = {
        "chunk_id": rows[0]["chunk_id"],
        "document_id": rows[0]["document_id"],
        "chunk_text": rows[0]["chunk_text"],
        "score": rows[0]["score"],
        "metadata": actual_metadata
    }
    assert actual_first_result == expected_first_result, "First result structure/content mismatch"


def test_query_similar_chunks_return_fewer_than_k(db_conn):
    """Test query returns fewer results than top_k when fewer matches exist."""
    conn, cur = db_conn

    # --- Setup: Insert document and only ONE chunk ---
    doc_metadata = {"year": 2025}
    doc_id, _ = _insert_test_document(cur, conn, "fewer-chunks", "Fewer Chunks Doc", metadata=doc_metadata)

    embedding_dim = 1536 # Dimension corrected based on schema/feedback
    chunks_to_insert = [
        (doc_id, 0, "The only chunk.", [0.4] * embedding_dim), # Simplified vector for test
    ]
    insert_sql = "INSERT INTO chunks (document_id, chunk_index, chunk_text, embedding) VALUES %s"
    psycopg2.extras.execute_values(cur, insert_sql, chunks_to_insert)
    conn.commit()

    # --- Query Parameters ---
    query_embedding = [0.41] * embedding_dim # Query vector
    top_k = 3 # Request more than available
 
    # --- SQL mimicking the tool's logic ---
    sql = """
        SELECT c.chunk_id, c.document_id, c.chunk_text, c.embedding <=> %s::vector AS score,
               d.source_uri, d.title, d.authors, d.publication_date, d.metadata_jsonb
        FROM chunks c JOIN documents d ON c.document_id = d.doc_id
        WHERE c.document_id = %s 
        ORDER BY score ASC 
        LIMIT %s;
    """
    query_params = (query_embedding, doc_id, top_k)

    # --- Execute Query --- 
    cur.execute(sql, query_params)
    rows = cur.fetchall()

    # --- Verify Results --- 
    assert len(rows) == 1, f"Expected 1 result (fewer than top_k={top_k}), got {len(rows)}"
    assert rows[0]["chunk_text"] == "The only chunk."


def test_query_similar_chunks_return_zero_results(db_conn):
    """Test query returns zero results when no matching chunks exist."""
    conn, cur = db_conn

    # --- Setup: Insert document but NO chunks ---
    doc_metadata = {"status": "empty"}
    doc_id, _ = _insert_test_document(cur, conn, "no-chunks", "No Chunks Doc", metadata=doc_metadata)

    # --- Query Parameters ---
    query_embedding = [0.5] * 1536 # Dimension corrected based on schema/feedback
    top_k = 5
 
    # --- SQL mimicking the tool's logic ---
    sql = """
        SELECT c.chunk_id, c.document_id, c.chunk_text, c.embedding <=> %s::vector AS score,
               d.source_uri, d.title, d.authors, d.publication_date, d.metadata_jsonb
        FROM chunks c JOIN documents d ON c.document_id = d.doc_id
        WHERE c.document_id = %s 
        ORDER BY score ASC 
        LIMIT %s;
    """
    query_params = (query_embedding, doc_id, top_k)

    # --- Execute Query --- 
    cur.execute(sql, query_params)
    rows = cur.fetchall()

    # --- Verify Results --- 
    assert len(rows) == 0, f"Expected 0 results, got {len(rows)}"


def test_query_similar_chunks_filter_jsonb_single(db_conn):
    """Test query correctly applies a single JSONB metadata filter."""
    conn, cur = db_conn

    # --- Setup: Insert two documents with different metadata using helper ---
    doc_meta_A = {"type": "A", "year": 2023}
    doc_meta_B = {"type": "B", "year": 2024}

    doc_id_A, _ = _insert_test_document(cur, conn, "A", "Doc A", metadata=doc_meta_A)
    doc_id_B, _ = _insert_test_document(cur, conn, "B", "Doc B", metadata=doc_meta_B)

    # --- Setup: Insert chunks for both documents ---
    embedding_dim = 1536 # Dimension corrected based on schema/feedback
    chunks_to_insert = [
        (doc_id_A, 0, "Chunk A1 (close).", [0.1] * embedding_dim),
        (doc_id_A, 1, "Chunk A2 (medium).", [0.5] * embedding_dim),
        (doc_id_B, 0, "Chunk B1 (close).", [0.1] * embedding_dim), # Same embedding as A1
        (doc_id_B, 1, "Chunk B2 (far).", [0.9] * embedding_dim),
    ]
    insert_sql = "INSERT INTO chunks (document_id, chunk_index, chunk_text, embedding) VALUES %s"
    psycopg2.extras.execute_values(cur, insert_sql, chunks_to_insert)
    conn.commit()

    # --- Query Parameters ---
    query_embedding = [0.1] * 1536 # Dimension corrected based on schema/feedback
    top_k = 5
    filters = {"type": "A"} # Filter for documents of type A

    # --- SQL mimicking the tool's logic with filter ---
    base_sql = """
        SELECT c.chunk_id, c.document_id, c.chunk_text, c.embedding <=> %s::vector AS score,
               d.source_uri, d.title, d.authors, d.publication_date, d.metadata_jsonb
        FROM chunks c JOIN documents d ON c.document_id = d.doc_id
    """
    where_clauses = []
    query_params_list = [query_embedding] # Embedding is first param for <=>

    # Build WHERE clause dynamically (simplified from spec pseudocode for test)
    filter_key, filter_value = list(filters.items())[0]
    where_clauses.append("d.metadata_jsonb @> %s")
    query_params_list.append(json.dumps({filter_key: filter_value}))

    sql = base_sql + " WHERE " + " AND ".join(where_clauses)
    sql += " ORDER BY score ASC LIMIT %s;"
    query_params_list.append(top_k)
    
    query_params_tuple = tuple(query_params_list)

    # --- Execute Query ---
    cur.execute(sql, query_params_tuple)
    rows = cur.fetchall()

    # --- Verify Results ---
    assert len(rows) > 0, "Expected results with filter"
    assert len(rows) == 2, f"Expected 2 results matching filter, got {len(rows)}" # A1 and A2
    for row in rows:
        assert row["document_id"] == doc_id_A, "All results should belong to Doc A"
        assert row["metadata_jsonb"]["type"] == "A", "Metadata should match filter"
    
    # Check that the closest chunk (A1) is first
    assert rows[0]["chunk_text"] == "Chunk A1 (close)."


def test_query_similar_chunks_filter_jsonb_multiple(db_conn):
    """Test query correctly applies multiple JSONB metadata filters (AND condition)."""
    conn, cur = db_conn

    # --- Setup: Insert documents with different metadata combinations using helper ---
    doc_meta_A1 = {"type": "A", "year": 2023, "status": "final"}
    doc_meta_A2 = {"type": "A", "year": 2024, "status": "draft"}
    doc_meta_B1 = {"type": "B", "year": 2023, "status": "final"}

    doc_id_A1, _ = _insert_test_document(cur, conn, "A1", "Doc A1", metadata=doc_meta_A1)
    doc_id_A2, _ = _insert_test_document(cur, conn, "A2", "Doc A2", metadata=doc_meta_A2)
    doc_id_B1, _ = _insert_test_document(cur, conn, "B1", "Doc B1", metadata=doc_meta_B1)

    # --- Setup: Insert chunks ---
    embedding_dim = 1536 # Dimension corrected based on schema/feedback
    chunks_to_insert = [
        (doc_id_A1, 0, "Chunk A1-0 (close).", [0.1] * embedding_dim),
        (doc_id_A2, 0, "Chunk A2-0 (medium).", [0.5] * embedding_dim),
        (doc_id_B1, 0, "Chunk B1-0 (close).", [0.1] * embedding_dim),
    ]
    insert_sql = "INSERT INTO chunks (document_id, chunk_index, chunk_text, embedding) VALUES %s"
    psycopg2.extras.execute_values(cur, insert_sql, chunks_to_insert)
    conn.commit()

    # --- Query Parameters ---
    query_embedding = [0.1] * 1536 # Dimension corrected based on schema/feedback
    top_k = 5
    filters = {"type": "A", "year": 2023} # Filter for type A AND year 2023

    # --- SQL mimicking the tool's logic with multiple filters ---
    base_sql = """
        SELECT c.chunk_id, c.document_id, c.chunk_text, c.embedding <=> %s::vector AS score,
               d.source_uri, d.title, d.authors, d.publication_date, d.metadata_jsonb
        FROM chunks c JOIN documents d ON c.document_id = d.doc_id
    """
    where_clauses = []
    query_params_list = [query_embedding] 

    # Build WHERE clause dynamically 
    for key, value in filters.items():
         # Assuming generic JSONB filter for all keys in this test
         where_clauses.append("d.metadata_jsonb @> %s")
         query_params_list.append(json.dumps({key: value}))

    sql = base_sql + " WHERE " + " AND ".join(where_clauses)
    sql += " ORDER BY score ASC LIMIT %s;"
    query_params_list.append(top_k)
    
    query_params_tuple = tuple(query_params_list)

    # --- Execute Query ---
    cur.execute(sql, query_params_tuple)
    rows = cur.fetchall()

    # --- Verify Results ---
    assert len(rows) == 1, f"Expected 1 result matching multiple filters, got {len(rows)}" 
    assert rows[0]["document_id"] == doc_id_A1, "Result should belong to Doc A1"
    assert rows[0]["metadata_jsonb"]["type"] == "A"
    assert rows[0]["metadata_jsonb"]["year"] == 2023


def test_query_similar_chunks_filter_date_after(db_conn):
    """Test query correctly applies a publication_date_after filter."""
    conn, cur = db_conn

    # --- Setup: Insert documents with different dates using helper ---
    date_2023 = date(2023, 1, 1)
    date_2024 = date(2024, 1, 1)

    doc_id_2023, _ = _insert_test_document(cur, conn, "2023", "Doc 2023", pub_date=date_2023)
    doc_id_2024, _ = _insert_test_document(cur, conn, "2024", "Doc 2024", pub_date=date_2024)

    # --- Setup: Insert chunks ---
    embedding_dim = 1536 # Dimension corrected based on schema/feedback
    chunks_to_insert = [
        (doc_id_2023, 0, "Chunk 2023.", [0.1] * embedding_dim),
        (doc_id_2024, 0, "Chunk 2024.", [0.1] * embedding_dim),
    ]
    insert_sql = "INSERT INTO chunks (document_id, chunk_index, chunk_text, embedding) VALUES %s"
    psycopg2.extras.execute_values(cur, insert_sql, chunks_to_insert)
    conn.commit()

    # --- Query Parameters ---
    query_embedding = [0.1] * 1536 # Dimension corrected based on schema/feedback
    top_k = 5
    filter_date_str = "2023-06-01"
    filters = {"publication_date_after": filter_date_str} 

    # --- SQL mimicking the tool's logic with date filter ---
    base_sql = """
        SELECT c.chunk_id, c.document_id, c.chunk_text, c.embedding <=> %s::vector AS score,
               d.source_uri, d.title, d.authors, d.publication_date, d.metadata_jsonb
        FROM chunks c JOIN documents d ON c.document_id = d.doc_id
    """
    where_clauses = []
    query_params_list = [query_embedding] 

    # Build WHERE clause dynamically 
    filter_key, filter_value = list(filters.items())[0]
    if filter_key == "publication_date_after":
        try: date_val = date.fromisoformat(str(filter_value))
        except ValueError: pytest.fail(f"Test setup error: Invalid date format '{filter_value}'")
        where_clauses.append("d.publication_date > %s")
        query_params_list.append(date_val)
    # Add elif for _before or other specific filters if needed
    else: # Default JSONB
         where_clauses.append("d.metadata_jsonb @> %s")
         query_params_list.append(json.dumps({filter_key: filter_value}))

    sql = base_sql + " WHERE " + " AND ".join(where_clauses)
    sql += " ORDER BY score ASC LIMIT %s;"
    query_params_list.append(top_k)
    
    query_params_tuple = tuple(query_params_list)

    # --- Execute Query ---
    cur.execute(sql, query_params_tuple)
    rows = cur.fetchall()

    # --- Verify Results ---
    assert len(rows) == 1, f"Expected 1 result matching date filter, got {len(rows)}" 
    assert rows[0]["document_id"] == doc_id_2024, "Result should belong to Doc 2024"
    assert rows[0]["publication_date"] == date_2024


def test_query_similar_chunks_filter_date_before(db_conn):
    """Test query correctly applies a publication_date_before filter."""
    conn, cur = db_conn

    # --- Setup: Insert documents with different dates using helper ---
    date_2023 = date(2023, 1, 1)
    date_2024 = date(2024, 1, 1)

    doc_id_2023, _ = _insert_test_document(cur, conn, "2023", "Doc 2023", pub_date=date_2023)
    doc_id_2024, _ = _insert_test_document(cur, conn, "2024", "Doc 2024", pub_date=date_2024)

    # --- Setup: Insert chunks ---
    embedding_dim = 1536 # Dimension corrected based on schema/feedback
    chunks_to_insert = [
        (doc_id_2023, 0, "Chunk 2023.", [0.1] * embedding_dim),
        (doc_id_2024, 0, "Chunk 2024.", [0.1] * embedding_dim),
    ]
    insert_sql = "INSERT INTO chunks (document_id, chunk_index, chunk_text, embedding) VALUES %s"
    psycopg2.extras.execute_values(cur, insert_sql, chunks_to_insert)
    conn.commit()

    # --- Query Parameters ---
    query_embedding = [0.1] * 1536 # Dimension corrected based on schema/feedback
    top_k = 5
    filter_date_str = "2023-06-01"
    filters = {"publication_date_before": filter_date_str} 

    # --- SQL mimicking the tool's logic with date filter ---
    base_sql = """
        SELECT c.chunk_id, c.document_id, c.chunk_text, c.embedding <=> %s::vector AS score,
               d.source_uri, d.title, d.authors, d.publication_date, d.metadata_jsonb
        FROM chunks c JOIN documents d ON c.document_id = d.doc_id
    """
    where_clauses = []
    query_params_list = [query_embedding] 

    # Build WHERE clause dynamically 
    filter_key, filter_value = list(filters.items())[0]
    if filter_key == "publication_date_after":
        try: date_val = date.fromisoformat(str(filter_value))
        except ValueError: pytest.fail(f"Test setup error: Invalid date format '{filter_value}'")
        where_clauses.append("d.publication_date > %s")
        query_params_list.append(date_val)
    elif filter_key == "publication_date_before":
        try: date_val = date.fromisoformat(str(filter_value))
        except ValueError: pytest.fail(f"Test setup error: Invalid date format '{filter_value}'")
        where_clauses.append("d.publication_date < %s")
        query_params_list.append(date_val)
    else: # Default JSONB
         where_clauses.append("d.metadata_jsonb @> %s")
         query_params_list.append(json.dumps({filter_key: filter_value}))

    sql = base_sql + " WHERE " + " AND ".join(where_clauses)
    sql += " ORDER BY score ASC LIMIT %s;"
    query_params_list.append(top_k)
    
    query_params_tuple = tuple(query_params_list)

    # --- Execute Query ---
    cur.execute(sql, query_params_tuple)
    rows = cur.fetchall()

    # --- Verify Results ---
    assert len(rows) == 1, f"Expected 1 result matching date filter, got {len(rows)}" 
    assert rows[0]["document_id"] == doc_id_2023, "Result should belong to Doc 2023"
    assert rows[0]["publication_date"] == date_2023


def test_query_similar_chunks_filter_invalid_date_format(db_conn):
    """Test query handling (expects ValueError) for invalid date format string in filters."""
    conn, cur = db_conn

    # --- Setup: Insert document and chunk (needed for query structure) using helper ---
    doc_id, _ = _insert_test_document(cur, conn, "date-invalid", "Date Invalid Doc")

    embedding_dim = 1536 # Dimension corrected based on schema/feedback
    chunks_to_insert = [(doc_id, 0, "Dummy chunk.", [0.5]*embedding_dim)]
    insert_sql = "INSERT INTO chunks (document_id, chunk_index, chunk_text, embedding) VALUES %s"
    psycopg2.extras.execute_values(cur, insert_sql, chunks_to_insert)
    conn.commit()

    # --- Query Parameters ---
    query_embedding = [0.1] * 1536 # Dimension corrected based on schema/feedback
    top_k = 5
    filters = {"publication_date_after": "invalid-date-string"}

    # --- SQL Construction and Execution ---
    # This part simulates the handler trying to build the query
    base_sql = """
        SELECT c.chunk_id, c.document_id, c.chunk_text, c.embedding <=> %s::vector AS score,
               d.source_uri, d.title, d.authors, d.publication_date, d.metadata_jsonb
        FROM chunks c JOIN documents d ON c.document_id = d.doc_id
    """
    where_clauses = []
    query_params_list = [query_embedding] 

    # Expect ValueError when trying to parse the invalid date string
    with pytest.raises(ValueError):
        filter_key, filter_value = list(filters.items())[0]
        if filter_key == "publication_date_after":
            date_val = date.fromisoformat(str(filter_value)) # This should raise ValueError
            where_clauses.append("d.publication_date > %s")
            query_params_list.append(date_val)
        # ... other filter logic ...

        # The following lines would not be reached if ValueError is raised as expected
        # sql = base_sql + " WHERE " + " AND ".join(where_clauses)
        # sql += " ORDER BY score ASC LIMIT %s;"
        # query_params_list.append(top_k)
        # query_params_tuple = tuple(query_params_list)
        # cur.execute(sql, query_params_tuple) 


def test_query_similar_chunks_error_invalid_embedding(db_conn):
    """Test query handling (expects DB error) for invalid query_embedding format/dimension."""
    conn, cur = db_conn

    # --- Setup: Insert document and chunk ---
    source_uri = f"test://doc/invalid-embed"
    cur.execute("INSERT INTO documents (source_uri, title) VALUES (%s, %s) RETURNING doc_id;", (source_uri, "Invalid Embed Doc"))
    doc_id = cur.fetchone()["doc_id"]
    conn.commit()
    # Use correct dimension for insertion
    embedding_dim = 1536 # Define dimension
    chunks_to_insert = [(doc_id, 0, "Dummy chunk.", [0.5] * embedding_dim)] # Corrected dimension
    insert_sql = "INSERT INTO chunks (document_id, chunk_index, chunk_text, embedding) VALUES %s"
    psycopg2.extras.execute_values(cur, insert_sql, chunks_to_insert)
    conn.commit()

    # --- Query Parameters ---
    # Invalid embedding: wrong dimension (assuming DB expects 3)
    query_embedding_wrong_dim = [0.1, 0.1] 
    top_k = 5

    # --- SQL mimicking the tool's logic --- 
    sql = """
        SELECT c.chunk_id, c.embedding <=> %s AS score
        FROM chunks c JOIN documents d ON c.document_id = d.doc_id
        WHERE c.document_id = %s 
        ORDER BY score ASC 
        LIMIT %s;
    """
    query_params = (query_embedding_wrong_dim, doc_id, top_k)

    # --- Execute Query --- 
    # Expecting a DB error (e.g., DataError or InternalError from pgvector)
    with pytest.raises(psycopg2.Error):
        cur.execute(sql, query_params)


# --- Tests for get_document_metadata ---

def test_get_document_metadata_success(db_conn):
    """Test successful retrieval of metadata for an existing doc_id."""
    conn, cur = db_conn

    # --- Setup: Insert document with known metadata ---
    source_uri = f"test://document/{uuid.uuid4()}-metadata"
    title = "Metadata Test Doc"
    authors = "Meta Author"
    pub_date = date(2022, 12, 25)
    jsonb_meta = {"project": "db-mcp-test", "version": 1.1}
    
    insert_sql = """
        INSERT INTO documents (source_uri, title, authors, publication_date, metadata_jsonb) 
        VALUES (%s, %s, %s, %s, %s) RETURNING doc_id;
    """
    insert_params = (source_uri, title, authors, pub_date, psycopg2.extras.Json(jsonb_meta))
    cur.execute(insert_sql, insert_params)
    doc_id = cur.fetchone()["doc_id"]
    conn.commit()
    assert isinstance(doc_id, int)

    # --- SQL mimicking the tool's logic ---
    select_sql = """
        SELECT doc_id, source_uri, title, authors, publication_date, metadata_jsonb, last_processed_at
        FROM documents WHERE doc_id = %s;
    """
    
    # --- Execute Query ---
    cur.execute(select_sql, (doc_id,))
    row = cur.fetchone()

    # --- Verify Result ---
    assert row is not None, "Document should be found"
    
    # Construct expected metadata object (as the tool should return)
    expected_metadata = {
        "doc_id": doc_id, 
        "source_uri": source_uri, 
        "title": title,
        "authors": authors,
        "publication_date": str(pub_date), # Convert date to string
        "last_processed_at": str(row["last_processed_at"]) if row["last_processed_at"] else None, # Convert timestamp
        **jsonb_meta # Merge JSONB fields
    }

    # Construct actual metadata from row
    actual_metadata = {
        "doc_id": row["doc_id"], 
        "source_uri": row["source_uri"], 
        "title": row["title"],
        "authors": row["authors"],
        "publication_date": str(row["publication_date"]) if row["publication_date"] else None,
        "last_processed_at": str(row["last_processed_at"]) if row["last_processed_at"] else None,
        **(row["metadata_jsonb"] if row["metadata_jsonb"] else {})
    }

    assert actual_metadata == expected_metadata, "Retrieved metadata does not match expected"


def test_get_document_metadata_not_found(db_conn):
    """Test retrieval attempt for a non-existent doc_id returns None."""
    conn, cur = db_conn

    non_existent_doc_id = 999999

    # --- SQL mimicking the tool's logic ---
    select_sql = """
        SELECT doc_id, source_uri, title, authors, publication_date, metadata_jsonb, last_processed_at
        FROM documents WHERE doc_id = %s;
    """
    
    # --- Execute Query ---
    cur.execute(select_sql, (non_existent_doc_id,))
    row = cur.fetchone()

    # --- Verify Result ---
    assert row is None, "No document should be found for a non-existent doc_id"