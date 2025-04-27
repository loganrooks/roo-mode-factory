import sys
import os
import pytest
# Add project root to path to find mcp_servers module
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import requests_mock
import json
import sys
import pytest # Ensure pytest is imported
from typing import Optional

# Correct SDK imports based on actual package structure
try:
   from mcp.shared.exceptions import McpError
   import mcp.types as types # Import types module for ErrorData and codes
   # McpToolContext is not needed for these tests
   # ToolHandlerResponse is not part of the SDK, removed dummy
   print("Info: Successfully imported core SDK classes from mcp package.", file=sys.stderr)
   SDK_AVAILABLE = True
except ImportError as e:
    print(f"Error: Cannot import core MCP SDK classes from mcp package ({e}). Using dummies.", file=sys.stderr)
    SDK_AVAILABLE = False
    # Define dummy classes to allow test collection if SDK import fails
    class McpError(Exception):
        # Dummy McpError needs to accept ErrorData-like structure if used
        def __init__(self, error_data):
           super().__init__(error_data.message)
           self.error = error_data

    # Dummy types module and ErrorData
    class types:
        class ErrorData:
            def __init__(self, code, message, data=None):
               self.code = code
               self.message = message
               self.data = data
        # Define necessary error codes as constants
        INVALID_PARAMS = -32602
        INTERNAL_ERROR = -32603
        METHOD_NOT_FOUND = -32601
        # NotFound is not standard, use INTERNAL_ERROR for dummy
        NotFound = -32001 # Or map to INTERNAL_ERROR

# --- Dynamic Import Workaround ---
# Standard import fails because the parent directory 'mcp-servers' contains a hyphen,
# which is invalid in Python package/module names.
# We use 'importlib' to load the server's 'main.py' file directly by its path.
import importlib.util

# Calculate the absolute path to the server's main.py file
main_py_path = os.path.abspath(os.path.join(
    os.path.dirname(__file__),           # Current file's directory
    '..', '..', '..',                    # Up three levels to project root
    'mcp-servers', 'philapi-mcp', 'main.py' # Path to the target file
))

# Create a module specification from the file path
# Use a valid Python module name (e.g., replace hyphen with underscore)
module_name = "philapi_mcp_main"
spec = importlib.util.spec_from_file_location(module_name, main_py_path)

# Attempt to load the module using the spec
if spec and spec.loader:
    try:
        # Create an empty module object
        philapi_main_module = importlib.util.module_from_spec(spec)
        # Add the new module to sys.modules *before* execution
        # This allows relative imports within the loaded module (if any) to work
        sys.modules[module_name] = philapi_main_module
        # Execute the module's code to populate the module object
        spec.loader.exec_module(philapi_main_module)

        # Import the necessary class and constants from the dynamically loaded module
        PhilAPIMCP = philapi_main_module.PhilApiMcpServer
        PHILPAPERS_API_BASE_URL = philapi_main_module.PHILPAPERS_SEARCH_URL
        PHILPAPERS_DETAILS_URL_TEMPLATE = philapi_main_module.PHILPAPERS_DETAILS_URL_TEMPLATE
        print(f"INFO: Successfully imported PhilApiMcpServer via importlib from {main_py_path}", file=sys.stderr)
        IMPORTLIB_LOAD_SUCCESS = True
    except Exception as e:
        print(f"FATAL: Error during importlib loading of {main_py_path}: {e}", file=sys.stderr)
        IMPORTLIB_LOAD_SUCCESS = False
else:
    print(f"FATAL: Could not create module spec for {main_py_path}", file=sys.stderr)
    IMPORTLIB_LOAD_SUCCESS = False

# Define dummy/placeholder values if dynamic import failed, allowing tests to be collected
if not IMPORTLIB_LOAD_SUCCESS:
    PHILPAPERS_API_BASE_URL = "https://philpapers.org/oai.json" # Placeholder
    PHILPAPERS_DETAILS_URL_TEMPLATE = "https://philpapers.org/rec/{id}.json" # Placeholder
    # Define dummy class so tests can be collected but will fail at runtime
    class PhilAPIMCP:
        def __init__(self, *args, **kwargs): pass # Add dummy init
        async def _handle_search_philpapers(self, arguments): raise NotImplementedError("PhilAPIMCP dynamic import failed")
        async def _handle_get_philpapers_details(self, arguments): raise NotImplementedError("PhilAPIMCP dynamic import failed")
    # Optionally raise ImportError here to halt test collection completely if preferred
    # raise ImportError(f"Could not load PhilAPIMCP server from {main_py_path}")


# --- Fixtures ---

