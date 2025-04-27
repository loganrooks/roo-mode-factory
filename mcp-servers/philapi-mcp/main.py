#!/usr/bin/env python3
"""
MCP Server for interacting with external Philosophy APIs (e.g., PhilPapers).

This server provides tools for RooCode modes to search and retrieve data
from philosophy-related databases and APIs.
"""

import os
import sys
import logging
import json
import requests
from datetime import date
from dotenv import load_dotenv
import asyncio
from typing import Dict, Any, List, Optional, Iterable

# --- SDK Import ---
# Attempt to import the installed 'mcp' package.
# Includes dummy classes for basic script loading if the SDK is missing.
try:
    # Import necessary components from the mcp package based on SDK structure
    from mcp.server import Server
    from mcp.server.stdio import stdio_server # Context manager for stdio transport
    from mcp.shared.exceptions import McpError
    import mcp.types as types # Contains ErrorData, Content types, error codes
    from mcp.server.models import InitializationOptions # For server.run

    # Note: Decorators like @server.tool_handler, @server.list_tools, @server.call_tool
    # are methods of the Server instance, not separate imports.

    print("INFO: Successfully imported core SDK classes from mcp package.", file=sys.stderr)
    MCP_SDK_AVAILABLE = True
except ImportError as e:
    # If import fails, print the error, set flag, and define dummy classes
    print(f"FATAL: Cannot import core MCP SDK classes from mcp package: {e}", file=sys.stderr)
    print("       Ensure 'mcp' package is installed in the correct environment.", file=sys.stderr)
    MCP_SDK_AVAILABLE = False
    # Define dummy classes to allow script to load but fail later if SDK is missing
    class Server:
        def list_tools(self, *args, **kwargs):
            def decorator(func):
                return func
            return decorator
        def call_tool(self, *args, **kwargs):
            def decorator(func):
                return func
            return decorator
        async def run(self, *args, **kwargs): pass
        async def close(self): pass
        def get_capabilities(self, *args, **kwargs): return {}
        def create_initialization_options(self, *args, **kwargs): return None
        def __init__(self, *args, **kwargs): pass

    class stdio_server: # Dummy context manager
        async def __aenter__(self): return (None, None)
        async def __aexit__(self, exc_type, exc, tb): pass

    class McpError(Exception):
        def __init__(self, error_data):
           super().__init__(error_data.message)
           self.error = error_data

    class types: # Dummy types module
        class ErrorData:
            def __init__(self, code, message, data=None):
               self.code = code; self.message = message; self.data = data
        class TextContent:
             def __init__(self, type, text): self.type = type; self.text = text
        class ImageContent: pass # Dummy
        class EmbeddedResource: pass # Dummy
        # Define necessary error codes as constants
        INVALID_PARAMS = -32602; INTERNAL_ERROR = -32603; METHOD_NOT_FOUND = -32601
        # Custom/non-standard codes used internally
        NotFound = -32001 # Placeholder for internal 404 mapping

    class InitializationOptions: pass # Dummy class

# --- Configuration ---

# Load .env file for local development secrets/config
load_dotenv()

