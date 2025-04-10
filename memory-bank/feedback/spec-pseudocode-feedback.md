# Specification Writer Feedback Log

*This log tracks challenges, decisions, and insights during specification and pseudocode generation.*

---

## [2025-04-10 13:00:15] - Task Start: RAG Ingestion Pipeline Spec & Pseudocode

*   **Challenge:** Mode-specific memory file (`memory-bank/mode-specific/spec-pseudocode.md`) and feedback log (`memory-bank/feedback/spec-pseudocode-feedback.md`) did not exist upon initialization.
*   **Decision:** Created the feedback log file. Will create the mode-specific file when pseudocode or specific specs are ready to be stored. Proceeding with Memory Bank activation.
*   **Insight:** Initial setup requires file creation checks. The rules handle this, but it's a point to note for process robustness.

## [2025-04-10 13:01:23] - Library Research & Analysis (EbookLib, pandoc)

*   **Challenge:** Initial library search pointed to `EbookLib`. Analysis of its `epub2markdown.py` sample revealed a dependency on the external tool `pandoc` for HTML-to-Markdown conversion. This adds a system dependency.
*   **Challenge:** Neither the `EbookLib` sample nor `pandoc` (by default) appears to handle the specific cleaning requirements (removing `![]()`, `{#...}`, footnote artifacts, figure refs) needed for RAG optimization.
*   **Challenge:** The sample script doesn't utilize `EbookLib`'s documented ToC extraction capabilities.
*   **Decision:** Recommend `EbookLib` for EPUB parsing and ToC structure extraction. Accept `pandoc` as the conversion engine due to its robustness, but explicitly plan for custom Python-based post-processing (likely using regex) on the Markdown output to perform the required cleaning.
*   **Decision:** ToC extraction will be handled separately using `EbookLib` and prepended/integrated into the final Markdown output.
*   **Decision:** Zlibrary automation will be noted as a high-risk assumption or a separate module requirement in the specification, acknowledging legal/ethical/technical challenges.
*   **Insight:** The core complexity lies in the custom cleaning logic applied *after* initial conversion, highlighting the limitations of existing tools for this specific RAG use case. The specification must clearly define this post-processing step.