@pytest.fixture
def mock_adapter():
    """Provides a requests_mock adapter."""
    adapter = requests_mock.Adapter()
    return adapter

@pytest.fixture
def philapi_mcp_instance(mock_adapter):
    """Provides an instance of the PhilAPIMCP server, potentially with mocked session."""
    # In a real scenario, you might inject the mock adapter into the server's session
    # For now, just instantiate the (potentially dummy) class
    instance = PhilAPIMCP()
    # If the real class uses requests.Session, you'd mount the adapter:
    # instance.session.mount('mock://', mock_adapter)
    return instance

# --- Test Data ---

MOCK_SEARCH_SUCCESS_RESPONSE = {
    "results": [
        {"id": "PAPER123", "title": "Test Paper 1", "authors": ["Author A"]},
        {"id": "PAPER456", "title": "Test Paper 2", "authors": ["Author B", "Author C"]},
    ],
    "total": 2,
    "offset": 0,
    "count": 2
}

MOCK_DETAILS_SUCCESS_RESPONSE = {
    "id": "PAPER123",
    "title": "Test Paper 1",
    "authors": ["Author A"],
    "abstract": "This is a test abstract.",
    "year": 2023,
    "journal": "Journal of Tests",
    "links": {"pdf": "http://example.com/paper123.pdf"}
}

# --- Tests for search_philpapers ---

@pytest.mark.asyncio
async def test_search_philpapers_success(philapi_mcp_instance, mock_adapter):
    """Test successful search returns expected structure."""
    query = "test query"
    # Construct URL based on how the actual implementation builds it (query param name)
    mock_url = f"{PHILPAPERS_API_BASE_URL}?query={query}" # Assuming 'query' param based on main.py logic
    mock_adapter.register_uri('GET', mock_url, json=MOCK_SEARCH_SUCCESS_RESPONSE, status_code=200)

    # This assumes the real implementation uses requests and the adapter is mounted
    # For the RED phase, the call itself might fail if the class is a dummy
    with requests_mock.Mocker(adapter=mock_adapter):
        # Call the tool handler method directly for testing unit logic
        # The SDK would normally wrap this in a request/response cycle
        # We simulate the arguments the handler expects
        # Directly call the internal handler method
        handler_result = await philapi_mcp_instance._handle_search_philpapers({"query": query})

    # Assertions on the structure returned by the handler
    assert isinstance(handler_result, dict)
    assert handler_result.get("success") is True
    assert "results" in handler_result
    assert isinstance(handler_result["results"], list)
    assert len(handler_result["results"]) == 2
    # Check specific fields based on mock data and expected mapping
    assert handler_result["results"][0].get("source_id") == "PAPER123"
    assert handler_result["results"][0].get("title") == "Test Paper 1"

@pytest.mark.asyncio
async def test_search_philpapers_api_error_4xx(philapi_mcp_instance, mock_adapter):
    """Test handling of 4xx API errors during search."""
    query = "bad query"
    mock_url = f"{PHILPAPERS_API_BASE_URL}?query={query}"
    mock_adapter.register_uri('GET', mock_url, status_code=400, text="Bad Request")

    with requests_mock.Mocker(adapter=mock_adapter):
        # Directly call the internal handler method
        # Expect McpError for 4xx errors based on main.py's _make_api_request
        with pytest.raises(McpError) as excinfo:
            await philapi_mcp_instance._handle_search_philpapers({"query": query})

    # Check the McpError details
    assert excinfo.value.error.code == types.INVALID_PARAMS
    assert "400" in excinfo.value.error.message # Check for status code in error message

@pytest.mark.asyncio
async def test_search_philpapers_api_error_5xx(philapi_mcp_instance, mock_adapter):
    """Test handling of 5xx API errors during search."""
    query = "server error query"
    mock_url = f"{PHILPAPERS_API_BASE_URL}?query={query}"
    mock_adapter.register_uri('GET', mock_url, status_code=500, text="Internal Server Error")

    with requests_mock.Mocker(adapter=mock_adapter):
        # Directly call the internal handler method
        # Expect McpError for 5xx errors based on main.py's _make_api_request
        with pytest.raises(McpError) as excinfo:
            await philapi_mcp_instance._handle_search_philpapers({"query": query})

    # Check the McpError details
    assert excinfo.value.error.code == types.INTERNAL_ERROR
    assert "500" in excinfo.value.error.message # Check for status code in error message

