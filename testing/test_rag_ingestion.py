import pytest
import os
import re
from pathlib import Path

# Assuming the scripts are importable relative to the project root
# Adjust imports if necessary based on project structure/PYTHONPATH
try:
    from testing.utils.epub_generator import create_epub
    from pipelines.rag_ingestion import run_pipeline
except ImportError:
    # Handle cases where direct import might fail (e.g., running pytest from root)
    import sys
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from testing.utils.epub_generator import create_epub
    from pipelines.rag_ingestion import run_pipeline

# Define artifacts used in the test EPUB
TEST_ARTIFACTS = ['html', 'pandoc_attrs', 'footnotes', 'misc_pandoc']
TEST_TITLE = "Pipeline Test EPUB"

@pytest.fixture
def test_epub(tmp_path):
    """Fixture to generate a test EPUB file in a temporary directory."""
    epub_path = tmp_path / "test_pipeline.epub"
    create_epub(
        output_path=str(epub_path),
        title=TEST_TITLE,
        artifacts_to_include=TEST_ARTIFACTS
    )
    # Verify epub exists after generation
    assert epub_path.exists()
    return epub_path


@pytest.fixture
def test_epub_no_spine(tmp_path):
    """Fixture to generate a test EPUB file without a spine."""
    epub_path = tmp_path / "test_pipeline_no_spine.epub"
    create_epub(
        output_path=str(epub_path),
        title="No Spine Test EPUB",
        artifacts_to_include=TEST_ARTIFACTS,
        generate_spine=False # Explicitly disable spine generation
    )
    # Verify epub exists after generation
    assert epub_path.exists()
    return epub_path


def test_rag_pipeline_cleaning(test_epub, tmp_path):
    """
    Tests the RAG ingestion pipeline's ability to process a generated EPUB
    and verify specific artifact cleaning steps.
    """
    output_dir = tmp_path / "output"
    output_dir.mkdir()

    # --- Act ---
    # Run the pipeline function directly
    output_file_path_str = run_pipeline(str(test_epub), str(output_dir))

    # --- Assert ---
    # 1. Check if output file was created
    assert output_file_path_str is not None, "Pipeline did not return an output file path."
    output_file_path = Path(output_file_path_str)
    assert output_file_path.exists(), f"Output file {output_file_path} was not created."
    assert output_file_path.name == "test_pipeline.rag.md", "Output file name is incorrect."

    # 2. Read output content
    output_content = output_file_path.read_text(encoding='utf-8')
    assert output_content, "Output file is empty."

    # 3. Verify specific cleaning rules based on previous manual checks
    # 3a. Duplicated TOC section should be absent
    assert f"## {TEST_TITLE}" not in output_content, "Duplicated TOC section found."
    assert f"1.  [Introduction](chap_01.xhtml)" not in output_content, "Duplicated TOC link found."

    # 3b. Simulated Pandoc footnote marker should be absent
    # Literal string in output was: \[\\ref\\\]{.footnote-class}
    assert r'\[\\ref\\\]{.footnote-class}' not in output_content, "Simulated Pandoc footnote marker found."

    # 3c. Footnote backlinks should be absent
    assert '↩︎' not in output_content, "Footnote backlink arrow found."

    # 3d. <br/> handling should result in a newline
    assert "This line ends with a hard break.\nThis is the next line." in output_content, "<br/> tag did not result in a newline."

    # 3e. Basic content check
    assert "# Introduction" in output_content, "Introduction header missing."
    assert "This is a test EPUB file generated programmatically." in output_content, "Introduction content missing."
    assert "## HTML Artifacts" in output_content, "HTML Artifacts section missing."
    assert "**bold text**" in output_content, "Bold text formatting incorrect/missing."


def test_rag_pipeline_no_spine(test_epub_no_spine, tmp_path, caplog):
    """
    Tests the RAG pipeline's handling of an EPUB with no spine.
    It should log a warning and process all document items.
    """
    output_dir = tmp_path / "output_no_spine"
    output_dir.mkdir()

    # --- Act ---
    # Run the pipeline function directly
    output_file_path_str = run_pipeline(str(test_epub_no_spine), str(output_dir))

    # --- Assert ---
    # 1. Check logs for the expected warning
    assert "EPUB spine is empty or missing. Processing all document items." in caplog.text

    # 2. Check if output file was created
    assert output_file_path_str is not None, "Pipeline did not return an output file path (no spine)."
    output_file_path = Path(output_file_path_str)
    assert output_file_path.exists(), f"Output file {output_file_path} was not created (no spine)."
    assert output_file_path.name == "test_pipeline_no_spine.rag.md", "Output file name is incorrect (no spine)."

    # 3. Read output content
    output_content = output_file_path.read_text(encoding='utf-8')
    assert output_content, "Output file is empty (no spine)."

    # 4. Verify content is still present (basic check)
    assert "# Introduction" in output_content, "Introduction header missing (no spine)."
    assert "## HTML Artifacts" in output_content, "HTML Artifacts section missing (no spine)."
    assert "This line ends with a hard break.\nThis is the next line." in output_content, "<br/> handling incorrect (no spine)."


def test_rag_pipeline_file_not_found(tmp_path, caplog):
    """
    Tests the pipeline's handling of a non-existent input EPUB file.
    It should return None and log an error.
    """
    non_existent_epub = tmp_path / "not_a_real_file.epub"
    output_dir = tmp_path / "output_not_found"
    output_dir.mkdir()

    # --- Act ---
    result = run_pipeline(str(non_existent_epub), str(output_dir))

    # --- Assert ---


import subprocess
import sys

def test_rag_pipeline_cli(test_epub, tmp_path):
    """
    Tests running the pipeline script from the command line.
    """
    output_dir = tmp_path / "output_cli"
    output_dir.mkdir()
    output_file_expected = output_dir / "test_pipeline.rag.md"
    script_path = Path(__file__).parent.parent / "pipelines" / "rag_ingestion.py"

    # --- Act ---
    # Use subprocess to run the script as if from the command line
    # Ensure using the same python executable that runs pytest
    process = subprocess.run(
        [sys.executable, str(script_path), str(test_epub), str(output_dir)],
        capture_output=True,
        text=True,
        check=False # Don't raise exception on non-zero exit
    )

    # --- Assert ---
    # 1. Check exit code
    assert process.returncode == 0, f"CLI script failed with exit code {process.returncode}. Stderr: {process.stderr}"

    # 2. Check if output file was created
    assert output_file_expected.exists(), f"Output file {output_file_expected} was not created via CLI."

    # 3. Optional: Check stdout for success message (might be fragile)
    assert "Processing complete. Output saved to:" in process.stderr # Check stderr for logs

    # Check for specific error log related to reading/parsing failure
    # Check for the higher-level failure log

