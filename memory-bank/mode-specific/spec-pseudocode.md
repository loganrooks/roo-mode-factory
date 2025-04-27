# Specification Writer Specific Memory

## Functional Requirements
<!-- Append new requirements using the format below -->

## System Constraints
<!-- Append new constraints using the format below -->

## Edge Cases
<!-- Append new edge cases using the format below -->

## Pseudocode Library
<!-- Append new pseudocode blocks using the format below -->
### Pseudocode: Philosopher Mode - Main Rule Flow
- Created: 2025-04-15 22:41:00
- Updated: 2025-04-15 22:41:00
```pseudocode
// --- Philosopher Mode .clinerules ---

// Rule: On User Message Received
ON event "user_message"
    // TDD Anchor: Test intent classification (question, command, discourse, task)
    // TDD Anchor: Test delegation trigger for research-requiring questions
    // TDD Anchor: Test critique trigger for "critique this" command
    // TDD Anchor: Test direct response for simple discourse

    LOG "Philosopher received user message."
    user_input = event.message

    // 1. Load Context from Memory Bank
    active_context = READ_MEMORY_BANK("activeContext.md")
    global_context = READ_MEMORY_BANK("globalContext.md")
    philosopher_memory = READ_MEMORY_BANK("mode-specific/philosopher.md")
    // Potentially load keyFindings, documentSummaries if relevant

    // 2. Analyze Intent & Context
    intent = ANALYZE_INTENT(user_input, active_context)
    current_methodology = GET_ACTIVE_METHODOLOGY(philosopher_memory, active_context)

    // 3. Decision Logic & Action
    IF intent == "RESEARCH_NEEDED" THEN
        task_description = FORMULATE_RESEARCH_TASK(user_input, active_context, current_methodology)
        UPDATE_MEMORY_BANK("activeContext.md", "[Philosopher] Delegating research: " + task_description)
        SWITCH_MODE("Researcher", reason="Research required", initial_message=task_description) // Pass task description
    ELSE IF intent == "CRITIQUE_REQUESTED" OR SHOULD_INVOKE_CRITIQUE(user_input, active_context) THEN
        context_to_critique = EXTRACT_CONTEXT_FOR_CRITIQUE(user_input, active_context)
        UPDATE_MEMORY_BANK("activeContext.md", "[Philosopher] Invoking critique.")
        SWITCH_MODE("Critic", reason="Critique requested/needed", initial_message=context_to_critique) // Pass context
    ELSE IF intent == "STUDY_TASK" THEN
        // May need research first
        IF REQUIRES_RESEARCH(user_input) THEN
             task_description = FORMULATE_RESEARCH_TASK(user_input, active_context, current_methodology)
             // Store original task details in activeContext for later use
             UPDATE_MEMORY_BANK("activeContext.md", "[Philosopher] Delegating research for study task: " + task_description)
             SWITCH_MODE("Researcher", reason="Research required for study task", initial_message=task_description)
        ELSE
             response = GENERATE_STUDY_ASSISTANCE(user_input, active_context, current_methodology)
             UPDATE_MEMORY_BANK("activeContext.md", "[Philosopher] Completed study task.")
             ATTEMPT_COMPLETION(result=response)
        END IF
    ELSE IF intent == "METHODOLOGY_CHANGE" THEN
        new_methodology = EXTRACT_METHODOLOGY(user_input)
        UPDATE_MEMORY_BANK("mode-specific/philosopher.md", "Set active methodology: " + new_methodology)
        response = "Acknowledged. Applying " + new_methodology + " methodology."
        ATTEMPT_COMPLETION(result=response)
    ELSE // Assume Discourse
        response = GENERATE_DISCOURSE_RESPONSE(user_input, active_context, current_methodology)
        UPDATE_MEMORY_BANK("activeContext.md", "[Philosopher] Engaging in discourse.")
        ATTEMPT_COMPLETION(result=response)
    END IF
END ON

// Rule: On Receiving Results from Researcher
ON event "mode_result" WHERE source_mode == "Researcher"
    // TDD Anchor: Test successful integration of research results into a user response
    // TDD Anchor: Test updating keyFindings/documentSummaries in Memory Bank
    // TDD Anchor: Test handling of research failure/empty results from Researcher

    LOG "Philosopher received results from Researcher."
    research_results = event.result
    original_task = GET_ORIGINAL_TASK_FROM_CONTEXT("activeContext.md") // Retrieve task that triggered research

    // 1. Load Context
    active_context = READ_MEMORY_BANK("activeContext.md")
    // Load other relevant MB sections

    // 2. Process & Synthesize Results
    IF research_results.success THEN
        // Update Memory Bank with summaries/findings
        UPDATE_MEMORY_BANK("documentSummaries.md", research_results.summary) // Example
        UPDATE_MEMORY_BANK("keyFindings.md", research_results.findings)     // Example

        // Synthesize response based on original task and results
        IF original_task.type == "STUDY_TASK" THEN // Check type property
             response = GENERATE_STUDY_ASSISTANCE(original_task.details, active_context, research_results)
        ELSE // Assume original task was user question/discourse
             response = SYNTHESIZE_RESPONSE(original_task.details, active_context, research_results)
        END IF
        UPDATE_MEMORY_BANK("activeContext.md", "[Philosopher] Synthesized response using research results.")
    ELSE
        LOG error "Research failed: " + research_results.error
        response = "I encountered an issue while researching that: " + research_results.error
        UPDATE_MEMORY_BANK("activeContext.md", "[Philosopher] Research delegation failed.")
    END IF

    // 3. Respond to User
    ATTEMPT_COMPLETION(result=response)
END ON

// Rule: On Receiving Critique from Critic
ON event "mode_result" WHERE source_mode == "Critic"
    // TDD Anchor: Test generating a response acknowledging/addressing the critique
    // TDD Anchor: Test triggering follow-up research based on critique
    // TDD Anchor: Test updating Memory Bank with critique interaction

    LOG "Philosopher received critique from Critic."
    critique = event.result
    active_context = READ_MEMORY_BANK("activeContext.md")

    // 1. Analyze Critique & Formulate Response
    response = FORMULATE_RESPONSE_TO_CRITIQUE(critique, active_context)
    UPDATE_MEMORY_BANK("activeContext.md", "[Philosopher] Responding to critique.")
    UPDATE_MEMORY_BANK("mode-specific/philosopher.md", "Critique received: " + critique.summary) // Log interaction

    // 2. Decide on Follow-up Action (Optional)
    IF REQUIRES_FURTHER_RESEARCH(critique) THEN
        task_description = FORMULATE_RESEARCH_TASK_FROM_CRITIQUE(critique, active_context)
        UPDATE_MEMORY_BANK("activeContext.md", "[Philosopher] Delegating research based on critique: " + task_description)
        SWITCH_MODE("Researcher", reason="Follow-up research after critique", initial_message=task_description)
    ELSE
        // 3. Respond to User (or continue internal processing)
        ATTEMPT_COMPLETION(result=response)
    END IF
END ON

// Helper Functions (Conceptual - Implementation depends on LLM/logic)
FUNCTION ANALYZE_INTENT(input, context) // -> "RESEARCH_NEEDED", "CRITIQUE_REQUESTED", "STUDY_TASK", "METHODOLOGY_CHANGE", "DISCOURSE"
FUNCTION FORMULATE_RESEARCH_TASK(input, context, methodology) // -> String (task description for Researcher)
FUNCTION EXTRACT_CONTEXT_FOR_CRITIQUE(input, context) // -> String (text/statement to critique)
FUNCTION SHOULD_INVOKE_CRITIQUE(input, context) // -> Boolean (logic for proactive critique)
FUNCTION GENERATE_STUDY_ASSISTANCE(input, context, methodology_or_results) // -> String (e.g., essay outline)
FUNCTION GENERATE_DISCOURSE_RESPONSE(input, context, methodology) // -> String (conversational response)
FUNCTION SYNTHESIZE_RESPONSE(original_input, context, research_results) // -> String
FUNCTION FORMULATE_RESPONSE_TO_CRITIQUE(critique, context) // -> String
FUNCTION REQUIRES_FURTHER_RESEARCH(critique) // -> Boolean
FUNCTION FORMULATE_RESEARCH_TASK_FROM_CRITIQUE(critique, context) // -> String
FUNCTION GET_ACTIVE_METHODOLOGY(philosopher_memory, active_context) // -> String or Null
FUNCTION EXTRACT_METHODOLOGY(input) // -> String
FUNCTION GET_ORIGINAL_TASK_FROM_CONTEXT(active_context_content) // -> Object { type: "STUDY_TASK" | "USER_QUERY", details: String }
// ... other helpers as needed
```
#### TDD Anchors:
- Test intent classification (question, command, discourse, task)
- Test delegation trigger for research-requiring questions
- Test critique trigger for "critique this" command
- Test direct response for simple discourse
- Test successful integration of research results into a user response
- Test updating keyFindings/documentSummaries in Memory Bank
- Test handling of research failure/empty results from Researcher
- Test generating a response acknowledging/addressing the critique
- Test triggering follow-up research based on critique
- Test updating Memory Bank with critique interaction

