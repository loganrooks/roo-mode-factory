# Specification Writer Specific Memory

## Functional Requirements
<!-- Append new requirements using the format below -->

## System Constraints
<!-- Append new constraints using the format below -->

## Edge Cases
<!-- Append new edge cases using the format below -->

## Pseudocode Library
<!-- Append new pseudocode blocks using the format below -->
### Pseudocode: RAG Ingestion Pipeline - Main Function
- Created: 2025-04-10 13:04:52
- Updated: 2025-04-10 13:04:52
```pseudocode
// Main Pipeline Function
// Provides the primary interface for agent integration.
FUNCTION process_epub_to_rag_markdown(epub_path, output_dir)
    // TDD Anchor: Test with valid epub_path and output_dir
    // TDD Anchor: Test with non-existent epub_path (expect FileNotFoundError)
    // TDD Anchor: Test with non-writable output_dir (expect PermissionError or similar)
    // TDD Anchor: Test integration: ensure output file contains formatted ToC and cleaned content

    LOG "Starting RAG ingestion for: {epub_path}"

    VALIDATE input epub_path exists ELSE RAISE FileNotFoundError
    VALIDATE output_dir is writable ELSE RAISE PermissionError // Or similar OS error

    TRY
        // 1. Process EPUB (using EbookLib)
        LOG "Step 1: Processing EPUB structure and content..."
        toc_structure, html_content_list = process_epub(epub_path)
        // TDD Anchor: Test process_epub returns expected toc_structure (list/dict) and html_content_list (list of strings) for a known EPUB
        // TDD Anchor: Test process_epub handles EPUBs with/without ToC gracefully (empty toc_structure)
        // TDD Anchor: Test process_epub raises EpubProcessingError for a known invalid/corrupt EPUB

        // 2. Convert HTML to Markdown (using Pandoc via subprocess)
        LOG "Step 2: Converting extracted HTML to Markdown via Pandoc..."
        raw_markdown = convert_html_to_markdown(html_content_list)
        // TDD Anchor: Test convert_html_to_markdown returns a non-empty string for valid HTML input
        // TDD Anchor: Test convert_html_to_markdown handles empty html_content_list (returns empty string)
        // TDD Anchor: Test convert_html_to_markdown raises PandocNotFoundError if pandoc command is invalid/not found

        // 3. Clean Markdown (using Python Regex)
        LOG "Step 3: Cleaning Markdown for RAG optimization..."
        cleaned_markdown = clean_markdown(raw_markdown)
        // TDD Anchor: Test clean_markdown removes all target artifacts (![](), {#...}, [^...], [^...]:, Figure refs) from sample Markdown
        // TDD Anchor: Test clean_markdown correctly normalizes multiple newlines and trims whitespace

        // 4. Format Output (Combine ToC & Content)
        LOG "Step 4: Formatting ToC and combining with cleaned content..."
        final_markdown = format_output(toc_structure, cleaned_markdown)
        // TDD Anchor: Test format_output correctly prepends a formatted Markdown ToC list
        // TDD Anchor: Test format_output includes a separator '---' between ToC and content
        // TDD Anchor: Test format_output handles empty toc_structure (includes \"No ToC\" message)
        // TDD Anchor: Test format_output handles empty cleaned_markdown (outputs only ToC section)

        // 5. Save Output File
        LOG "Step 5: Saving final RAG-optimized Markdown..."
        output_filename = generate_output_filename(epub_path, output_dir)
        save_markdown(final_markdown, output_filename)
        // TDD Anchor: Test save_markdown creates the file at the expected path with '.rag.md' extension
        // TDD Anchor: Test content of saved file matches final_markdown exactly

        LOG "Successfully completed RAG ingestion. Output: {output_filename}"
        RETURN output_filename

    CATCH FileNotFoundError as e
        LOG error \"Input EPUB not found: {epub_path}\"
        RAISE e // Re-raise for agent handling
    CATCH PandocNotFoundError as e
        LOG error \"Pandoc command not found. Please ensure it's installed and in PATH.\"
        RAISE e // Re-raise for agent handling
    CATCH EpubProcessingError as e
        LOG error \"Error processing EPUB {epub_path}: {e}\"
        RAISE e // Re-raise for agent handling
    CATCH PermissionError as e
        LOG error \"Permission denied writing to output directory: {output_dir}\"
        RAISE e // Re-raise for agent handling
    CATCH Exception as e // Generic catch for other potential errors
        LOG error \"Unexpected error during RAG ingestion for {epub_path}: {e}\"
        // Wrap unexpected errors for consistent handling
        RAISE EpubProcessingError(\"Unexpected processing error: {e}\")
END FUNCTION
```
#### TDD Anchors:
- Test `process_epub_to_rag_markdown` with valid inputs.
- Test `process_epub_to_rag_markdown` with non-existent input file.
- Test `process_epub_to_rag_markdown` with non-writable output directory.
- Test `process_epub_to_rag_markdown` end-to-end integration (output file content).
- Test `process_epub` returns correct ToC structure and HTML list.
- Test `process_epub` handles EPUBs with and without ToC.
- Test `process_epub` raises error for invalid EPUB.
- Test `convert_html_to_markdown` returns string for valid HTML.
- Test `convert_html_to_markdown` handles empty input list.
- Test `convert_html_to_markdown` raises error if pandoc command is invalid/not found.
- Test `clean_markdown` removes all specified artifacts (`![]()`, `{#...}`, footnotes, figure refs).
- Test `clean_markdown` normalizes whitespace and newlines.
- Test `format_output` prepends formatted ToC correctly.
- Test `format_output` includes separator.
- Test `format_output` handles empty toc_structure (includes \"No ToC\" message).
- Test `format_output` handles empty cleaned_markdown (outputs only ToC section).
- Test `save_markdown` creates file at correct path.
- Test `save_markdown` writes correct content.

### Pseudocode: RAG Ingestion Pipeline - EPUB Processor
- Created: 2025-04-10 13:04:52
- Updated: 2025-04-10 13:04:52
```pseudocode
// Module: epub_processor
// Responsibility: Parse EPUB, extract ToC and HTML content using EbookLib.

// Import necessary libraries (ebooklib)
IMPORT ebooklib.epub

FUNCTION process_epub(epub_path)
    // TDD Anchor: Test with a known EPUB containing ToC (NCX/NavMap)
    // TDD Anchor: Test with a known EPUB without a ToC
    // TDD Anchor: Test with a known EPUB containing various content types (HTML, images)
    // TDD Anchor: Test with a non-existent path (should be caught by caller, but defensive check possible)
    // TDD Anchor: Test with a corrupted/invalid EPUB file (expect EpubProcessingError)

    TRY
        book = ebooklib.epub.read_epub(epub_path)
    CATCH Exception as e // Catch EbookLib specific errors if possible, otherwise generic
        RAISE EpubProcessingError(\"Failed to read or parse EPUB file: {epub_path}. Reason: {e}\")

    // --- Extract Table of Contents ---\
    toc_items = []
    // Try EPUB 2 NCX ToC first
    IF book.toc IS NOT EMPTY THEN
        LOG \"Extracting ToC using NCX...\"
        // EbookLib's book.toc provides a nested structure of EpubNcx and Link objects
        // Need a helper function to flatten/traverse this structure
        toc_items = _parse_toc_recursive(book.toc)
    ELSE // Try EPUB 3 NavMap (often within an XHTML file marked as 'nav')
        nav_item = book.get_item_with_href('nav.xhtml') // Common name, might need checking properties
        IF nav_item IS NOT NULL THEN
            LOG "Extracting ToC using NavMap (nav.xhtml)..."
            // Requires parsing the HTML of the nav_item to find the <nav type="toc"> element
            // This is more complex and might need an HTML parser like BeautifulSoup
            // toc_items = _parse_navmap_html(nav_item.get_content())
            LOG warning "EPUB 3 NavMap parsing not fully implemented in pseudocode."
            // For now, return empty if only NavMap exists and parsing isn't implemented
        ELSE
            LOG warning "No recognizable ToC (NCX or NavMap) found in EPUB."

    // --- Extract HTML Content ---
    html_content_list = []
    // Iterate through items in the spine order for correct content sequence
    spine_items = book.spine
    IF NOT spine_items:
        LOG warning "EPUB spine is empty or missing. Content order might be incorrect."
        // Fallback: iterate all documents? Might include non-content like cover, toc.xhtml
        items_to_process = book.get_items_of_type(ebooklib.ITEM_DOCUMENT)
    ELSE:
        # Get actual item objects from spine IDs
        items_to_process = [book.get_item_with_id(item_id) for item_id, _ in spine_items]


    FOR item IN items_to_process:
        IF item IS NOT NULL AND item.get_type() == ebooklib.ITEM_DOCUMENT:
            TRY
                // Decode content bytes to string, handling potential encoding issues
                content_str = item.get_content().decode('utf-8', errors='ignore')
                html_content_list.append(content_str)
            CATCH Exception as e:
                LOG error "Failed to decode content for item {item.file_name}: {e}"
                // Decide: skip item or raise error? Skipping for robustness.
                CONTINUE
        ELSE IF item IS NULL:
             LOG warning "Item ID found in spine does not exist in EPUB manifest."


    IF NOT html_content_list:
        LOG warning "No HTML content extracted from EPUB."
        // Consider raising an error if no content is critical

    RETURN toc_items, html_content_list

// --- Helper for ToC Parsing (Example for NCX) ---
FUNCTION _parse_toc_recursive(toc_nodes, level = 1)
    items = []
    FOR node IN toc_nodes:
        IF isinstance(node, ebooklib.epub.Link):
            items.append({'level': level, 'title': node.title, 'href': node.href})
        // If node is a tuple, it might contain nested nodes (EbookLib structure)
        ELSE IF isinstance(node, tuple) AND len(node) == 2 AND isinstance(node[1], list):
             section_title = node[0].title if hasattr(node[0], 'title') else "Section" # Handle potential section wrapper without title
             items.append({'level': level, 'title': section_title, 'href': node[0].href if hasattr(node[0], 'href') else None}) # Add section itself
             items.extend(_parse_toc_recursive(node[1], level + 1)) # Recurse into children
    RETURN items

// FUNCTION _parse_navmap_html(html_content) // Placeholder for EPUB 3 NavMap parsing
//    IMPORT BeautifulSoup // Example dependency
//    soup = BeautifulSoup(html_content, 'html.parser')
//    nav_element = soup.find('nav', attrs={'epub:type': 'toc'})
//    IF nav_element:
//        // Traverse the nested <li> and <a> tags within the <ol>
//        // Extract title and href, determine level based on nesting
//        RETURN parsed_items
//    RETURN []

```
#### TDD Anchors:
- Test `process_epub` with EPUB 2 (NCX ToC).
- Test `process_epub` with EPUB 3 (NavMap ToC) - *requires NavMap parsing implementation*.
- Test `process_epub` with EPUB having no ToC.
- Test `process_epub` extracts HTML content in spine order.
- Test `process_epub` handles missing spine items gracefully.
- Test `process_epub` handles content decoding errors.
- Test `process_epub` raises `EpubProcessingError` for invalid EPUB files.
- Test `_parse_toc_recursive` correctly flattens nested NCX structure with levels.

### Pseudocode: RAG Ingestion Pipeline - Markdown Converter
- Created: 2025-04-10 13:04:52
- Updated: 2025-04-10 13:04:52
```pseudocode
// Module: markdown_converter
// Responsibility: Convert a list of HTML strings to a single Markdown string using Pandoc.

// Import necessary libraries
IMPORT subprocess
IMPORT shutil // To check for command existence

// Define custom exception
CLASS PandocNotFoundError inherits Exception

FUNCTION convert_html_to_markdown(html_content_list)
    // TDD Anchor: Test with a list containing valid HTML strings.
    // TDD Anchor: Test with an empty list (expect empty string).
    // TDD Anchor: Test with HTML containing elements Pandoc should convert (headers, lists, bold, etc.).
    // TDD Anchor: Test behavior when pandoc command is not found (expect PandocNotFoundError).
    // TDD Anchor: Test behavior when pandoc fails (e.g., invalid input, though less likely for HTML) (expect EpubProcessingError).

    IF NOT html_content_list:
        RETURN ""

    // Check if pandoc command exists in PATH
    IF shutil.which("pandoc") IS NULL:
        RAISE PandocNotFoundError("Pandoc command not found in system PATH.")

    // Combine HTML content - consider adding separators if needed, but pandoc might handle structure.
    // Simple concatenation might be sufficient if EPUB structure implies document flow.
    combined_html = "\n".join(html_content_list)

    // Define Pandoc command arguments
    // 'markdown_strict' avoids many extensions. '+pipe_tables' keeps tables. '-raw_html' passes through unknown HTML. '--wrap=none' prevents line wrapping.
    // Consider '--markdown-headings=atx' for consistent '#' headers.
    command = [
        "pandoc",
        "-f", "html",                     // Input format
        "-t", "markdown_strict+pipe_tables-raw_html", // Output format with specific extensions
        "--wrap=none",                    // Disable line wrapping
        # "--markdown-headings=atx"       # Optional: Force ATX style headers (# Header)
    ]

    TRY
        // Execute pandoc, feeding combined HTML via stdin
        process = subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True, // Work with text streams
            encoding='utf-8' // Ensure consistent encoding
        )
        stdout, stderr = process.communicate(input=combined_html)

        IF process.returncode != 0 THEN
            // Pandoc failed
            LOG error \"Pandoc conversion failed with exit code {process.returncode}. Stderr: {stderr}\"
            RAISE EpubProcessingError(f\"Pandoc conversion failed: {stderr}\")

        // Pandoc succeeded
        RETURN stdout

    CATCH FileNotFoundError:
        // This catch is technically redundant if shutil.which check passes, but good defense.
        RAISE PandocNotFoundError(\"Pandoc command not found during execution attempt.\")
    CATCH Exception as e:
        // Catch other potential subprocess errors
        LOG error \"Unexpected error during Pandoc execution: {e}\"
        RAISE EpubProcessingError(f\"Unexpected error calling Pandoc: {e}\")

END FUNCTION
```
#### TDD Anchors:
- Test `convert_html_to_markdown` with valid HTML list input.
- Test `convert_html_to_markdown` with empty list input.
- Test `convert_html_to_markdown` raises `PandocNotFoundError` if `pandoc` is not in PATH.
- Test `convert_html_to_markdown` raises `EpubProcessingError` if `pandoc` returns non-zero exit code.
- Verify output Markdown structure matches expected conversion from sample HTML.

### Pseudocode: RAG Ingestion Pipeline - Markdown Cleaner
- Created: 2025-04-10 13:04:52
- Updated: 2025-04-10 13:04:52
```pseudocode
// Module: markdown_cleaner
// Responsibility: Clean Markdown text by removing unwanted elements and normalizing whitespace.

// Import necessary libraries
IMPORT re // For regular expressions

FUNCTION clean_markdown(markdown_text)
    // TDD Anchor: Test removal of various image formats (![...](...))
    // TDD Anchor: Test removal of inline links ([...](...)) - should keep link text
    // TDD Anchor: Test removal of reference links ([...][...]) - should keep link text
    // TDD Anchor: Test removal of footnote definitions ([^...]: ...)
    // TDD Anchor: Test removal of footnote markers ([^...])
    // TDD Anchor: Test removal of HTML tags (<...> and </...>)
    // TDD Anchor: Test normalization of multiple newlines to single newlines
    // TDD Anchor: Test trimming of leading/trailing whitespace from each line
    // TDD Anchor: Test handling of empty input string (should return empty string)

    IF markdown_text IS NULL THEN
        RETURN ""
    END IF

    // 1. Remove image tags: ![alt text](path/to/image.jpg)
    // This regex targets the whole image tag structure.
    markdown_text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", markdown_text)

    // 2. Remove footnote definitions: [^...]: ...
    // This targets lines starting with [^...] followed by a colon.
    markdown_text = re.sub(r"^\s*\[\^[^\]]+\]:.*$", "", markdown_text, flags=re.MULTILINE)

    // 3. Remove footnote markers: [^...]
    // This targets the marker itself, potentially leaving brackets if used for other purposes.
    // A more robust approach might involve context-aware parsing.
    markdown_text = re.sub(r"\[\^[^\]]+\]", "", markdown_text)

    // 4. Remove inline links, keeping the link text: [text](url) -> text
    // This uses capturing groups to keep the text part.
    markdown_text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", markdown_text)

    // 5. Remove reference links, keeping the link text: [text][label] -> text
    // This also uses capturing groups.
    markdown_text = re.sub(r"\[([^\]]+)\]\[[^\]]*\]", r"\1", markdown_text)

    // 6. Remove HTML tags: <tag> and </tag>
    // This removes opening and closing tags, including self-closing ones.
    markdown_text = re.sub(r"<[^>]+>", "", markdown_text)

    // 7. Normalize multiple newlines to single newlines
    // Replace sequences of 2 or more newlines with exactly two newlines (paragraph break).
    markdown_text = re.sub(r"\n{2,}", "\n\n", markdown_text)
    // Replace sequences of 3 or more newlines (often used for spacing) with two.
    markdown_text = re.sub(r"\n{3,}", "\n\n", markdown_text)


    // 8. Trim leading/trailing whitespace from each line
    lines = markdown_text.split('\n')
    lines = [line.strip() for line in lines]
    markdown_text = '\n'.join(lines)

    // 9. Remove leading/trailing whitespace from the entire text
    markdown_text = markdown_text.strip()

    RETURN markdown_text

END FUNCTION
```
#### TDD Anchors:
- Test `clean_markdown` removes image tags (`![]()`).
- Test `clean_markdown` removes footnote definitions (`[^...]:`).
- Test `clean_markdown` removes footnote markers (`[^...]`).
- Test `clean_markdown` removes inline links (`[]()`) but keeps link text.
- Test `clean_markdown` removes reference links (`[][]`) but keeps link text.
- Test `clean_markdown` removes HTML tags (`<>`).
- Test `clean_markdown` normalizes multiple newlines to double newlines.
- Test `clean_markdown` trims leading/trailing whitespace from each line.
- Test `clean_markdown` handles empty input string.

### Pseudocode: RAG Ingestion Pipeline - Output Formatter
- Created: 2025-04-10 13:04:52
- Updated: 2025-04-10 13:04:52
```pseudocode
// Module: output_formatter
// Responsibility: Format the ToC and combine it with cleaned Markdown content.

// Import necessary libraries
IMPORT re
IMPORT os // For path manipulation if needed for anchors

FUNCTION format_output(toc_structure, cleaned_markdown)
    // TDD Anchor: Test with a valid toc_structure (list of dicts with level, title, href).
    // TDD Anchor: Test with an empty toc_structure (should produce only content).
    // TDD Anchor: Test with valid cleaned_markdown.
    // TDD Anchor: Test with empty cleaned_markdown (should produce only ToC).
    // TDD Anchor: Test output contains \"# Table of Contents\" header if toc_structure is not empty.
    // TDD Anchor: Test output contains '---' separator if both ToC and content exist.
    // TDD Anchor: Test ToC items are formatted as Markdown list with correct indentation.
    // TDD Anchor: Test basic anchor link generation (e.g., spaces to hyphens, lowercase).

    formatted_toc = \"\"
    IF toc_structure IS NOT EMPTY THEN
        formatted_toc = "# Table of Contents\n\n"
        FOR item IN toc_structure:
            level = item.get('level', 1)
            title = item.get('title', 'Untitled')
            href = item.get('href', '') // Original href from EPUB

            // Basic indentation based on level (assuming level 1 is top)
            indent = \"  \" * (level - 1)

            // Basic anchor generation from title (simple, may need refinement)
            // Remove non-alphanumeric, replace space with hyphen, lowercase
            IF title:
                 anchor_base = re.sub(r'[^\\w\\s-]', '', title.lower()) # Remove unwanted chars
                 anchor = re.sub(r'\\s+', '-', anchor_base).strip('-') # Replace space with hyphen
            ELSE:
                 anchor = \"untitled-section\"


            // Create Markdown list item
            // Note: Linking directly using generated anchor '#{anchor}'
            formatted_toc += f"{indent}*   [{title}](#{anchor})\n"

    // --- Combine ToC and Content ---
    LOG \"Combining formatted ToC and cleaned content.\"
    final_markdown = \"\"
    IF formatted_toc AND cleaned_markdown:
        final_markdown = formatted_toc + "\n---\n\n" + cleaned_markdown.strip()
    ELSE IF formatted_toc: // Only ToC exists
        final_markdown = formatted_toc.strip()
    ELSE IF cleaned_markdown: // Only content exists
        final_markdown = cleaned_markdown.strip()
    // If both are empty, final_markdown remains ""

    RETURN final_markdown.strip() // Return final combined string

END FUNCTION

// --- Custom Exceptions (defined once, used across modules) ---
CLASS PandocNotFoundError inherits Exception
CLASS EpubProcessingError inherits Exception

```
#### TDD Anchors:
- Test `format_output` with a valid `toc_structure` and `cleaned_markdown`.
- Test `format_output` with an empty `toc_structure` and valid `cleaned_markdown`.
- Test `format_output` with a valid `toc_structure` and empty `cleaned_markdown`.
- Test `format_output` with both `toc_structure` and `cleaned_markdown` being empty.
- Verify output starts with `# Table of Contents` only when `toc_structure` is not empty.
- Verify output includes `---` separator only when both `toc_structure` and `cleaned_markdown` are present.
- Verify ToC list items use `*   ` and correct indentation.
- Verify basic anchor link generation (`[Title](#title-anchor)`).

### Pseudocode: RAG Ingestion Pipeline - Utility Functions
- Created: 2025-04-10 13:04:52
- Updated: 2025-04-10 13:04:52
```pseudocode
// Module: utilities
// Responsibility: Helper functions for file naming and saving.

// Import necessary libraries
IMPORT os
IMPORT re // For filename sanitization

FUNCTION generate_output_filename(epub_path, output_dir)
    // TDD Anchor: Test with standard epub path.
    // TDD Anchor: Test with path containing spaces or special characters.
    // TDD Anchor: Test output includes '.rag.md' suffix.
    // TDD Anchor: Test output filename is sanitized (e.g., no invalid chars).

    // Get the base name of the EPUB file without extension
    base_name = os.path.splitext(os.path.basename(epub_path))[0]

    // Sanitize the base name to create a valid filename
    # Remove potentially problematic characters (allow alphanumeric, underscore, hyphen)
    safe_base_name = re.sub(r'[^\w\-_\.]', '_', base_name)
    # Ensure it doesn't start/end with problematic chars like periods or spaces
    safe_base_name = safe_base_name.strip('._ ')

    // Handle empty filename after sanitization
    IF NOT safe_base_name:
        safe_base_name = "default_output"

    // Construct the output filename with .rag.md suffix
    output_filename = os.path.join(output_dir, f\"{safe_base_name}.rag.md\")
    RETURN output_filename
END FUNCTION

FUNCTION save_markdown(markdown_content, output_filename)
    // TDD Anchor: Test saving content to a file.
    // TDD Anchor: Test directory creation if it doesn't exist.
    // TDD Anchor: Test file overwriting behavior.
    // TDD Anchor: Test correct UTF-8 encoding is used.
    // TDD Anchor: Test error handling for permission issues (caught by caller).

    TRY
        // Ensure the output directory exists
        output_dir = os.path.dirname(output_filename)
        // Handle potential empty output_dir (e.g., if filename has no path)
        IF output_dir:
             os.makedirs(output_dir, exist_ok=True) // Creates dir only if it doesn't exist

        // Write the content to the file using UTF-8 encoding
        WITH open(output_filename, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        LOG \"Markdown content successfully saved to: {output_filename}\"

    CATCH IOError as e:
        LOG error \"Failed to write output file: {output_filename}. Reason: {e}\"
        // Re-raise as a processing error or let the caller handle specific IOErrors
        RAISE EpubProcessingError(f\"Failed to write output file: {e}\")
    CATCH Exception as e:
        LOG error \"Unexpected error during file save: {e}\"
        RAISE EpubProcessingError(f\"Unexpected error saving file: {e}\")

END FUNCTION

// --- Custom Exceptions (defined once, used across modules) ---
CLASS PandocNotFoundError inherits Exception
CLASS EpubProcessingError inherits Exception

```
#### TDD Anchors:
- Test `generate_output_filename` produces correct `*.rag.md` path.
- Test `generate_output_filename` sanitizes filenames with invalid characters.
- Test `generate_output_filename` handles empty base names after sanitization.
- Test `save_markdown` creates the directory if needed.
- Test `save_markdown` writes the exact content provided.
- Test `save_markdown` uses UTF-8 encoding (verify by reading back).
- Test `save_markdown` raises `EpubProcessingError` for permission issues.
- Test `save_markdown` raises `EpubProcessingError` for other IO errors.
