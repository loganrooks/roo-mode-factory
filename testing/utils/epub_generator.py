import ebooklib
from ebooklib import epub
import argparse
import os
from datetime import datetime, timezone # Import timezone
import uuid

# --- Artifact Generation Functions ---

def get_html_artifact_content():
    """Returns XHTML content containing basic HTML tags."""
    return """
    <h2>HTML Artifacts</h2>
    <p>This paragraph contains <b>bold text</b>, <i>italic text</i>, and <em>emphasized text</em>.</p>
    <div>This is a div element.</div>
    <span>This is a span element.</span>
    <p>Link: <a href="http://example.com">Example Link</a></p>
    <!-- This is an HTML comment -->
    <figure>
        <figcaption>Figure Caption</figcaption>
    </figure>
    <aside>Aside content</aside>
    <table>
        <tr><th>Header 1</th><th>Header 2</th></tr>
        <tr><td>Data 1</td><td>Data 2</td></tr>
    </table>
    """

def get_pandoc_attribute_content():
    """Returns XHTML content simulating Pandoc attributes (using comments/data attributes)."""
    return """
    <h2>Pandoc Attributes (Simulated)</h2>
    <!-- Pandoc Attr: {#header-id .section-class} -->
    <h3 id="header-id" class="section-class" data-pandoc-attrs="{#header-id .section-class}">Header with Attributes</h3>
    <p>Paragraph with an inline span <!-- Pandoc Attr: {.special} --> <span class="special" data-pandoc-attrs="{.special}">like this</span>.</p>
    <p>Link with attributes: <!-- Pandoc Attr: {#link-target .external} --> <a href="#target" id="link-target" class="external" data-pandoc-attrs="{#link-target .external}">Target Link</a></p>
    <!-- Pandoc Empty Anchor: []{#empty-anchor} -->
    <a id="empty-anchor" data-pandoc-attrs="[]{#empty-anchor}"></a>
    """

def get_pandoc_div_content(): # Added this function back as it was in the original error trace
    """Returns XHTML content simulating Pandoc fenced divs."""
    return """
    <h2>Pandoc Fenced Divs (Simulated)</h2>
    <!-- Pandoc Div: ::: note -->
    <div class="note" data-pandoc-attrs="::: note">
        <p>This is a simulated 'note' div.</p>
    </div>
    <!-- Pandoc Div: ::: {#div-id .custom-class} -->
    <div id="div-id" class="custom-class" data-pandoc-attrs="::: {#div-id .custom-class}">
        <p>This is a div with ID and class attributes.</p>
    </div>
    """

def get_footnote_content():
    """Returns XHTML content simulating footnotes."""
    return """
    <h2>Footnotes (Simulated)</h2>
    <p>Here is some text with a footnote reference<a href="#fn1" id="fnref1" role="doc-noteref"><sup>1</sup></a>. And another one<a href="#fn2" id="fnref2" role="doc-noteref"><sup>2</sup></a>.</p>
    <p>This simulates Pandoc-style markers: [\\[ref\\]]{.footnote-class}</p>

    <div class="footnotes" role="doc-endnotes">
      <hr/>
      <ol>
        <li id="fn1" role="doc-endnote">
          <p>This is the first footnote definition. <a href="#fnref1" role="doc-backlink">&#8617;</a></p>
        </li>
        <li id="fn2" role="doc-endnote">
          <p>This is the second footnote definition. <a href="#fnref2" role="doc-backlink">&#8617;</a></p>
        </li>
      </ol>
    </div>
    <!-- Pandoc Footnote Def: [^ref]: Definition -->
    <!-- Pandoc Footnote Def: \\[ref\\] Definition -->
    """

