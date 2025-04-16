# Z-Library API Client (`zlibrary`) Notes

This document summarizes the usage and features of the unofficial `zlibrary` Python library (`sertraline/zlibrary`), based on analysis of its README and source code (as of 2025-04-10).

**Disclaimer:** This is an unofficial library and may break if Z-Library changes its website structure or API.

## Installation

```bash
pip install zlibrary
```

## Core Usage (Async)

The primary interface is the `AsyncZlib` class.

```python
import zlibrary
import asyncio
import os
from dotenv import load_dotenv

# Load credentials (example)
load_dotenv()
ZLIBRARY_EMAIL = os.getenv("ZLIBRARY_EMAIL")
ZLIBRARY_PASSWORD = os.getenv("ZLIBRARY_PASSWORD")

async def main():
    # Initialize the client (optionally with session, proxy, onion settings)
    # Using a session is recommended for cookie management
    async with aiohttp.ClientSession() as session:
        lib = zlibrary.AsyncZlib(session=session)

        # --- Authentication ---
        try:
            await lib.login(ZLIBRARY_EMAIL, ZLIBRARY_PASSWORD)
            print("Login successful")
        except zlibrary.exception.LoginFailed as e:
            print(f"Login failed: {e}")
            return
        except Exception as e:
            print(f"An unexpected error occurred during login: {e}")
            return

        # --- Searching ---
        try:
            # Metadata Search
            paginator = await lib.search(
                mesasage="Python Programming",
                limit=10, # Results per page
                order=zlibrary.OrderOptions.POPULAR,
                extensions=[zlibrary.Extension.EPUB],
                languages=[zlibrary.Language.ENGLISH],
                from_year=2020
            )

            # Fetch first page of results
            results = await paginator.next()
            print(f"Found {len(results)} results on page 1:")
            for i, item in enumerate(results):
                print(f"  {i+1}. {item.get('name')} by {item.get('authors', [])}")

            # Navigate pagination
            # next_page_results = await paginator.next()
            # prev_page_results = await paginator.prev()
            # current_results = paginator.result # Access cached results for current page

            # Full-Text Search (Example)
            # ft_paginator = await lib.full_text_search(
            #     message="specific phrase from a book",
            #     phrase=True, # Search for exact phrase
            #     extensions=[zlibrary.Extension.PDF]
            # )
            # ft_results = await ft_paginator.next()

        except zlibrary.exception.EmptyQueryError:
            print("Search query cannot be empty.")
        except Exception as e:
            print(f"An error occurred during search: {e}")
            return

        # --- Fetching Book Details & Download URL ---
        if results:
            selected_item = results[0] # Example: select the first result
            try:
                print(f"Fetching details for: {selected_item.get('name')}")
                # Use the fetch() method on the search result item
                book_details = await selected_item.fetch()

                print(f"Year: {book_details.get('year')}")
                print(f"Description: {book_details.get('description', 'N/A')[:100]}...")
                download_url = book_details.get('download_url')

                if download_url:
                    print(f"Download URL found: {download_url}")
                    # Proceed with manual download using aiohttp (see acquire_epub.py)
                else:
                    print("Download URL not found in details.")

                # Alternative: Fetch by ID if known
                # known_id = '123456/abcdef' # Example ID format
                # details_by_id = await lib.get_by_id(known_id)
                # print(f"Fetched by ID: {details_by_id.get('name')}")

            except Exception as e:
                print(f"Error fetching book details: {e}")

        # --- Profile Information (Requires Login) ---
        if lib.profile:
            try:
                limits = await lib.profile.get_limits()
                print(f"Download Limits: {limits.get('daily_remaining')} remaining today.")

                # history_paginator = await lib.profile.download_history()
                # first_history_page = await history_paginator.next()

                # public_lists_paginator = await lib.profile.search_public_booklists(q="philosophy")
                # first_public_lists = await public_lists_paginator.next()

            except Exception as e:
                print(f"Error accessing profile information: {e}")

        # --- Logout (Optional) ---
        # await lib.logout() # Clears internal cookies

if __name__ == "__main__":
    # Requires aiohttp to be installed: pip install aiohttp
    import aiohttp
    asyncio.run(main())

```

