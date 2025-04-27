# TDD Specific Memory

## Test Plans (Driving Implementation)
<!-- Append new test plans using the format below -->
### Test Plan: PhilAPI-MCP Core Tools - [2025-04-16 09:02:58]
- **Objective**: Drive implementation of `search_philpapers` and `get_philpapers_details` tools for PhilAPI-MCP server.
- **Scope**: `mcp-servers/philapi-mcp/main.py` (to be created).
- **Test Cases**:
    - `test_search_philpapers_success`: Failing / Expected: Success response structure / Status: Red
    - `test_search_philpapers_api_error_4xx`: Failing / Expected: Failure response with error / Status: Red
    - `test_search_philpapers_api_error_5xx`: Failing / Expected: Failure response with error / Status: Red
    - `test_search_philpapers_no_results`: Failing / Expected: Success response with empty results / Status: Red
    - `test_search_philpapers_with_filters`: Failing / Expected: Success response structure / Status: Red
    - `test_get_details_success`: Failing / Expected: Success response structure / Status: Red
    - `test_get_details_not_found`: Failing / Expected: Failure response with error / Status: Red
    - `test_get_details_api_error_5xx`: Failing / Expected: Failure response with error / Status: Red
- **Related Requirements**: `docs/custom_mcp_servers_spec.md#philapi-mcp-server`




## Test Coverage Summary
<!-- Update coverage summary using the format below -->

## Test Fixtures
### Fixture: `db_conn` - [%%current_timestamp%%]
- **Location**: `testing/mcp-servers/db-mcp/test_db_mcp.py`
- **Description**: Sets up a PostgreSQL connection using env vars, registers pgvector, yields (conn, cursor), truncates tables on teardown.
- **Usage**: All tests in `test_db_mcp.py`.
- **Dependencies**: `pytest`, `psycopg2`, `os`, `dotenv`, `pgvector`.


<!-- Append new fixtures using the format below -->
### Fixture: `mock_adapter` (PhilAPI) - [2025-04-16 09:02:58]
- **Location**: `testing/mcp-servers/philapi-mcp/test_philapi_mcp.py`
- **Description**: Provides a `requests_mock.Adapter` instance for mocking PhilPapers API HTTP requests.
- **Usage**: Used by `philapi_mcp_instance` fixture and within tests via `requests_mock.Mocker`.
- **Dependencies**: `requests-mock`.

### Fixture: `philapi_mcp_instance` - [2025-04-16 09:02:58]
- **Location**: `testing/mcp-servers/philapi-mcp/test_philapi_mcp.py`
- **Description**: Provides an instance of the (potentially dummy) `PhilAPIMCP` class for testing tool handlers. Intended to integrate `mock_adapter` when the real implementation uses `requests.Session`.
- **Usage**: Used by all test functions in `test_philapi_mcp.py`.
- **Dependencies**: `pytest`, `mock_adapter` fixture, `PhilAPIMCP` class (or dummy).




## TDD Cycles Log
### TDD Cycle: `get_document_metadata` (Not Found) - [%%current_timestamp%%]
- **Red**: Wrote failing test `test_get_document_metadata_not_found` for non-existent doc_id. / Test File: `testing/mcp-servers/db-mcp/test_db_mcp.py`
- **Outcome**: RED phase complete.

### TDD Cycle: `get_document_metadata` (Success) - [%%current_timestamp%%]
- **Red**: Wrote failing test `test_get_document_metadata_success` for existing doc_id. / Test File: `testing/mcp-servers/db-mcp/test_db_mcp.py`
- **Outcome**: RED phase complete.

### TDD Cycle: `query_similar_chunks` (Invalid Embedding) - [%%current_timestamp%%]
- **Red**: Wrote failing test `test_query_similar_chunks_invalid_embedding` for invalid query vector. / Test File: `testing/mcp-servers/db-mcp/test_db_mcp.py`
- **Outcome**: RED phase complete.

### TDD Cycle: `query_similar_chunks` (Invalid Date Filter) - [%%current_timestamp%%]
- **Red**: Wrote failing test `test_query_similar_chunks_invalid_date_filter` for invalid date string in filter. / Test File: `testing/mcp-servers/db-mcp/test_db_mcp.py`
- **Outcome**: RED phase complete.

### TDD Cycle: `query_similar_chunks` (Date Before Filter) - [%%current_timestamp%%]
- **Red**: Wrote failing test `test_query_similar_chunks_with_date_before_filter`. / Test File: `testing/mcp-servers/db-mcp/test_db_mcp.py`
- **Outcome**: RED phase complete.

