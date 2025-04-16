import os
import argparse
import asyncio
import aiohttp
from dotenv import load_dotenv
import zlibrary # Correct import based on README
import logging
import sys

# Configure logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# Enable zlibrary debug logging as per README
logging.getLogger("zlibrary").addHandler(logging.StreamHandler())
logging.getLogger("zlibrary").setLevel(logging.DEBUG)
# Configure root logger as well
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', stream=sys.stdout)


# Load environment variables from .env file
load_dotenv()

ZLIBRARY_EMAIL = os.getenv("ZLIBRARY_EMAIL")
ZLIBRARY_PASSWORD = os.getenv("ZLIBRARY_PASSWORD")

async def search_books(lib: zlibrary.AsyncZlib, query: str):
    """Searches Z-Library for books matching the query."""
    logging.info(f"Searching for query: '{query}'")
    try:
        # Search with filters for EPUB extension and English language
        paginator = await lib.search( # Corrected parameter names based on source code
            q=query,
            count=20,  # Limit results for better presentation (using 'count' now)
            # Removed 'order' as it's not in the source signature
            from_year=None, # Corrected parameter name
            to_year=None,   # Corrected parameter name
            extensions=[zlibrary.Extension.EPUB], # Parameter name is correct
            lang=[zlibrary.Language.ENGLISH] # Corrected parameter name
        )
        # Fetch the first page of results
        results = await paginator.next()
        logging.info(f"Found {len(results)} potential EPUB results on the first page.")
        return results, paginator # Return paginator for potential future use if needed
    except Exception as e:
        logging.error(f"Error during search: {e}", exc_info=True)
        return [], None

async def download_book(session: aiohttp.ClientSession, download_url: str, output_path: str):
    """Downloads the EPUB file from the given URL using the existing session."""
    logging.info(f"Attempting to download from: {download_url}")
    try:
        # Use the same session that lib.login() used, which should have cookies
        async with session.get(download_url, allow_redirects=True) as response:
            response.raise_for_status()  # Raise an exception for bad status codes
            if response.status == 200:
                # Ensure output directory exists
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                with open(output_path, 'wb') as f:
                    while True:
                        chunk = await response.content.read(8192) # Read in chunks
                        if not chunk:
                            break
                        f.write(chunk)
                logging.info(f"Successfully downloaded EPUB to: {output_path}")
                return True
            else:
                logging.error(f"Download failed with status code: {response.status}")
                logging.debug(f"Response headers: {response.headers}")
                logging.debug(f"Response text (first 500 chars): {(await response.text())[:500]}")
                return False
    except aiohttp.ClientResponseError as e:
        logging.error(f"HTTP error during download: {e.status} {e.message}")
        logging.debug(f"Response headers: {e.headers}")
        return False
    except aiohttp.ClientError as e:
        logging.error(f"Network error during download: {e}")
        return False
    except OSError as e:
        logging.error(f"File system error saving download: {e}")
        return False
    except Exception as e:
        logging.error(f"An unexpected error occurred during download: {e}", exc_info=True)
        return False

async def main():
    """Main function to handle CLI arguments, search, selection, and download."""
    parser = argparse.ArgumentParser(description="Search Z-Library and download EPUB files.")
    parser.add_argument("-q", "--query", required=True, help="Search query for the book.")
    parser.add_argument("-o", "--output-dir", default="library/source-epubs/", help="Directory to save downloaded EPUBs.")

    args = parser.parse_args()

    if not ZLIBRARY_EMAIL or not ZLIBRARY_PASSWORD:
        logging.error("ZLIBRARY_EMAIL and ZLIBRARY_PASSWORD must be set in the .env file.")
        sys.exit(1)

    # Use aiohttp ClientSession to manage cookies across requests
    # The zlibrary client will use this session internally
    async with aiohttp.ClientSession() as session:
        # Pass the session to the client
        lib = zlibrary.AsyncZlib() # Correct instantiation - removed session

        try:
            logging.info("Attempting to log in...")
            await lib.login(ZLIBRARY_EMAIL, ZLIBRARY_PASSWORD) # Explicit login
            logging.info("Login successful.")
        except Exception as e:
            logging.error(f"Login failed: {e}", exc_info=True)
            sys.exit(1)

        results, _ = await search_books(lib, args.query) # Ignore paginator for now

        if not results:
            logging.warning("No EPUB results found for your query.")
            sys.exit(0)

        print("\nSearch Results (EPUBs only):")
        print("-" * 30)
        for i, book_item in enumerate(results):
            # Display relevant book information using dictionary access from README example
            title = book_item.get('name', 'N/A')
            # Authors are provided as a list of strings by the library
            authors_list = book_item.get('authors', [])
            author_str = ", ".join(authors_list) if authors_list else 'N/A' # Correctly join list of strings
            year = book_item.get('year', 'N/A')
            ext = book_item.get('extension', 'N/A')
            print(f"{i+1}. {title} - {author_str} ({year}) [{ext}]")

        print("-" * 30)

        selected_book_item = None
        while True:
            try:
                selection = input("Enter the number of the book to download (or 'q' to quit): ")
                if selection.lower() == 'q':
                    logging.info("Exiting without download.")
                    sys.exit(0)
                index = int(selection) - 1
                if 0 <= index < len(results):
                    selected_book_item = results[index] # This is the item from the search result list
                    break
                else:
                    print("Invalid selection. Please enter a number from the list.")
            except ValueError:
                print("Invalid input. Please enter a number or 'q'.")

        logging.info(f"Selected: {selected_book_item.get('name', 'N/A')}")

        try:
            logging.info("Fetching book details to get download URL...")
            # Fetch full details using the item from search results, as per README
            # The search result item itself seems to have the .fetch() method
            book_details = await selected_book_item.fetch()

            download_url = book_details.get('download_url')

            if not download_url:
                logging.error("Could not retrieve download URL from book details.")
                logging.debug(f"Book details received: {book_details}")
                sys.exit(1)

            # Construct a safe filename
            filename_base = "".join(c if c.isalnum() or c in (' ', '_', '-') else '_' for c in book_details.get('name', 'unknown_book'))
            filename = f"{filename_base}.epub"
            output_path = os.path.join(args.output_dir, filename)

            # Download using the same session used for login
            success = await download_book(session, download_url, output_path)

            if success:
                logging.info("Download process completed.")
                print(f"EPUB saved to: {output_path}") # Print path for potential scripting use
            else:
                logging.error("Download process failed.")
                sys.exit(1)

        except Exception as e:
            logging.error(f"Error during download preparation or execution: {e}", exc_info=True)
            sys.exit(1)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Process interrupted by user.")
        sys.exit(0)