## Key Classes & Objects

*   **`zlibrary.AsyncZlib`**: The main asynchronous client class.
    *   `__init__(session=None, onion=False, proxy_list=None, disable_semaphore=False)`: Initializes the client. Pass an `aiohttp.ClientSession` for cookie management. Set `onion=True` and provide `proxy_list` for Tor access.
    *   `login(email, password)`: Authenticates with Z-Library. Required for most operations. Raises `LoginFailed` on error. Stores cookies internally and within the provided session.
    *   `search(...)`: Performs metadata search. Returns a `SearchPaginator`.
    *   `full_text_search(...)`: Performs full-text search within books. Returns a `SearchPaginator`.
    *   `get_by_id(id)`: Fetches book details directly using the Z-Library book ID (e.g., `'123456/abcdef'`). Returns a dictionary similar to `item.fetch()`.
    *   `logout()`: Clears internal cookie storage.
    *   `profile`: An instance of `ZlibProfile` available after successful login.
*   **`zlibrary.SearchPaginator`**: Handles pagination for search results.
    *   `next()`: Fetches the next page of results. Returns a list of `BookItem` dictionaries.
    *   `prev()`: Fetches the previous page of results.
    *   `result`: Accesses the cached list of results for the current page.
*   **`zlibrary.BookItem` (Dictionary)**: Represents a book in search results. It's essentially a dictionary.
    *   `fetch()`: Asynchronous method called *on a result item* to retrieve the full book details, including the `download_url`. Returns a dictionary.
    *   Keys (Common): `'id'`, `'name'`, `'authors'`, `'year'`, `'extension'`, `'url'`, `'cover'`, etc. (See README example for more).
*   **`zlibrary.ZlibProfile`**: Accessed via `lib.profile` after login.
    *   `get_limits()`: Returns a dictionary with download limit information (`daily_amount`, `daily_allowed`, `daily_remaining`, `daily_reset`).
    *   `download_history()`: Returns a `DownloadsPaginator` for browsing download history.
    *   `search_public_booklists(...)`: Returns a `Booklists` paginator for public booklists.
    *   `search_private_booklists(...)`: Returns a `Booklists` paginator for the user's private booklists.
*   **`zlibrary.const.Language` (Enum)**: Defines language codes (e.g., `Language.ENGLISH`, `Language.FRENCH`). Use in `search` `lang` list.
*   **`zlibrary.const.Extension` (Enum)**: Defines file extension codes (e.g., `Extension.EPUB`, `Extension.PDF`). Use in `search` `extensions` list.
*   **`zlibrary.const.OrderOptions` (Enum)**: Defines search result ordering (e.g., `OrderOptions.POPULAR`, `OrderOptions.NEWEST`). Use in `search` `order` parameter.
*   **`zlibrary.exception`**: Contains specific exceptions like `LoginFailed`, `EmptyQueryError`, `NoProfileError`, `ParseError`.

## Configuration

*   **Tor/Onion:** Initialize with `onion=True` and `proxy_list=['socks5://127.0.0.1:9050']` (or your Tor proxy address). Requires a running Tor service.
*   **Proxies:** Provide a list of proxy URLs to `proxy_list` during initialization for non-Tor proxy usage.
*   **Logging:** Enable debug logging as shown in the README/example:
    ```python
    import logging
    logging.getLogger("zlibrary").addHandler(logging.StreamHandler())
    logging.getLogger("zlibrary").setLevel(logging.DEBUG)
    ```

## Notes

*   The library relies heavily on parsing HTML, making it vulnerable to website changes.
*   Downloading requires manually using the `download_url` obtained from `item.fetch()` or `get_by_id()` with an HTTP client (like `aiohttp`) using the same session/cookies established during login.
*   Error handling around network requests and parsing is recommended.