def get_misc_pandoc_content():
    """Returns XHTML content simulating other Pandoc features."""
    return """
    <h2>Miscellaneous Pandoc Features (Simulated)</h2>
    <p>This includes <sup>superscript</sup> text.</p> <!-- Pandoc: ^superscript^ -->
    <p>Inline code: <code>my_variable</code>.</p> <!-- Pandoc: `my_variable` -->
    <p>Inline code with class: <!-- Pandoc: `code`{.lang} --> <code class="lang" data-pandoc-attrs="{.lang}">code</code>.</p>
    <pre><code class="python"># Fenced code block
def hello():
    print("Hello")
    </code></pre> <!-- Pandoc: ```python -->
    <pre><code class="clojure numberLines">;; Fenced code block with attributes
(println "Hello")
    </code></pre> <!-- Pandoc: ```{.clojure .numberLines} -->
    <p>This line ends with a hard break.<br/> <!-- Pandoc: \ -->
    This is the next line.</p>
    <p>Unicode: → ≠ </p>
    <p>Email link simulation: <user@example.com></p> <!-- Pandoc: <user@example.com> -->
    <!-- Pandoc Raw Block: ```{=html} <raw>...</raw> ``` -->
    <raw>This simulates raw HTML block content</raw>
    """

def get_table_content():
    """Returns XHTML content for tables."""
    return """
    <h2>Tables</h2>
    <h3>Simple Table</h3>
    <table>
      <thead>
        <tr><th>Col A</th><th>Col B</th></tr>
      </thead>
      <tbody>
        <tr><td>Row 1, Col A</td><td>Row 1, Col B</td></tr>
        <tr><td>Row 2, Col A</td><td>Row 2, Col B</td></tr>
      </tbody>
    </table>
    <!-- Pandoc Grid Table simulation would be complex, representing as standard HTML -->
    """

# --- Main EPUB Creation Function ---