### Pseudocode: Researcher Mode - Main Rule Flow
- Created: 2025-04-15 22:41:00
- Updated: 2025-04-15 22:41:00
```pseudocode
// --- Researcher Mode .clinerules ---

// Rule: On Receiving Task from Philosopher
ON event "user_message" // Assuming delegation uses the standard message mechanism
    // TDD Anchor: Test parsing of task description from Philosopher
    // TDD Anchor: Test source selection logic (RAG vs PhilAPI vs Web)
    // TDD Anchor: Test query formulation for DB-MCP (embedding generation)
    // TDD Anchor: Test query formulation for PhilAPI-MCP
    // TDD Anchor: Test successful return of structured results to Philosopher

    LOG "Researcher received task."
    task_description = event.message

    // 1. Load Context
    active_context = READ_MEMORY_BANK("activeContext.md")
    global_context = READ_MEMORY_BANK("globalContext.md")
    // Load researchQueries, keyFindings for context augmentation

    UPDATE_MEMORY_BANK("activeContext.md", "[Researcher] Starting task: " + task_description)

    // 2. Analyze Task & Select Source(s)
    analyzed_task = ANALYZE_RESEARCH_TASK(task_description, active_context)
    selected_sources = SELECT_SOURCES(analyzed_task) // -> List ["RAG", "PhilAPI", "Web"]

    // 3. Execute Queries (Iterate through selected sources)
    all_results = []
    query_log = [] // For logging to researchQueries.md

    IF "RAG" IN selected_sources THEN
        rag_query_embedding = GENERATE_EMBEDDING(analyzed_task.query_text) // May involve local script/tool
        query_log.append({ type: "RAG", query: analyzed_task.query_text, embedding_used: true })
        TRY
            db_mcp_result = USE_MCP_TOOL("DB-MCP", "query_similar_chunks", { query_embedding: rag_query_embedding, filters: analyzed_task.filters })
            IF db_mcp_result.success THEN
                processed_rag_results = PROCESS_RAG_RESULTS(db_mcp_result.chunks)
                all_results.extend(processed_rag_results)
            ELSE
                LOG error "DB-MCP query failed: " + db_mcp_result.error
                UPDATE_MEMORY_BANK("activeContext.md", "[Researcher] DB-MCP query failed.")
            END IF
        CATCH McpError as e
             LOG error "Error calling DB-MCP: " + e.message
             UPDATE_MEMORY_BANK("activeContext.md", "[Researcher] Error calling DB-MCP.")
        END TRY
    END IF

    IF "PhilAPI" IN selected_sources THEN
        api_query = FORMULATE_API_QUERY(analyzed_task)
        query_log.append({ type: "PhilAPI", query: api_query.query, filters: api_query.filters }) // Log structured query
        TRY
            philapi_mcp_result = USE_MCP_TOOL("PhilAPI-MCP", "search_philpapers", { query: api_query.query, filters: api_query.filters })
            IF philapi_mcp_result.success THEN
                processed_api_results = PROCESS_PHILAPI_RESULTS(philapi_mcp_result.results)
                all_results.extend(processed_api_results)
            ELSE
                LOG error "PhilAPI-MCP query failed: " + philapi_mcp_result.error
                UPDATE_MEMORY_BANK("activeContext.md", "[Researcher] PhilAPI-MCP query failed.")
            END IF
        CATCH McpError as e
             LOG error "Error calling PhilAPI-MCP: " + e.message
             UPDATE_MEMORY_BANK("activeContext.md", "[Researcher] Error calling PhilAPI-MCP.")
        END TRY
    END IF

    IF "Web" IN selected_sources THEN
        web_query = FORMULATE_WEB_QUERY(analyzed_task)
        query_log.append({ type: "Web", query: web_query })
        TRY
            // Option 1: Use Brave Search MCP
            // web_mcp_result = USE_MCP_TOOL("brave-search", "brave_web_search", { query: web_query })
            // Option 2: Use Fetcher MCP (requires identifying URLs first, maybe via search)
            // urls_to_fetch = FIND_URLS_VIA_SEARCH(web_query) // Might use brave-search first just for URLs
            // web_mcp_result = USE_MCP_TOOL("fetcher", "fetch_urls", { urls: urls_to_fetch })

            // Assuming Brave Search for simplicity here:
            web_mcp_result = USE_MCP_TOOL("brave-search", "brave_web_search", { query: web_query })

            IF web_mcp_result.success THEN
                 processed_web_results = PROCESS_WEB_RESULTS(web_mcp_result.results) // Process search snippets or fetched content
                 all_results.extend(processed_web_results)
            ELSE
                 LOG error "Web search/fetch failed: " + web_mcp_result.error
                 UPDATE_MEMORY_BANK("activeContext.md", "[Researcher] Web search/fetch failed.")
            END IF
        CATCH McpError as e
             LOG error "Error calling Web Search/Fetcher MCP: " + e.message
             UPDATE_MEMORY_BANK("activeContext.md", "[Researcher] Error calling Web Search/Fetcher MCP.")
        END TRY
    END IF

    // 4. Log Queries
    UPDATE_MEMORY_BANK("researchQueries.md", query_log) // Append new queries

    // 5. Synthesize & Format Final Results
    IF all_results IS NOT EMPTY THEN
        final_summary, final_findings = SYNTHESIZE_ALL_RESULTS(all_results)
        // Log summaries/findings
        UPDATE_MEMORY_BANK("documentSummaries.md", final_summary) // Append
        UPDATE_MEMORY_BANK("keyFindings.md", final_findings)     // Append
        return_payload = { success: true, summary: final_summary, findings: final_findings, sources: EXTRACT_SOURCES(all_results) }
        UPDATE_MEMORY_BANK("activeContext.md", "[Researcher] Research complete. Found " + len(all_results) + " relevant items.")
    ELSE
        return_payload = { success: false, error: "No relevant information found.", summary: "", findings: [], sources: [] }
        UPDATE_MEMORY_BANK("activeContext.md", "[Researcher] Research complete. No relevant information found.")
    END IF

    // 6. Return to Philosopher
    SWITCH_MODE("Philosopher", reason="Returning research results", result=return_payload) // Pass results object
END ON

// Helper Functions (Conceptual)
FUNCTION ANALYZE_RESEARCH_TASK(task_desc, context) // -> { query_text: String, filters: Object, type: String }
FUNCTION SELECT_SOURCES(analyzed_task) // -> List ["RAG", "PhilAPI", "Web"]
FUNCTION GENERATE_EMBEDDING(text) // -> Vector (May call external tool/script)
FUNCTION PROCESS_RAG_RESULTS(chunks) // -> List[ProcessedResult]
FUNCTION FORMULATE_API_QUERY(analyzed_task) // -> { query: String, filters: Object }
FUNCTION PROCESS_PHILAPI_RESULTS(api_hits) // -> List[ProcessedResult]
FUNCTION FORMULATE_WEB_QUERY(analyzed_task) // -> String
FUNCTION PROCESS_WEB_RESULTS(search_hits_or_pages) // -> List[ProcessedResult]
FUNCTION SYNTHESIZE_ALL_RESULTS(all_results) // -> String (summary), List[Finding]
FUNCTION EXTRACT_SOURCES(all_results) // -> List[SourceLink]
// ... other helpers
```
#### TDD Anchors:
- Test parsing of task description from Philosopher
- Test source selection logic (RAG vs PhilAPI vs Web)
- Test query formulation for DB-MCP (embedding generation)
- Test query formulation for PhilAPI-MCP
- Test successful return of structured results to Philosopher

