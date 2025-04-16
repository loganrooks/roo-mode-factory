# ADR-001: Z-Library EPUB Acquisition Integration

*   **Status:** Proposed
*   **Date:** 2025-04-10

## Context

The project requires a method to automatically acquire EPUB files, specifically from Z-Library, to feed into the existing RAG ingestion pipeline (`pipelines/rag_ingestion.py` and `process_epubs.sh`). The current pipeline processes existing EPUBs but lacks an acquisition mechanism. A premium Z-Library account is available, potentially offering higher download limits but still subject to automation detection. Integration options considered include using existing libraries/tools (like `sertraline/zlibrary`), building a dedicated MCP server, or using simple standalone scripts.

## Decision

We will implement the Z-Library integration using a **standalone Python script (`acquire_epub.py`)** that leverages the **`sertraline/zlibrary`** Python library (unofficial).

**Details:**

1.  **Core Script (`acquire_epub.py`):**
    *   Uses `sertraline/zlibrary` for Z-Library interactions.
    *   Handles authentication using credentials stored securely.
    *   Performs searches based on user queries (CLI argument).
    *   Filters results for EPUB format.
    *   Presents search results interactively to the user for selection.
    *   Retrieves the download URL for the selected book.
    *   Downloads the EPUB file using the authenticated session (requires careful implementation with `requests` or `aiohttp`).
    *   Outputs the local path of the downloaded EPUB file.
2.  **Authentication:**
    *   Credentials (email/password) stored in `config/zlibrary_creds.env`.
    *   File loaded via `python-dotenv`.
    *   `config/zlibrary_creds.env` **MUST** be added to `.gitignore`.
3.  **Dependencies:** `zlibrary`, `python-dotenv`, `requests` (or `aiohttp`).
4.  **Storage:**
    *   Downloaded EPUBs temporarily stored in `downloads/epubs/` (this directory should also be gitignored).
5.  **Orchestration:**
    *   An existing or new script (e.g., modified `process_epubs.sh`) will:
        *   Execute `python acquire_epub.py --query "..."`.
        *   Capture the output path.
        *   Pass the path to `python pipelines/rag_ingestion.py --input <path>`.

## Consequences

**Positive:**

*   Leverages features of an existing library (`sertraline/zlibrary`), reducing initial development effort for search, auth, and proxy support.
*   Integrates cleanly with the existing Python-based RAG pipeline.
*   Avoids the complexity of setting up and maintaining a dedicated MCP server for this specific task initially.
*   Provides the needed automated EPUB acquisition capability.
*   The script is modular and could potentially be refactored into an MCP tool later if needed.

**Negative:**

*   **Reliability Risk:** High dependency on the unofficial `sertraline/zlibrary` library, which may break if Z-Library changes its site/API. Requires monitoring and potential maintenance.
*   **Implementation Detail:** Correctly handling the authenticated session/cookies for the download request needs careful implementation and testing.
*   **Anti-Scraping:** Z-Library may still implement blocking or rate-limiting measures against automation, even with proxies/Tor and a premium account. Requires robust error handling, delays, and potentially proxy rotation.
*   **Legal/Ethical:** Automating downloads from Z-Library exists in a legal gray area regarding copyright. Use must be responsible and aware of potential risks.
*   **Dependencies:** Introduces new Python dependencies to manage.
*   **Interactivity:** The current design requires user interaction for book selection, limiting full end-to-end automation unless selection logic is changed (e.g., "download first result").