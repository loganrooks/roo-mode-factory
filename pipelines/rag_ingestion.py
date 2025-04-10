import os
import logging
import pypandoc
from typing import List, Tuple, Dict, Optional
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import re # Import re here

# --- Logging Setup ---
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG) # Set level to DEBUG for detailed output
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# Add a handler to output to console for debugging purposes
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
# Prevent adding handler multiple times if script is reloaded/run multiple times in same session
if not log.handlers:
    log.addHandler(console_handler)

# --- Custom Exception ---
class EpubProcessingError(Exception):
    """Custom exception for errors during EPUB processing."""
    pass

# --- HTML Parsing (using BeautifulSoup) ---

def _parse_toc_recursive(toc_items: List[epub.Link | epub.Section], level: int = 1) -> List[Dict]:
    """
    Recursively parses the ToC structure from ebooklib's toc attribute.

    Args:
        toc_items: A list of ebooklib Link or Section objects.
        level: The current nesting level (used for indentation).

    Returns:
        A list of dictionaries, each representing a ToC item with 'title' and 'level'.
    """
    parsed_toc = []
    for item in toc_items:
        if isinstance(item, epub.Link):
            parsed_toc.append({'title': item.title, 'level': level})
        elif isinstance(item, epub.Section):
            # Process the section title if it exists
            if item.title:
                parsed_toc.append({'title': item.title, 'level': level})
            # Recursively process subsections
            parsed_toc.extend(_parse_toc_recursive(item.children, level + 1))
    return parsed_toc

def _parse_navmap_html(html_content: str) -> List[Dict]:
    """
    Parses the ToC structure from an EPUB 3 NavMap HTML content.

    Args:
        html_content: The HTML content of the NavMap file.

    Returns:
        A list of dictionaries, each representing a ToC item with 'title' and 'level'.
        Returns an empty list if BeautifulSoup is not available or parsing fails.
    """
    if BeautifulSoup is None:
        log.warning("BeautifulSoup library not found. Cannot parse EPUB 3 NavMap.")
        return []

    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        nav_element = soup.find('nav', attrs={'epub:type': 'toc'})
        if not nav_element:
            log.warning("Could not find <nav epub:type='toc'> element in NavMap HTML.")
            return []

        # Find the main ordered list (usually the root of the ToC)
        root_ol = nav_element.find('ol')
        if not root_ol:
            log.warning("Could not find root <ol> element within the NavMap.")
            return []

        return _parse_navmap_list(root_ol)

    except Exception as e:
        log.error(f"Error parsing NavMap HTML with BeautifulSoup: {e}")
        return []

def _parse_navmap_list(ol_element: BeautifulSoup, level: int = 1) -> List[Dict]:
    """
    Recursively parses list items within a NavMap <ol> element.

    Args:
        ol_element: The BeautifulSoup <ol> element to parse.
        level: The current nesting level.

    Returns:
        A list of dictionaries representing ToC items.
    """
    parsed_toc = []
    for li in ol_element.find_all('li', recursive=False): # Only direct children
        a_tag = li.find('a', recursive=False)
        if a_tag and a_tag.string:
            parsed_toc.append({'title': a_tag.string.strip(), 'level': level})

        # Check for nested <ol> for recursion
        nested_ol = li.find('ol', recursive=False)
        if nested_ol:
            parsed_toc.extend(_parse_navmap_list(nested_ol, level + 1))
    return parsed_toc


# --- EPUB Processing (using EbookLib) ---