### Pseudocode: Critic Mode - Main Rule Flow
- Created: 2025-04-15 22:41:00
- Updated: 2025-04-15 22:41:00
```pseudocode
// --- Critic Mode .clinerules ---

// Rule: On Receiving Context to Critique from Philosopher
ON event "user_message" // Assuming invocation uses standard message mechanism
    // TDD Anchor: Test identification of assumptions in a sample text
    // TDD Anchor: Test formulation of relevant critical questions
    // TDD Anchor: Test delegation to Researcher if critique requires external info
    // TDD Anchor: Test successful return of critique object to Philosopher

    LOG "Critic received context for critique."
    context_to_critique = event.message

    // 1. Load Context & Critical Stance
    active_context = READ_MEMORY_BANK("activeContext.md")
    critic_memory = READ_MEMORY_BANK("mode-specific/critic.md")
    // Potentially load keyFindings for counter-arguments

    UPDATE_MEMORY_BANK("activeContext.md", "[Critic] Starting critique of context: " + SUBSTRING(context_to_critique, 0, 50))

    // 2. Analyze Context & Identify Critique Points
    critique_points = IDENTIFY_CRITIQUE_POINTS(context_to_critique, critic_memory, active_context) // -> List[Point(type, detail)]

    // 3. Check if Research is Needed for Critique
    IF REQUIRES_RESEARCH_FOR_CRITIQUE(critique_points) THEN
        task_description = FORMULATE_CRITIQUE_RESEARCH_TASK(critique_points, context_to_critique)
        // Store original context in activeContext for resuming later
        UPDATE_MEMORY_BANK("activeContext.md", "[Critic] Delegating research for critique: " + task_description)
        SWITCH_MODE("Researcher", reason="Research required for critique", initial_message=task_description)
    ELSE
        // 4. Formulate Critique Directly
        critique_output = FORMULATE_CRITIQUE(critique_points, context_to_critique, critic_memory) // -> { summary: String, questions: List[String], observations: List[String] }

        // 5. Log Critique
        UPDATE_MEMORY_BANK("mode-specific/critic.md", { context: context_to_critique, critique: critique_output }) // Append
        UPDATE_MEMORY_BANK("activeContext.md", "[Critic] Critique formulated.")

        // 6. Return Critique to Philosopher
        SWITCH_MODE("Philosopher", reason="Returning critique", result=critique_output)
    END IF
END ON

// Rule: On Receiving Research Results (if delegated)
ON event "mode_result" WHERE source_mode == "Researcher"
    // TDD Anchor: Test integration of research results into the final critique
    // TDD Anchor: Test resuming critique formulation after research

    LOG "Critic received research results."
    research_results = event.result
    original_critique_context = GET_ORIGINAL_CRITIQUE_CONTEXT("activeContext.md") // Retrieve stored context

    // 1. Load Context
    active_context = READ_MEMORY_BANK("activeContext.md")
    critic_memory = READ_MEMORY_BANK("mode-specific/critic.md")

    // 2. Re-analyze and Formulate Final Critique using Research
    IF research_results.success THEN
        critique_points = IDENTIFY_CRITIQUE_POINTS(original_critique_context.context, critic_memory, active_context, research_results)
        critique_output = FORMULATE_CRITIQUE(critique_points, original_critique_context.context, critic_memory)
        UPDATE_MEMORY_BANK("activeContext.md", "[Critic] Critique formulated using research results.")
    ELSE
        LOG error "Research for critique failed: " + research_results.error
        // Decide how to proceed: critique without research, or report failure?
        critique_output = { summary: "Critique incomplete due to research failure.", error: research_results.error, questions: [], observations: [] }
        UPDATE_MEMORY_BANK("activeContext.md", "[Critic] Research delegation for critique failed.")
    END IF

    // 3. Log Critique
    UPDATE_MEMORY_BANK("mode-specific/critic.md", { context: original_critique_context.context, critique: critique_output }) // Append

    // 4. Return Critique to Philosopher
    SWITCH_MODE("Philosopher", reason="Returning critique (post-research)", result=critique_output)
END ON


// Helper Functions (Conceptual)
FUNCTION IDENTIFY_CRITIQUE_POINTS(context, critic_mem, active_ctx, research_results=None) // -> List[CritiquePoint]
FUNCTION REQUIRES_RESEARCH_FOR_CRITIQUE(critique_points) // -> Boolean
FUNCTION FORMULATE_CRITIQUE_RESEARCH_TASK(critique_points, context) // -> String
FUNCTION FORMULATE_CRITIQUE(critique_points, context, critic_mem) // -> CritiqueObject { summary, questions, observations }
FUNCTION GET_ORIGINAL_CRITIQUE_CONTEXT(active_context_content) // -> Object { context: String }
// ... other helpers
```
#### TDD Anchors:
- Test identification of assumptions in a sample text
- Test formulation of relevant critical questions
- Test delegation to Researcher if critique requires external info
- Test successful return of critique object to Philosopher
- Test integration of research results into the final critique
- Test resuming critique formulation after research