### TDD Cycle: `query_similar_chunks` (Date After Filter) - [%%current_timestamp%%]
- **Red**: Wrote failing test `test_query_similar_chunks_with_date_after_filter`. / Test File: `testing/mcp-servers/db-mcp/test_db_mcp.py`
- **Outcome**: RED phase complete.

### TDD Cycle: `query_similar_chunks` (Multiple JSONB Filters) - [%%current_timestamp%%]
- **Red**: Wrote failing test `test_query_similar_chunks_with_multiple_jsonb_filters`. / Test File: `testing/mcp-servers/db-mcp/test_db_mcp.py`
- **Outcome**: RED phase complete.

### TDD Cycle: `query_similar_chunks` (Single JSONB Filter) - [%%current_timestamp%%]
- **Red**: Wrote failing test `test_query_similar_chunks_with_jsonb_filter`. / Test File: `testing/mcp-servers/db-mcp/test_db_mcp.py`
- **Outcome**: RED phase complete.

### TDD Cycle: `query_similar_chunks` (Zero Results) - [%%current_timestamp%%]
- **Red**: Wrote failing test `test_query_similar_chunks_zero_results`. / Test File: `testing/mcp-servers/db-mcp/test_db_mcp.py`
- **Outcome**: RED phase complete.

### TDD Cycle: `query_similar_chunks` (Fewer than K) - [%%current_timestamp%%]
- **Red**: Wrote failing test `test_query_similar_chunks_fewer_than_k`. / Test File: `testing/mcp-servers/db-mcp/test_db_mcp.py`
- **Outcome**: RED phase complete.

### TDD Cycle: `query_similar_chunks` (Success) - [%%current_timestamp%%]
- **Red**: Wrote failing test `test_query_similar_chunks_success`. / Test File: `testing/mcp-servers/db-mcp/test_db_mcp.py`
- **Outcome**: RED phase complete.

### TDD Cycle: `batch_insert_chunks` (Duplicate Index) - [%%current_timestamp%%]
- **Red**: Wrote failing test `test_batch_insert_chunks_duplicate_index_in_batch`. / Test File: `testing/mcp-servers/db-mcp/test_db_mcp.py`
- **Outcome**: RED phase complete.

### TDD Cycle: `batch_insert_chunks` (Invalid Doc ID) - [%%current_timestamp%%]
- **Red**: Wrote failing test `test_batch_insert_chunks_invalid_doc_id`. / Test File: `testing/mcp-servers/db-mcp/test_db_mcp.py`
- **Outcome**: RED phase complete.

### TDD Cycle: `batch_insert_chunks` (Large Batch) - [%%current_timestamp%%]
- **Red**: Wrote failing test `test_batch_insert_chunks_large_batch`. / Test File: `testing/mcp-servers/db-mcp/test_db_mcp.py`
- **Outcome**: RED phase complete.

### TDD Cycle: `batch_insert_chunks` (Update) - [%%current_timestamp%%]
- **Red**: Wrote failing test `test_batch_insert_chunks_update_on_conflict`. / Test File: `testing/mcp-servers/db-mcp/test_db_mcp.py`
- **Outcome**: RED phase complete.

### TDD Cycle: `batch_insert_chunks` (Success) - [%%current_timestamp%%]
- **Red**: Wrote failing test `test_batch_insert_chunks_success`. / Test File: `testing/mcp-servers/db-mcp/test_db_mcp.py`
- **Outcome**: RED phase complete.

### TDD Cycle: `add_document` (Complex Metadata) - [%%current_timestamp%%]
- **Red**: Wrote failing test `test_add_document_complex_metadata`. / Test File: `testing/mcp-servers/db-mcp/test_db_mcp.py`
- **Outcome**: RED phase complete.

### TDD Cycle: `add_document` (Invalid Date) - [%%current_timestamp%%]
- **Red**: Wrote failing test `test_add_document_invalid_date`. / Test File: `testing/mcp-servers/db-mcp/test_db_mcp.py`
- **Outcome**: RED phase complete.

### TDD Cycle: `add_document` (Null Values) - [%%current_timestamp%%]
- **Red**: Wrote failing test `test_add_document_null_values`. / Test File: `testing/mcp-servers/db-mcp/test_db_mcp.py`
- **Outcome**: RED phase complete.

### TDD Cycle: `add_document` (Update) - [%%current_timestamp%%]
- **Red**: Wrote failing test `test_add_document_update_on_conflict`. / Test File: `testing/mcp-servers/db-mcp/test_db_mcp.py`
- **Outcome**: RED phase complete.