# Setup logging to stderr
LOG_LEVEL_NAME = os.getenv("LOG_LEVEL", "INFO").upper()
logging.basicConfig(level=LOG_LEVEL_NAME, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', stream=sys.stderr)
logger = logging.getLogger("PhilApiMcpServer")

# API Configuration
PHILPAPERS_API_KEY = os.getenv("PHILPAPERS_API_KEY") # Optional, depends on API requirements
REQUESTS_TIMEOUT = int(os.getenv("REQUESTS_TIMEOUT", 30)) # Timeout for API calls

# Base URLs (Using placeholders based on spec/tests due to API doc discrepancy)
# Actual PhilPapers JSON API for search/details might differ or require specific agreements.
PHILPAPERS_SEARCH_URL = os.getenv("PHILPAPERS_SEARCH_URL", "https://philpapers.org/oai.json")
PHILPAPERS_DETAILS_URL_TEMPLATE = os.getenv("PHILPAPERS_DETAILS_URL_TEMPLATE", "https://philpapers.org/rec/{id}.json")
# OPENLIBRARY_BASE_URL = "https://openlibrary.org" # Example for future extension
# DOAB_BASE_URL = "https://directory.doabooks.org/rest/search" # Example for future extension

# --- Server Implementation ---

class PhilApiMcpServer(Server):
    """
    MCP Server providing tools to query external philosophy APIs (PhilPapers).

    Handles communication with the MCP client (RooCode) and makes requests
    to the configured philosophy API endpoints.
    """
    def __init__(self):
        """Initializes the server and the HTTP client session."""
        # Initialize the base MCP Server
        super().__init__(name="philapi-mcp")

        # Initialize persistent HTTP client session for connection reuse
        self.http_session = requests.Session()
        self.http_session.headers.update({"User-Agent": "RooCodePhilApiMcpServer/1.0"})

        # Log API key status (without logging the key itself)
        if PHILPAPERS_API_KEY:
            # Note: Actual header needed depends on the API (e.g., 'Authorization': f'Bearer {key}')
            # self.http_session.headers.update({"X-API-Key": PHILPAPERS_API_KEY}) # Example
            logger.info("PHILPAPERS_API_KEY is set (available if required by API).")
        else:
            logger.warning("PHILPAPERS_API_KEY is not set. API calls will be anonymous.")

        # Register tool handlers defined in this class
        self.register_tool_handlers()

    def _make_api_request(self, method: str, url: str, params: Optional[Dict] = None, data: Optional[Dict] = None, headers: Optional[Dict] = None) -> Any:
        """
        Helper function to make HTTP requests to the external API.

        Handles common request patterns, JSON decoding, and error conditions,
        translating them into McpError exceptions.

        Args:
            method: HTTP method (e.g., 'GET', 'POST').
            url: The URL for the API endpoint.
            params: Optional dictionary of URL query parameters.
            data: Optional dictionary of data for the request body (sent as JSON).
            headers: Optional dictionary of additional HTTP headers.

        Returns:
            The parsed JSON response from the API.

        Raises:
            McpError: If the API request fails due to network issues, timeouts,
                      bad status codes (4xx/5xx), or JSON decoding errors.
        """
        try:
            logger.debug(f"Making API request: {method} {url} Params: {params}")
            response = self.http_session.request(
                method=method,
                url=url,
                params=params,
                json=data, # Send body data as JSON
                headers=headers,
                timeout=REQUESTS_TIMEOUT
            )
            response.raise_for_status() # Raises HTTPError for 4xx/5xx responses

            # Handle successful responses
            if response.status_code == 204: # No Content
                logger.debug(f"Received 204 No Content from {url}")
                return None
            try:
                json_response = response.json()
                logger.debug(f"Received successful JSON response from {url}")
                return json_response
            except json.JSONDecodeError as json_err:
                logger.error(f"Failed to decode JSON response from {url}: {json_err}")
                logger.debug(f"Response text (first 500 chars): {response.text[:500]}")
                raise McpError(types.ErrorData(
                    code=types.INTERNAL_ERROR,
                    message=f"Invalid JSON response received from API: {url}"
                )) from json_err

        except requests.exceptions.Timeout as e:
            logger.error(f"API request timed out after {REQUESTS_TIMEOUT}s: {url}")
            raise McpError(types.ErrorData(
                code=types.INTERNAL_ERROR,
                message=f"API request timed out: {e}"
            )) from e
        except requests.exceptions.HTTPError as e:
            status_code = e.response.status_code
            response_text_preview = e.response.text[:200] # Limit error text length
            logger.error(f"API request failed: {url} - Status {status_code} - Response: {response_text_preview}")

            # Map HTTP status codes to McpError codes
            if status_code == 429: # Too Many Requests
                error_message = f"API rate limit exceeded for {url}. Please try again later."
                error_code = types.INTERNAL_ERROR # Or a custom rate limit code if defined
            elif status_code == 404: # Not Found
                # Let specific handlers decide if 404 is an error or expected (e.g., get_details)
                # Raise a generic error here; handlers can catch and customize if needed.
                error_message = f"API resource not found ({status_code}): {url}"
                error_code = types.INTERNAL_ERROR # Using generic internal error for 404 by default
            elif 400 <= status_code < 500: # Other Client Errors (e.g., 400 Bad Request, 401 Unauthorized, 403 Forbidden)
                error_message = f"API request failed ({status_code} Client Error): {response_text_preview}"
                error_code = types.INVALID_PARAMS # Map client errors to invalid params generally
            else: # 5xx Server Errors
                error_message = f"API request failed ({status_code} Server Error): {response_text_preview}"
                error_code = types.INTERNAL_ERROR

            raise McpError(types.ErrorData(code=error_code, message=error_message)) from e
        except requests.exceptions.RequestException as e:
            # Catch other potential requests errors (e.g., connection errors)
            logger.error(f"API request failed due to network issue: {url} - {e}")
            raise McpError(types.ErrorData(
                code=types.INTERNAL_ERROR,
                message=f"API request failed (network issue): {e}"
            )) from e

    def register_tool_handlers(self):
        """Registers handlers for the server's tools using SDK decorators."""
        logger.debug("Registering tool handlers...")

        # --- Handler for tools/list ---
        @self.list_tools()
        async def list_tools(params: Dict) -> Dict:
            """Handles the 'tools/list' request, returning available tools."""
            logger.info("Received tools/list request")
            # Define the tools provided by this server
            # Schemas should match the expected inputs/outputs of the handler logic.
            return {
                "tools": [
                    {
                        "name": "search_philpapers",
                        "description": "Searches the PhilPapers database (using assumed API structure based on tests).",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "query": {"type": "string", "description": "Search query terms."},
                                "filters": {
                                    "type": ["object", "null"],
                                    "description": "Optional filters (e.g., {'publicationYear': 2023, 'author': 'Kant'}). Structure depends on API.",
                                    "default": {}
                                }
                            },
                            "required": ["query"]
                        },
                        "outputSchema": {
                             "type": "object",
                             "properties": {
                                 "success": {"type": "boolean", "description": "Indicates if the search was processed successfully."},
                                 "results": {
                                     "type": "array",
                                     "description": "List of search results.",
                                     "items": {
                                         "type": "object",
                                         "properties": {
                                             "title": {"type": ["string", "null"]},
                                             "authors": {"type": "array", "items": {"type": "string"}},
                                             "abstract": {"type": ["string", "null"]},
                                             "url": {"type": ["string", "null"]},
                                             "source_id": {"type": ["string", "integer", "null"], "description": "Unique ID from PhilPapers."}
                                         },
                                         "required": ["title", "authors", "source_id"] # Core required fields
                                     }
                                 },
                                 "error": {"type": ["string", "null"], "description": "Error message if success is false."}
                             },
                             "required": ["success"]
                         }
                    },
                    {
                        "name": "get_philpapers_details",
                        "description": "Gets details for a PhilPapers entry by ID (using assumed API structure based on tests).",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "source_id": {"type": "string", "description": "The unique ID from PhilPapers (e.g., 'PAPER123')."}
                            },
                            "required": ["source_id"]
                        },
                        "outputSchema": {
                             "type": "object",
                             "properties": {
                                 "success": {"type": "boolean", "description": "Indicates if details were retrieved successfully."},
                                 "details": {"type": ["object", "null"], "description": "Detailed information object for the entry."},
                                 "error": {"type": ["string", "null"], "description": "Error message if success is false."}
                             },
                             "required": ["success"]
                         }
                    },
                    # Add definitions for other tools (e.g., search_other_apis) here if implemented
                ]
            }

        # --- Handler for tools/call ---
        @self.call_tool()
        async def handle_call_tool(self, name: str, arguments: Optional[dict]) -> Iterable[types.TextContent | types.ImageContent | types.EmbeddedResource]:
            """
            Handles incoming 'tools/call' requests by dispatching to the appropriate internal handler.

            Args:
                name: The name of the tool being called.
                arguments: The arguments provided for the tool call.

            Returns:
                An iterable containing Content items (e.g., TextContent with JSON result).

            Raises:
                McpError: If the tool name is not found or if the internal handler raises an McpError.
                          Other exceptions are caught by the SDK decorator and converted to INTERNAL_ERROR.
            """
            tool_name = name
            tool_args = arguments or {} # Ensure args is a dict even if None
            logger.info(f"Received tools/call request for tool: '{tool_name}' with args: {tool_args}")

            # Dispatch to the corresponding internal handler method
            if tool_name == "search_philpapers":
                result_data = await self._handle_search_philpapers(tool_args)
            elif tool_name == "get_philpapers_details":
                result_data = await self._handle_get_philpapers_details(tool_args)
            # Add elif for other tools here
            else:
                logger.error(f"Attempted to call unknown tool: '{tool_name}'")
                raise McpError(types.ErrorData(
                    code=types.METHOD_NOT_FOUND,
                    message=f"Tool '{tool_name}' not found."
                ))

            # Wrap the dictionary result in a TextContent object containing a JSON string
            # The SDK expects an iterable of Content items as the return value.
            logger.debug(f"Tool '{tool_name}' executed successfully. Returning result.")
            return [types.TextContent(type="text", text=json.dumps(result_data))]

    # --- Internal Handler Methods ---

    async def _handle_search_philpapers(self, tool_args: Dict) -> Dict:
        """
        Internal logic for handling the 'search_philpapers' tool call.

        Performs the search against the PhilPapers API (using placeholder URL)
        and formats the response.

        Args:
            tool_args: Dictionary containing the 'query' and optional 'filters'.

        Returns:
            A dictionary containing 'success' (bool) and 'results' (list) or 'error' (str).
        """
        # Basic input validation (more robust schema validation could be added)
        if "query" not in tool_args or not isinstance(tool_args["query"], str):
            raise McpError(types.ErrorData(
                code=types.INVALID_PARAMS,
                message="Missing or invalid 'query' argument (string) for search_philpapers."
            ))

        query = tool_args["query"]
        filters = tool_args.get("filters", {})
        if not isinstance(filters, dict):
             logger.warning(f"Invalid 'filters' type received: {type(filters)}. Ignoring filters.")
             filters = {}

        # Construct API parameters based on assumed API structure (from tests/spec)
        api_params = {"query": query} # Assuming 'query' parameter name based on test mock
        # Add API key if required by the actual API
        # if PHILPAPERS_API_KEY:
        #     api_params["apiKey"] = PHILPAPERS_API_KEY

        # Map filters from input schema to API parameters (adjust based on actual API)
        if "publicationYear" in filters:
            api_params["year"] = filters["publicationYear"] # Assuming 'year' param based on test
        if "author" in filters:
            api_params["author"] = filters["author"]
        # Add other filter mappings here...

        logger.info(f"Performing PhilPapers search with query: '{query}', filters: {filters}")
        api_response = self._make_api_request("GET", PHILPAPERS_SEARCH_URL, params=api_params)

        # Process and map the API response to the tool's output schema
        results = []
        # Assuming the API response structure matches the test mock (a dict with a 'results' list)
        if isinstance(api_response, dict) and "results" in api_response and isinstance(api_response["results"], list):
             for item in api_response["results"]:
                  if isinstance(item, dict):
                       # Map fields based on assumed API response and output schema
                       results.append({
                           "title": item.get("title"),
                           "authors": item.get("authors", []), # Default to empty list
                           "abstract": item.get("abstract"), # Optional field
                           "url": item.get("url"), # Optional field
                           "source_id": item.get("id") # Assuming 'id' maps to 'source_id'
                       })
                  else:
                       logger.warning(f"Skipping non-dictionary item in API results list: {item}")
        else:
            # Log unexpected format but still return success with empty results
            logger.warning(f"Unexpected API response format from {PHILPAPERS_SEARCH_URL}. Expected dict with 'results' list, got: {type(api_response)}")

        logger.info(f"PhilPapers search for '{query}' returned {len(results)} results.")
        return {"success": True, "results": results}

    async def _handle_get_philpapers_details(self, tool_args: Dict) -> Dict:
        """
        Internal logic for handling the 'get_philpapers_details' tool call.

        Retrieves details for a specific PhilPapers entry by its ID.

        Args:
            tool_args: Dictionary containing the 'source_id'.

        Returns:
            A dictionary containing 'success' (bool) and 'details' (dict) or 'error' (str).
        """
        # Basic input validation
        if "source_id" not in tool_args or not isinstance(tool_args["source_id"], str):
            raise McpError(types.ErrorData(
                code=types.INVALID_PARAMS,
                message="Missing or invalid 'source_id' argument (string) for get_philpapers_details."
            ))

        source_id = tool_args["source_id"]
        details_url = PHILPAPERS_DETAILS_URL_TEMPLATE.format(id=source_id)
        api_params = {}
        # Add API key if required
        # if PHILPAPERS_API_KEY:
        #     api_params["apiKey"] = PHILPAPERS_API_KEY

        logger.info(f"Retrieving details for PhilPapers ID: {source_id} from {details_url}")
        try:
            api_response = self._make_api_request("GET", details_url, params=api_params)
            # Assuming the API returns the details object directly on success
            logger.info(f"Successfully retrieved details for PhilPapers ID: {source_id}")
            return {"success": True, "details": api_response}
        except McpError as e:
             # Check if the error was due to a 404 (Not Found) from _make_api_request
             # _make_api_request raises INTERNAL_ERROR for 404 by default
             if e.error.code == types.INTERNAL_ERROR and "404" in e.error.message:
                  logger.warning(f"PhilPapers entry with ID '{source_id}' not found (404).")
                  # Re-raise with a more specific message, still using INTERNAL_ERROR
                  # as NotFound isn't a standard JSON-RPC code.
                  raise McpError(types.ErrorData(
                      code=types.INTERNAL_ERROR, # Or a custom code like types.NotFound if client handles it
                      message=f"PhilPapers entry with ID '{source_id}' not found."
                  )) from e
             else:
                  # Re-raise other McpErrors (e.g., timeouts, 5xx errors, other 4xx)
                  logger.error(f"API error retrieving details for ID {source_id}: {e.error.message}")
                  raise e


    async def shutdown(self):
        """Handles graceful shutdown: closes HTTP session and base server."""
        logger.info("Shutting down PhilAPI MCP server...")
        if self.http_session:
            self.http_session.close()
            logger.debug("HTTP session closed.")
        await super().close() # Call base server close method
        logger.info("PhilAPI MCP Server shut down complete.")

