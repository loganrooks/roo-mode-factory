# Specification Writer Feedback Log

*This log tracks challenges, decisions, and insights during specification and pseudocode generation.*

---

## [2025-04-16 01:15:33] - Task: Custom MCP Server Specifications (`DB-MCP`, `PhilAPI-MCP`, `ChunkerEmbedder-MCP`)

*   **Challenge:** Accurately reflecting the existing `DB-MCP` logic (transactions, batching, ON CONFLICT) in the specification while also defining new servers (`PhilAPI-MCP`, `ChunkerEmbedder-MCP`) based purely on documentation.
*   **Challenge:** Specifying the interaction between `ChunkerEmbedder-MCP` and `DB-MCP`. Decided to specify Option A (ChunkerEmbedder acts as an MCP client to call DB-MCP) as the architecturally preferred approach, acknowledging the implementation complexity vs. Option B (direct DB access).
*   **Challenge:** Defining robust error handling for external API calls (`PhilAPI-MCP`) including rate limits, timeouts, and various HTTP status codes, mapping them to appropriate `McpError` types.
*   **Decision:** Integrated Python-like pseudocode directly within the Markdown specification for each handler function to clearly illustrate the intended logic flow. Used `@contextlib.contextmanager` for the DB cursor helper based on Python best practices, slightly deviating from the raw `try/finally` in the original `main.py` for clarity in the spec.
*   **Decision:** Included specific TDD anchors alongside the pseudocode to guide test development for each server and tool.
*   **Insight:** The `ChunkerEmbedder-MCP` has significant dependencies (embedding models/APIs, potentially MCP client logic) and requires careful environment setup and API key management. The alternative shell script approach might be simpler in some deployment scenarios despite potential environment management issues.
*   **Insight:** Consistent use of `McpError` with standard codes is crucial for the RooCode agent to understand and potentially react to failures in the MCP servers.


## [2025-04-15 22:41:50] - Task: .clinerules Specification (Philosopher, Researcher, Critic, Librarian)

*   **Challenge:** Ensuring pseudocode accurately reflects the intended logic flow and interactions described in the architecture (`docs/philosophy_assistant_architecture.md`), especially for complex multi-step processes like the Librarian's ingestion pipeline involving multiple MCPs and potential script execution.
*   **Challenge:** Defining clear boundaries and handoffs between modes (e.g., the exact structure of the task description passed from Philosopher to Researcher, or the results object passed back).
*   **Challenge:** Representing complex internal logic (like intent analysis or critique formulation) within pseudocode without making it overly verbose or implementation-specific. Used conceptual helper function names (e.g., `ANALYZE_INTENT`, `IDENTIFY_CRITIQUE_POINTS`).
*   **Decision:** Explicitly included Memory Bank read/write steps (`READ_MEMORY_BANK`, `UPDATE_MEMORY_BANK`) in the pseudocode to emphasize context management.
*   **Decision:** Included TDD anchors directly within the pseudocode comments to guide future test development for the `.clinerules` logic.
*   **Decision:** Focused Librarian pseudocode on the Shell Script option (`execute_command`) as a primary path, acknowledging the `ChunkerEmbedder-MCP` as an alternative.
*   **Insight:** The `.clinerules` will require robust error handling for MCP tool calls (`USE_MCP_TOOL`) and external script executions (`EXECUTE_COMMAND`). The interaction between the Librarian and the chunking/embedding script needs a well-defined contract (arguments, output format, exit codes) for reliable orchestration.
*   **Insight:** The effectiveness of the `Philosopher` and `Critic` modes will heavily depend on the quality of the underlying LLM and the implementation of the conceptual helper functions.


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