### Pseudocode: Librarian Mode - Main Rule Flow (Shell Script Option)
- Created: 2025-04-15 22:41:00
- Updated: 2025-04-15 22:41:00
```pseudocode
// --- Librarian Mode .clinerules ---

// Rule: On Receiving Ingestion Command from User
ON event "user_message" // Assuming command format like "Librarian, ingest book ID 12345"
    // TDD Anchor: Test parsing of book ID from command
    // TDD Anchor: Test successful call to ZLibrary-MCP download_book_to_file
    // TDD Anchor: Test successful construction and execution of chunk/embed script command
    // TDD Anchor: Test handling of ZLibrary-MCP failure
    // TDD Anchor: Test handling of script execution failure (non-zero exit code)
    // TDD Anchor: Test logging of progress and errors to Memory Bank

    LOG "Librarian received ingestion command."
    command_text = event.message

    // 1. Parse Command & Load Context
    ingestion_params = PARSE_INGESTION_COMMAND(command_text) // -> { book_id: String, ... }
    IF ingestion_params IS NULL THEN
        ATTEMPT_COMPLETION(result="Invalid ingestion command. Please provide book ID.")
        EXIT RULE
    END IF

    active_context = READ_MEMORY_BANK("activeContext.md")
    librarian_memory = READ_MEMORY_BANK("mode-specific/librarian.md")

    UPDATE_MEMORY_BANK("activeContext.md", "[Librarian] Starting ingestion for Book ID: " + ingestion_params.book_id)
    UPDATE_MEMORY_BANK("mode-specific/librarian.md", "Ingestion Start: Book ID " + ingestion_params.book_id)

    // 2. Step 1: Acquire & Process via ZLibrary-MCP
    TRY
        zlib_result = USE_MCP_TOOL("ZLibrary-MCP", "download_book_to_file", { id: ingestion_params.book_id, process_for_rag: true })
    CATCH McpError as e
        LOG error "Error calling ZLibrary-MCP: " + e.message
        UPDATE_MEMORY_BANK("activeContext.md", "[Librarian] Failed: Error calling ZLibrary-MCP.")
        UPDATE_MEMORY_BANK("mode-specific/librarian.md", "Ingestion Failed (ZLib Call): " + e.message)
        ATTEMPT_COMPLETION(result="Failed to initiate download/processing via ZLibrary MCP: " + e.message)
        EXIT RULE
    END TRY

    IF NOT zlib_result.success OR NOT zlib_result.processed_path THEN
        error_msg = zlib_result.error || "Unknown error during ZLibrary download/processing."
        LOG error "ZLibrary-MCP failed: " + error_msg
        UPDATE_MEMORY_BANK("activeContext.md", "[Librarian] Failed: ZLibrary download/processing error.")
        UPDATE_MEMORY_BANK("mode-specific/librarian.md", "Ingestion Failed (ZLib Process): " + error_msg)
        ATTEMPT_COMPLETION(result="ZLibrary download/processing failed: " + error_msg)
        EXIT RULE
    END IF

    processed_file_path = zlib_result.processed_path
    doc_metadata = EXTRACT_METADATA_FROM_ZLIB_RESULT(zlib_result) // Get title, author etc. if available
    UPDATE_MEMORY_BANK("mode-specific/librarian.md", "Acquisition/Processing Complete. Processed file: " + processed_file_path)

    // 3. Step 2: Chunk, Embed, Store via Shell Script
    // Construct script command (ensure paths are correct relative to workspace or absolute)
    // Metadata needs to be passed securely, maybe via temp file or escaped JSON string
    metadata_json_string = JSON_STRINGIFY(doc_metadata) // Needs escaping for shell
    script_path = "scripts/chunk_embed_store.py" // Assumed path
    command_to_run = "python " + script_path + " --input \"" + processed_file_path + "\" --doc-metadata '" + metadata_json_string + "'" // Example, needs robust path/arg handling

    UPDATE_MEMORY_BANK("activeContext.md", "[Librarian] Executing chunk/embed/store script...")
    TRY
        script_result = EXECUTE_COMMAND(command_to_run, timeout=600) // Long timeout for processing
    CATCH CommandError as e
        LOG error "Error executing chunk/embed script: " + e.message
        UPDATE_MEMORY_BANK("activeContext.md", "[Librarian] Failed: Error executing processing script.")
        UPDATE_MEMORY_BANK("mode-specific/librarian.md", "Ingestion Failed (Script Execution): " + e.message)
        ATTEMPT_COMPLETION(result="Failed to execute processing script: " + e.message)
        EXIT RULE
    END TRY

    // Check script result (assuming script prints success/failure or uses exit codes)
    // This part is highly dependent on the script's output contract.
    IF script_result.exit_code != 0 OR CONTAINS_ERROR(script_result.stdout, script_result.stderr) THEN
        error_msg = "Script failed. Exit code: " + script_result.exit_code + ". Output: " + script_result.stderr // Simplified
        LOG error error_msg
        UPDATE_MEMORY_BANK("activeContext.md", "[Librarian] Failed: Processing script reported failure.")
        UPDATE_MEMORY_BANK("mode-specific/librarian.md", "Ingestion Failed (Script Logic): " + error_msg)
        ATTEMPT_COMPLETION(result="Processing script failed: " + error_msg)
        EXIT RULE
    END IF

    // 4. Report Success
    // Extract details from script output if available (e.g., doc ID, chunk count)
    final_doc_id = PARSE_SCRIPT_OUTPUT_FOR_DOC_ID(script_result.stdout)
    final_chunk_count = PARSE_SCRIPT_OUTPUT_FOR_CHUNK_COUNT(script_result.stdout)

    success_msg = "Ingestion successful for Book ID " + ingestion_params.book_id + "."
    IF final_doc_id THEN success_msg += " DB Doc ID: " + final_doc_id
    IF final_chunk_count THEN success_msg += " Chunks created: " + final_chunk_count

    LOG success_msg
    UPDATE_MEMORY_BANK("activeContext.md", "[Librarian] Ingestion successful for Book ID: " + ingestion_params.book_id)
    UPDATE_MEMORY_BANK("mode-specific/librarian.md", "Ingestion Success: Book ID " + ingestion_params.book_id + ". DB ID: " + (final_doc_id || "N/A"))
    ATTEMPT_COMPLETION(result=success_msg)

END ON

// Helper Functions (Conceptual)
FUNCTION PARSE_INGESTION_COMMAND(text) // -> { book_id: String } or Null
FUNCTION EXTRACT_METADATA_FROM_ZLIB_RESULT(zlib_result) // -> Object { title, author, ... }
FUNCTION JSON_STRINGIFY(object) // -> String (properly escaped for shell)
FUNCTION CONTAINS_ERROR(stdout, stderr) // -> Boolean (checks for error keywords)
FUNCTION PARSE_SCRIPT_OUTPUT_FOR_DOC_ID(stdout) // -> String or Null
FUNCTION PARSE_SCRIPT_OUTPUT_FOR_CHUNK_COUNT(stdout) // -> String or Null
// ... other helpers
```


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