### TDD Cycle: `add_document` (Success) - [%%current_timestamp%%]
- **Red**: Wrote failing test `test_add_document_success`. / Test File: `testing/mcp-servers/db-mcp/test_db_mcp.py`
- **Outcome**: RED phase complete.


### TDD Cycle: `get_philpapers_details` (API Error 5xx) - [2025-04-16 09:02:58]
- **Red**: Wrote failing test `test_get_details_api_error_5xx`. / Test File: `testing/mcp-servers/philapi-mcp/test_philapi_mcp.py`
- **Outcome**: RED phase complete.

### TDD Cycle: `get_philpapers_details` (Not Found 404) - [2025-04-16 09:02:58]
- **Red**: Wrote failing test `test_get_details_not_found`. / Test File: `testing/mcp-servers/philapi-mcp/test_philapi_mcp.py`
- **Outcome**: RED phase complete.

### TDD Cycle: `get_philpapers_details` (Success) - [2025-04-16 09:02:58]
- **Red**: Wrote failing test `test_get_details_success`. / Test File: `testing/mcp-servers/philapi-mcp/test_philapi_mcp.py`
- **Outcome**: RED phase complete.

### TDD Cycle: `search_philpapers` (With Filters) - [2025-04-16 09:02:58]
- **Red**: Wrote failing test `test_search_philpapers_with_filters`. / Test File: `testing/mcp-servers/philapi-mcp/test_philapi_mcp.py`
- **Outcome**: RED phase complete.

### TDD Cycle: `search_philpapers` (No Results) - [2025-04-16 09:02:58]
- **Red**: Wrote failing test `test_search_philpapers_no_results`. / Test File: `testing/mcp-servers/philapi-mcp/test_philapi_mcp.py`
- **Outcome**: RED phase complete.

### TDD Cycle: `search_philpapers` (API Error 5xx) - [2025-04-16 09:02:58]
- **Red**: Wrote failing test `test_search_philpapers_api_error_5xx`. / Test File: `testing/mcp-servers/philapi-mcp/test_philapi_mcp.py`
- **Outcome**: RED phase complete.

### TDD Cycle: `search_philpapers` (API Error 4xx) - [2025-04-16 09:02:58]
- **Red**: Wrote failing test `test_search_philpapers_api_error_4xx`. / Test File: `testing/mcp-servers/philapi-mcp/test_philapi_mcp.py`
- **Outcome**: RED phase complete.

### TDD Cycle: `search_philpapers` (Success) - [2025-04-16 09:02:58]
- **Red**: Wrote failing test `test_search_philpapers_success`. / Test File: `testing/mcp-servers/philapi-mcp/test_philapi_mcp.py`
- **Outcome**: RED phase complete.



<!-- Append TDD cycle outcomes using the format below -->

## Test Execution Results
### Test Execution: [Unit/Integration - DB-MCP Attempt 3] - [2025-04-16 08:33:44]
- **Trigger**: Manual (Task Request - GREEN Phase Verification after Attempt 2 corrections)
- **Outcome**: FAIL / **Summary**: 1 test failed, 20 passed
- **Failed Tests**:
    - `testing/mcp-servers/db-mcp/test_db_mcp.py::test_query_similar_chunks_success`: AssertionError: assert 'Chunk B (far).' == 'Chunk D (very close).'
- **Notes**: Previous fixes for casting (`::vector`) and cardinality violation were successful. The remaining failure is due to a test data design flaw: vectors used ([0.1]*1536, [0.9]*1536, [0.11]+[0.1]*1535) have near-zero cosine distance, making ordering unreliable. Test data needs redesign for meaningful similarity testing. GREEN phase incomplete.



### Test Execution: [Unit/Integration - DB-MCP Attempt 2] - [2025-04-16 08:04:03]
- **Trigger**: Manual (Task Request - GREEN Phase Verification after corrections)
- **Outcome**: FAIL / **Summary**: 8 tests failed, 13 passed
- **Failed Tests**:
    - `test_batch_insert_chunks_duplicate_index_in_batch`: psycopg2.errors.CardinalityViolation: ON CONFLICT DO UPDATE command cannot affect row a second time
    - `test_query_similar_chunks_success`: psycopg2.errors.UndefinedFunction: operator does not exist: vector <=> numeric[]
    - `test_query_similar_chunks_fewer_than_k`: psycopg2.errors.UndefinedFunction: operator does not exist: vector <=> numeric[]
    - `test_query_similar_chunks_zero_results`: psycopg2.errors.UndefinedFunction: operator does not exist: vector <=> numeric[]
    - `test_query_similar_chunks_with_jsonb_filter`: psycopg2.errors.UndefinedFunction: operator does not exist: vector <=> numeric[]
    - `test_query_similar_chunks_with_multiple_jsonb_filters`: psycopg2.errors.UndefinedFunction: operator does not exist: vector <=> numeric[]
    - `test_query_similar_chunks_with_date_after_filter`: psycopg2.errors.UndefinedFunction: operator does not exist: vector <=> numeric[]
    - `test_query_similar_chunks_with_date_before_filter`: psycopg2.errors.UndefinedFunction: operator does not exist: vector <=> numeric[]