# --- Entry Point ---
async def main():
    """Sets up and runs the MCP server."""
    logger.info("Initializing PhilApiMcpServer...")
    server_instance = PhilApiMcpServer()
    init_options = server_instance.create_initialization_options() # Get init options from server

    logger.info("Starting server using stdio transport...")
    # Use the stdio_server context manager for handling transport
    try:
        async with stdio_server() as (read_stream, write_stream):
            logger.info('PhilAPI MCP Server connected via stdio. Running...')
            # Pass streams and init_options to the server's run method
            await server_instance.run(read_stream, write_stream, init_options)
            logger.info('PhilAPI MCP Server finished running normally.')
    except McpError as e:
        # Catch MCP-specific errors during connection or execution
        logger.critical(f"MCP Error during server execution: {e.error.message} (Code: {e.error.code})")
        sys.exit(f"Server Execution Failed: {e.error.message}")
    except Exception as e:
        # Catch unexpected errors during setup or run
        logger.critical(f"Unexpected error starting or running PhilAPI MCP server: {e}", exc_info=True)
        sys.exit(f"Unexpected Server Error: {e}")
    finally:
        # Ensure shutdown logic is called, even if run finishes without error
        # Note: SIGINT handling might need adjustment depending on the parent process.
        await server_instance.shutdown()

if __name__ == "__main__":
    if not MCP_SDK_AVAILABLE:
        logger.critical("MCP SDK is not available. Cannot start server.")
        sys.exit("MCP SDK not available. Cannot start server.")

    # Basic signal handling (may be overridden by parent process)
    # import signal
    # loop = asyncio.get_event_loop()
    # for sig in (signal.SIGINT, signal.SIGTERM):
    #     loop.add_signal_handler(sig, lambda s=sig: asyncio.create_task(shutdown_signal(s, loop)))

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("KeyboardInterrupt received (likely handled by main's finally block).")
    except Exception as e:
        # Final catch-all for errors during asyncio.run itself
        logger.critical(f"Unhandled exception during server execution: {e}", exc_info=True)
        sys.exit(f"Unhandled Server Error: {e}")