def process_epub(epub_path: str) -> Tuple[List[Dict], List[str]]:
    """
    Parses an EPUB file using EbookLib to extract ToC structure and HTML content.

    Args:
        epub_path: Path to the input EPUB file.

    Returns:
        A tuple containing:
        - toc_items: A list of dictionaries representing the ToC structure.
        - html_content_list: A list of strings, each containing HTML content from the EPUB spine.

    Raises:
        EpubProcessingError: If the EPUB file cannot be read or parsed.
    """
    if epub is None:
        raise EpubProcessingError("ebooklib library is not available.")

    try:
        log.info(f"Reading EPUB: {epub_path}")
        book = epub.read_epub(epub_path)
        # --- DEBUG: Print all item IDs and filenames ---
        log.debug("--- DEBUG: Items in EPUB manifest ---")
        for item in book.items:
            log.debug(f"  ID: {item.id}, FileName: {item.file_name}, Type: {item.media_type}")
        log.debug("--- END DEBUG ---")
    except Exception as e:
        raise EpubProcessingError(f"Failed to read or parse EPUB file: {epub_path}. Reason: {e}")

    # --- Extract Table of Contents ---
    toc_items = []
    nav_doc_id = None # Initialize nav_doc_id
    if book.toc:
        log.info("Extracting ToC using NCX...")
        # Try to get the NCX item ID
        ncx_item = book.get_item_with_id('ncx')
        if ncx_item:
            nav_doc_id = ncx_item.id # Store the NCX item's ID
        toc_items = _parse_toc_recursive(book.toc)
    else:
        # Try to find the Nav document in EPUB 3
        nav_items = book.get_items_by_type(ebooklib.ITEM_NAVIGATION)
        if nav_items:
            nav_doc_id = nav_items[0].id # Store the nav document ID
            log.info("Found EPUB 3 NavMap item(s). Attempting to parse...")
            # Assuming the first nav item is the primary ToC
            nav_item = nav_items[0]
            try:
                nav_html_content = nav_item.get_content().decode('utf-8', errors='ignore')
                toc_items = _parse_navmap_html(nav_html_content)
                if not toc_items:
                     log.warning("EPUB 3 NavMap parsing yielded no ToC items.")
            except Exception as e:
                log.error(f"Failed to decode or parse NavMap content from {nav_item.file_name}: {e}")
        else:
            log.warning("No recognizable ToC (NCX or NavMap) found in EPUB.")

    # --- Extract HTML Content ---
    html_content_list = []
    items_to_process = []

    # Use spine order if available
    if book.spine:
        log.info("Processing content based on EPUB spine order.")
        item_map = {item.id: item for item in book.get_items()} # Rebuild item map based on IDs
        for spine_entry in book.spine: # Iterate through entries directly
            item_id = None
            if isinstance(spine_entry, tuple): # Handle tuple format (id, linear)
                item_id = spine_entry[0]
            elif isinstance(spine_entry, str): # Handle string format (just id)
                item_id = spine_entry
            else:
                log.warning(f"Unexpected entry type in spine: {spine_entry}")
                continue

            if item_id is None:
                log.warning(f"Could not determine item ID from spine entry: {spine_entry}")
                continue

            item = item_map.get(item_id) # Use dictionary lookup by ID

            if item:
                 # Check if the item is the navigation document; if so, skip it
                 if item.id == nav_doc_id:
                      log.debug(f"Skipping navigation document: {item.file_name}")
                      continue
                 # If it's not the nav doc, add it for processing
                 items_to_process.append(item)
            else:
                 # This warning should now only appear if the ID genuinely isn't in the manifest
                 log.warning(f"Item with ID '{item_id}' found in spine but not in EPUB manifest (using item_map).")
    else:
        log.warning("EPUB spine is empty or missing. Processing all document items.")
        # Filter out nav doc even when processing all documents
        items_to_process = [item for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT) if item.id != nav_doc_id]

    # Process the collected items
    for item in items_to_process:
        try:
            content_str = item.get_content().decode('utf-8', errors='ignore')
            html_content_list.append(content_str)
        except Exception as e:
            log.error(f"Failed to decode content for item {item.file_name}: {e}. Skipping item.")
            continue

    log.info(f"Extracted {len(toc_items)} ToC items and {len(html_content_list)} HTML content parts.")
    return toc_items, html_content_list


# --- Markdown Conversion (using Pandoc) ---