def create_epub(output_path, title="Test EPUB", author="EPUB Generator", language="en", artifacts_to_include=None, generate_spine=True):
    """
    Generates an EPUB file with specified artifacts.

    Args:
        output_path (str): Path to save the generated EPUB file.
        title (str): Title of the EPUB.
        author (str): Author of the EPUB.
        language (str): Language code (e.g., 'en').
        artifacts_to_include (list): List of artifact types (strings) to include.
                                     Valid types: 'html', 'pandoc_attrs', 'pandoc_divs',
                                                  'footnotes', 'misc_pandoc', 'tables'.
                                     If None or empty, includes a basic chapter.
    """
    book = epub.EpubBook()

    # Set metadata
    book_uuid = uuid.uuid4()
    book.set_identifier(f'urn:uuid:{book_uuid}')
    book.set_title(title)
    book.set_language(language)
    book.add_author(author)
    # Use timezone-aware datetime
    book.add_metadata('DC', 'date', datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'))
    book.add_metadata('DC', 'description', f'Test EPUB generated with artifacts: {artifacts_to_include}')

    # --- Create Chapters ---
    chapters = []
    toc_links = []

    # Chapter 1: Introduction / Basic Content
    c1_content = """<h1>Introduction</h1><p>This is a test EPUB file generated programmatically.</p>"""
    c1 = epub.EpubHtml(title='Introduction', file_name='chap_01.xhtml', lang=language, uid='chap_01') # <<< Set uid
    # Ensure chapter 1 has full HTML structure
    # Add CSS link automatically via book.add_item(nav_css) later
    c1.content = c1_content # Assign only body content
    chapters.append(c1)
    toc_links.append(epub.Link('chap_01.xhtml', 'Introduction', 'intro'))

    # Chapter 2: Artifacts
    c2_content_parts = ["<h1>Artifact Examples</h1><p>This chapter contains examples of specific artifacts.</p>"]
    artifact_map = {
        'html': get_html_artifact_content,
        'pandoc_attrs': get_pandoc_attribute_content,
        'pandoc_divs': get_pandoc_div_content, # Added back
        'footnotes': get_footnote_content,
        'misc_pandoc': get_misc_pandoc_content,
        'tables': get_table_content,
    }

    if artifacts_to_include:
        for artifact_key in artifacts_to_include:
            if artifact_key in artifact_map:
                # Wrap each artifact's content in a div
                c2_content_parts.append(f'<div class="artifact-section" id="{artifact_key}">')
                c2_content_parts.append(artifact_map[artifact_key]())
                c2_content_parts.append('</div>')
            else:
                print(f"Warning: Unknown artifact type '{artifact_key}' requested.")
    else:
         c2_content_parts.append("<p>No specific artifacts requested for this chapter.</p>")

    # Join the parts into a single HTML string
    c2_full_content = "\n".join(c2_content_parts)

    c2 = epub.EpubHtml(title='Artifacts', file_name='chap_02.xhtml', lang=language, uid='chap_02') # <<< Set uid
    # Ensure the final content is wrapped in the basic HTML structure
    # Add CSS link automatically via book.add_item(nav_css) later
    c2.content = c2_full_content # Assign only body content
    chapters.append(c2)
    toc_links.append(epub.Link('chap_02.xhtml', 'Artifacts', 'artifacts'))
    # Add chapters to the book's manifest
    book.add_item(c1)
    book.add_item(c2)


    # --- Define CSS style ---
    style = '''
@namespace epub "http://www.idpf.org/2007/ops";
body { font-family: Cambria, Liberation Serif, sans-serif; } /* Added sans-serif fallback */
h1, h2, h3 { text-align: left; }
.note { border: 1px solid #ccc; padding: 10px; margin: 10px 0; background-color: #f9f9f9; }
.footnotes { font-size: 0.9em; margin-top: 2em; border-top: 1px solid #ccc; padding-top: 1em;}
.footnotes li { margin-bottom: 0.5em; }
.artifact-section { margin-bottom: 1em; padding: 10px; border: 1px dashed #ccc; } /* Style for artifact sections */
'''
    # Ensure CSS content is bytes
    nav_css = epub.EpubItem(uid="style_nav", file_name="style/main.css", media_type="text/css", content=style.encode('utf-8'))
    book.add_item(nav_css)

    # --- Define Book Structure (TOC, NCX, Nav) ---
    book.toc = tuple(toc_links) # Use toc_links for TOC

    # Add default NCX and Nav file
    book.add_item(epub.EpubNcx()) # NCX usually gets id 'ncx' by default
    nav_item = epub.EpubNav(uid='nav') # <<< Explicitly set uid='nav'
    book.add_item(nav_item)

    # --- Define Spine ---
    if generate_spine:
        spine_items = ['nav'] # Start with Nav document
        # Add chapters to spine only if they exist in the manifest
        if 'chap_01' in [item.id for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT)]:
            spine_items.append('chap_01')
        if 'chap_02' in [item.id for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT)]:
            spine_items.append('chap_02')
        book.spine = spine_items
    else:
        # Set spine to empty list if generate_spine is False
        # ebooklib should handle this, representing no linear reading order.
        book.spine = []

    # --- Write EPUB File ---
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    epub.write_epub(output_path, book, {}) # Removed the empty options dict
    print(f"EPUB file generated successfully at: {output_path}")


# --- Command Line Interface ---

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a simple EPUB file with specific artifacts for testing.")
    parser.add_argument("output_path", help="Path to save the generated EPUB file (e.g., testing/artifacts/test.epub)")
    parser.add_argument("-t", "--title", default="Test EPUB", help="Title of the EPUB")
    parser.add_argument("-a", "--author", default="EPUB Generator", help="Author of the EPUB")
    parser.add_argument("-l", "--lang", default="en", help="Language code (e.g., 'en')")
    parser.add_argument("--artifacts", nargs='+',
                        choices=['html', 'pandoc_attrs', 'pandoc_divs', 'footnotes', 'misc_pandoc', 'tables'],
                        default=[], # Default to empty list if not provided
                        help="List of artifact types to include in the EPUB content.")
    parser.add_argument("--no-spine", action='store_true', help="Do not include a spine in the EPUB") # Added no-spine flag

    args = parser.parse_args()

    print("--- Generating EPUB via CLI Arguments ---")
    create_epub(
        output_path=args.output_path,
        title=args.title,
        author=args.author,
        language=args.lang,
        artifacts_to_include=args.artifacts,
        generate_spine=not args.no_spine # Pass generate_spine flag
    )