@pytest.mark.asyncio
async def test_search_philpapers_no_results(philapi_mcp_instance, mock_adapter):
    """Test search returning no results."""
    query = "obscure query"
    mock_url = f"{PHILPAPERS_API_BASE_URL}?query={query}"
    # Mock needs to match the structure the implementation expects after parsing
    mock_adapter.register_uri('GET', mock_url, json={"results": [], "total": 0}, status_code=200)

    with requests_mock.Mocker(adapter=mock_adapter):
        # Directly call the internal handler method
        handler_result = await philapi_mcp_instance._handle_search_philpapers({"query": query})

    # Assertions for a successful call but empty results list
    assert isinstance(handler_result, dict)
    assert handler_result.get("success") is True
    assert "results" in handler_result
    assert isinstance(handler_result["results"], list)
    assert len(handler_result["results"]) == 0

@pytest.mark.asyncio
async def test_search_philpapers_with_filters(philapi_mcp_instance, mock_adapter):
    """Test search with filters (e.g., year)."""
    query = "filtered query"
    year = 2022
    # Adjust mock URL based on how filters are implemented in main.py
    mock_url = f"{PHILPAPERS_API_BASE_URL}?query={query}&year={year}" # Assuming 'year' param
    mock_adapter.register_uri('GET', mock_url, json=MOCK_SEARCH_SUCCESS_RESPONSE, status_code=200)

    with requests_mock.Mocker(adapter=mock_adapter):
        # Pass filters correctly in arguments
        # Directly call the internal handler method
        handler_result = await philapi_mcp_instance._handle_search_philpapers({"query": query, "filters": {"publicationYear": year}})

    # Assertions for a successful call with filters
    assert isinstance(handler_result, dict)
    assert handler_result.get("success") is True
    assert "results" in handler_result
    assert len(handler_result["results"]) > 0 # Assuming mock returns results

# --- Tests for get_philpapers_details ---

@pytest.mark.asyncio
async def test_get_details_success(philapi_mcp_instance, mock_adapter):
    """Test successful retrieval of paper details."""
    source_id = "PAPER123"
    # Use the URL template defined/imported
    mock_url = PHILPAPERS_DETAILS_URL_TEMPLATE.format(id=source_id)
    mock_adapter.register_uri('GET', mock_url, json=MOCK_DETAILS_SUCCESS_RESPONSE, status_code=200)

    with requests_mock.Mocker(adapter=mock_adapter):
        # Directly call the internal handler method
        handler_result = await philapi_mcp_instance._handle_get_philpapers_details({"source_id": source_id})

    # Assertions on the successful details response
    assert isinstance(handler_result, dict)
    assert handler_result.get("success") is True
    details_data = handler_result.get("details") # Handler returns dict with 'details' key
    assert isinstance(details_data, dict)
    assert details_data.get("id") == source_id
    assert "abstract" in details_data

@pytest.mark.asyncio
async def test_get_details_not_found(philapi_mcp_instance, mock_adapter):
    """Test handling of invalid/non-existent source_id."""
    source_id = "INVALID999"
    mock_url = PHILPAPERS_DETAILS_URL_TEMPLATE.format(id=source_id)
    mock_adapter.register_uri('GET', mock_url, status_code=404, text="Not Found")

    with requests_mock.Mocker(adapter=mock_adapter):
        # Directly call the registered handler method
        # Directly call the internal handler method
        # The internal handler now raises McpError on 404, which the test framework should catch.
        # We expect an McpError to be raised here.
        with pytest.raises(McpError) as excinfo:
             await philapi_mcp_instance._handle_get_philpapers_details({"source_id": source_id})
        # Optionally check the error details
        # Use the correct error code from types module (NotFound isn't standard)
        # main.py raises INTERNAL_ERROR for 404 in _handle_get_philpapers_details
        assert excinfo.value.error.code == types.INTERNAL_ERROR
        assert "not found" in str(excinfo.value.error.message).lower() # Corrected access to error.message

@pytest.mark.asyncio
async def test_get_details_api_error_5xx(philapi_mcp_instance, mock_adapter):
    """Test handling of 5xx API errors during detail retrieval."""
    source_id = "ERROR500ID"
    mock_url = PHILPAPERS_DETAILS_URL_TEMPLATE.format(id=source_id)
    mock_adapter.register_uri('GET', mock_url, status_code=500, text="Server Error")

    with requests_mock.Mocker(adapter=mock_adapter):
        # The internal handler raises McpError on 500 via _make_api_request
        with pytest.raises(McpError) as excinfo:
            await philapi_mcp_instance._handle_get_philpapers_details({"source_id": source_id})
        # Optionally check the error details
        # Use the correct error code from types module
        assert excinfo.value.error.code == types.INTERNAL_ERROR
        assert "500" in str(excinfo.value.error.message) or "Server Error" in str(excinfo.value.error.message).lower() # Corrected access to error.message

# Add more tests as needed based on spec (e.g., rate limiting simulation if possible)