def convert_html_to_markdown(html_content_list: List[str]) -> str:
    """
    Converts a list of HTML strings to a single Markdown string using Pandoc.

    Args:
        html_content_list: A list of strings, each containing HTML content.

    Returns:
        A single string containing the combined Markdown content.

    Raises:
        EpubProcessingError: If Pandoc is not found or conversion fails.
    """
    if pypandoc is None:
        raise EpubProcessingError("pypandoc library is not available.")

    combined_html = "".join(html_content_list)

    try:
        log.info("Converting HTML to Markdown using Pandoc...")
        # Use 'gfm' (GitHub Flavored Markdown) for broad compatibility, no wrap
        markdown_content = pypandoc.convert_text(combined_html, 'gfm', format='html', extra_args=['--wrap=none'])
        log.info("Pandoc conversion successful.")
        return markdown_content
    except (OSError, RuntimeError) as e:
        # OSError is raised if pandoc is not found
        # RuntimeError might be raised by pypandoc for other conversion issues
        raise EpubProcessingError(f"Pandoc conversion failed: {e}")


# --- Markdown Cleaning ---

def clean_markdown(markdown_content: str) -> str:
    """
    Cleans the Markdown content for better RAG performance.
    Removes headers, figure references, image tags, excessive newlines, etc.

    Args:
        markdown_content: The Markdown string to clean.

    Returns:
        The cleaned Markdown string.
    """
    log.info("Starting Markdown cleaning process...")

    # Remove Pandoc header identifiers like {#_Toc12345}
    cleaned_content = re.sub(r'\s*\{#_Toc\d+\}', '', markdown_content)
    log.debug("Removed Pandoc header identifiers.")

    # Remove duplicated TOC section derived from nav.xhtml
    # Matches '## Title\n\n1. [Link](file.xhtml)\n...' structure
    cleaned_content = re.sub(r'\n*## .*\n+(\d+\.\s+\[.*?\]\(.*?\.xhtml\)\n*)+', '', cleaned_content)
    log.debug("Removed duplicated TOC section.")


    # Remove empty image links like ![]()
    cleaned_content = re.sub(r'!\[\]\(\)', '', cleaned_content)
    log.debug("Removed empty image links.")

    # Remove footnote definitions like [^1]: ...

    # Remove simulated Pandoc footnote markers like [\ref\]{.class}
    cleaned_content = re.sub(r'\\\[\\\\ref\\\\\\]\{.*?\}', '', cleaned_content) # Corrected regex attempt 4
    log.debug("Removed simulated Pandoc footnote markers.")

    cleaned_content = re.sub(r'\[\^\d+\]:.*\n?', '', cleaned_content)
    log.debug("Removed footnote definitions.")

    # Remove footnote markers like [^1]
    cleaned_content = re.sub(r'\[\^\d+\]', '', cleaned_content)
    log.debug("Removed footnote markers.")

    # Remove footnote backlink arrows
    cleaned_content = re.sub(r'↩︎', '', cleaned_content)
    log.debug("Removed footnote backlink arrows.")


    # Remove basic figure references like \[Fig \d+\] or \[Figure \d+\]
    cleaned_content = re.sub(r'\\\[(Fig|Figure)\s*\d+\\\]', '', cleaned_content)
    log.debug("Removed basic figure references.")

    # Replace <br> tags with newlines before general tag removal
    cleaned_content = re.sub(r'<br\s*/?>', '\n', cleaned_content, flags=re.IGNORECASE)
    log.debug("Replaced <br> tags with newlines.")

    # Remove remaining image tags like ![alt text](path/to/image.jpg)
    cleaned_content = re.sub(r'!\[.*?\]\(.*?\)', '', cleaned_content)
    log.debug("Removed remaining image tags.")

    # Remove basic HTML tags that might remain (e.g., <br>, <div>)
    cleaned_content = re.sub(r'<[^>]+>', '', cleaned_content)
    log.debug("Removed basic HTML tags.")

    # Normalize excessive newlines (more than two consecutive newlines)
    cleaned_content = re.sub(r'\n{3,}', '\n\n', cleaned_content)
    log.debug("Normalized excessive newlines.")

    # Trim whitespace from each line
    lines = cleaned_content.split('\n')
    cleaned_lines = [line.strip() for line in lines]
    cleaned_content = '\n'.join(cleaned_lines)
    log.debug("Trimmed whitespace from each line.")

    # Remove leading/trailing whitespace from the whole string
    cleaned_content = cleaned_content.strip()

    log.info("Markdown cleaning finished.")
    return cleaned_content