- **Notes**: Dimension mismatch seems resolved for inserts, but persists for query parameter casting (`vector <=> numeric[]`). New failure reveals issue with handling duplicate keys within a single batch insert using ON CONFLICT DO UPDATE.



<!-- Append test run summaries using the format below -->
### Test Execution: [Unit/Integration - DB-MCP] - [2025-04-16 07:33:26]
- **Trigger**: Manual (Task Request - GREEN Phase Verification)
- **Outcome**: FAIL / **Summary**: 13 tests failed, 8 passed
- **Failed Tests**:
    - `test_batch_insert_chunks_success`: `psycopg2.errors.DataException: expected 1536 dimensions, not 3`
    - `test_batch_insert_chunks_update_on_conflict`: `psycopg2.errors.DataException: expected 1536 dimensions, not 3`
    - `test_batch_insert_chunks_large_batch`: `psycopg2.errors.DataException: expected 1536 dimensions, not 3`
    - `test_batch_insert_chunks_duplicate_index_in_batch`: `psycopg2.errors.DataException: expected 1536 dimensions, not 3`
    - `test_query_similar_chunks_success`: `psycopg2.errors.DataException: expected 1536 dimensions, not 3`
    - `test_query_similar_chunks_fewer_than_k`: `psycopg2.errors.DataException: expected 1536 dimensions, not 3`
    - `test_query_similar_chunks_zero_results`: `psycopg2.errors.UndefinedFunction: operator does not exist: vector <=> numeric[]`
    - `test_query_similar_chunks_with_jsonb_filter`: `psycopg2.errors.DataException: expected 1536 dimensions, not 3`
    - `test_query_similar_chunks_with_multiple_jsonb_filters`: `psycopg2.errors.DataException: expected 1536 dimensions, not 3`
    - `test_query_similar_chunks_with_date_after_filter`: `psycopg2.errors.DataException: expected 1536 dimensions, not 3`
    - `test_query_similar_chunks_with_date_before_filter`: `psycopg2.errors.DataException: expected 1536 dimensions, not 3`
    - `test_query_similar_chunks_invalid_date_filter`: `psycopg2.errors.DataException: expected 1536 dimensions, not 3`
    - `test_query_similar_chunks_invalid_embedding`: `psycopg2.errors.DataException: expected 1536 dimensions, not 3`
- **Notes**: Primary failure cause is embedding dimension mismatch in test data (used 3, DB requires 1536). Secondary issue with `vector <=> numeric[]` operator in `test_query_similar_chunks_zero_results`. Test fixtures/data need correction.



### Test Run: [2025-04-10 17:37:41] (Final Update)
- **Trigger**: Manual (Task Request) / **Env**: Local / **Suite**: Pipeline Integration Test (`rag_ingestion.py`)
- **Result**: FAIL / **Summary**: Test aborted. Root cause identified as invalid test EPUB generated by `testing/utils/epub_generator.py` (missing chapter content files). Pipeline script (`pipelines/rag_ingestion.py`) behaved correctly given invalid input. Pipeline script changes reverted.
- **Report Link**: N/A / **Failures**: `Test Data`: `test_pipeline.epub` was incomplete. `Verification`: Objective could not be met due to invalid test data.

### Test Run: [2025-04-10 17:26:08]
- **Trigger**: Manual (Task Request) / **Env**: Local / **Suite**: Pipeline Integration Test (`rag_ingestion.py`)
- **Result**: PARTIAL FAIL / **Summary**: EPUB Gen: OK, Pipeline Run: OK (after fix), Verification: Incomplete (TOC duplicated, artifact removal unverified due to read_file issue).
- **Report Link**: N/A / **Failures**: `Verification`: Incomplete content read from `library/rag-output/test_pipeline.rag.md`, duplicated TOC section observed.