# --- Final Output Formatting ---

def format_final_output(toc_items: List[Dict], cleaned_markdown: str) -> str:
    """
    Formats the final output string including the ToC and cleaned content.

    Args:
        toc_items: A list of dictionaries representing the ToC structure.
        cleaned_markdown: The cleaned Markdown content string.

    Returns:
        The final formatted Markdown string ready for saving.
    """
    log.info("Formatting final output...")
    toc_md = "# Table of Contents\n\n"
    for item in toc_items:
        indent = "  " * (item['level'] - 1)
        toc_md += f"{indent}- {item['title']}\n"

    final_output = f"{toc_md}\n\n---\n\n{cleaned_markdown}"
    log.info("Generated Markdown ToC and combined with cleaned content.")
    return final_output


# --- Main Pipeline Function ---

def run_pipeline(epub_path: str, output_path: str) -> Optional[str]:
    """
    Runs the complete EPUB to Markdown RAG pipeline.

    Args:
        epub_path: Path to the input EPUB file.
        output_path: Full path (including filename) to save the final Markdown file.

    Returns:
        The path to the generated Markdown file, or None if an error occurred.
    """
    try:
        # Ensure output directory exists
        output_dir_path = os.path.dirname(output_path)
        os.makedirs(output_dir_path, exist_ok=True)
        log.debug(f"Ensured output directory exists: {output_dir_path}")

        # Step 1: Process EPUB to get ToC and HTML content
        toc_items, html_content_list = process_epub(epub_path)

        # Step 2: Convert HTML to Markdown
        raw_markdown = convert_html_to_markdown(html_content_list)

        # Step 3: Clean Markdown
        cleaned_markdown = clean_markdown(raw_markdown)

        # Step 4: Format Final Output
        final_output = format_final_output(toc_items, cleaned_markdown)

        # Step 5: Save Final RAG-optimized Markdown
        # Use the provided full output path directly
        output_filename = output_path

        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(final_output)

        log.info(f"Markdown content successfully saved to: {output_filename}")
        return output_filename

    except EpubProcessingError as e:
        log.error(f"EPUB processing failed: {e}")
        return None
    except Exception as e:
        # Catch any other unexpected errors during the process
        log.error(f"An unexpected error occurred: {e}", exc_info=True)
        return None

# --- Command Line Execution ---
if __name__ == '__main__':
    import argparse
    import sys

    # Setup basic config here in case script is run directly
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    log = logging.getLogger(__name__) # Ensure log is defined in this scope

    parser = argparse.ArgumentParser(description="Convert EPUB to RAG-optimized Markdown.")
    parser.add_argument("epub_path", help="Path to the input EPUB file.")
    parser.add_argument("output_path", help="Full path to save the output .rag.md file.")

    args = parser.parse_args()

    input_epub_path = args.epub_path
    output_path_arg = args.output_path

    try:
        log.info(f"Processing EPUB from CLI: {input_epub_path}")
        # Call the main pipeline function, renamed from run_pipeline for clarity
        output_file = run_pipeline(input_epub_path, output_path_arg)
        if output_file:
            log.info(f"Processing complete. Output saved to: {output_file}")
        else:
            log.error("Pipeline execution failed.")
            sys.exit(1) # Exit with error code if pipeline function returns None
    except (FileNotFoundError, EpubProcessingError, PermissionError, ValueError) as e:
        log.error(f"Processing failed: {e}")
        sys.exit(1)
    except Exception as e:
        log.exception(f"An unexpected error occurred during command line execution: {e}")
        sys.exit(1)