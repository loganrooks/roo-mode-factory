# Specification: Philosophy Assistant Mode `.clinerules`

**Version:** 1.0
**Date:** 2025-04-15
**Author:** Specification Writer (RooCode Mode)
**Based On:** `docs/philosophy_assistant_architecture.md` (v2, 2025-04-15)

## 1. Introduction

This document provides detailed specifications and pseudocode for the `.clinerules` files governing the behavior of the core modes within the Philosophical Research Assistant system: `Philosopher`, `Researcher`, `Critic`, and `Librarian`. The focus is on the internal logic, decision-making, tool interactions (MCP, Memory Bank, Filesystem), and inter-mode communication defined within these rule files.

## 2. Common `.clinerules` Elements

*   **Memory Bank Integration:** All modes will include rules for reading relevant sections of the Memory Bank at the start of a task (e.g., `activeContext.md`, `globalContext.md`, mode-specific files) and writing updates at key points (task completion, significant findings, errors) using `insert_content` or `apply_diff`. Updates will follow the reverse chronological format specified in the global rules.
*   **Error Handling:** Rules should include basic error handling for tool calls (MCP, filesystem) and log errors to the Memory Bank (`activeContext.md`, potentially mode-specific logs). Critical failures might trigger a notification to the user or a switch to a default state.
*   **Mode Switching:** Modes will use the `switch_mode` tool for delegation (e.g., Philosopher -> Researcher) or when handing off control based on user intent.

## 3. Mode: `Philosopher`

### 3.1. Responsibilities

*   Primary user interaction point.
*   Engages in philosophical discourse (Socratic, dialectic, etc.).
*   Applies different philosophical methodologies based on context/request.
*   Assists with study tasks (outlining, question generation).
*   Synthesizes information from `Researcher` and RAG context.
*   Delegates research tasks to `Researcher`.
*   Invokes `Critic` for critical analysis.
*   Manages conversation flow and context using Memory Bank.

### 3.2. Workflow Triggers

*   Receiving a message from the User (`on_message` event).
*   Receiving results back from the `Researcher` mode.
*   Receiving critique back from the `Critic` mode.

### 3.3. Core Decision Logic (`.clinerules`)

*   **Input Analysis:**
    *   Analyze user message intent: Is it a question, a statement for discussion, a command (e.g., "apply phenomenology", "critique this"), a study task request, or a request requiring external information?
    *   Consult Memory Bank (`activeContext.md`, `mode-specific/philosopher.md`) for ongoing conversation context, current methodology, user preferences.
*   **Methodology Application:**
    *   If a specific methodology is requested or active (check Memory Bank), apply its principles to response generation or task decomposition (e.g., phenomenological bracketing, hermeneutic interpretation focus). Store active methodology in `mode-specific/philosopher.md`.
*   **Delegation vs. Direct Response:**
    *   If external information is needed: Formulate a research task description and delegate to `Researcher` using `switch_mode`. Log delegation in `activeContext.md`.
    *   If critique is requested or deemed appropriate: Formulate context for critique and invoke `Critic` using `switch_mode`. Log invocation in `activeContext.md`.
    *   If it's a study task (e.g., outline essay): Break down the task, potentially using RAG context via `Researcher` first, then generate the response.
    *   If it's discourse: Generate a response based on current context, methodology, and potentially RAG summaries from Memory Bank (`documentSummaries.md`, `keyFindings.md`).
*   **Synthesis:**
    *   When receiving results from `Researcher`: Parse results, integrate with existing context (Memory Bank), synthesize a response for the user, update `keyFindings.md` or `documentSummaries.md`.
    *   When receiving critique from `Critic`: Analyze critique, formulate a response (acknowledging, refuting, questioning), potentially trigger further research via `Researcher`.
*   **Memory Bank Management:**
    *   Read relevant context on task start.
    *   Write summaries, key findings, discourse turns, methodology shifts, and task status to relevant Memory Bank files (`activeContext.md`, `keyFindings.md`, `documentSummaries.md`, `mode-specific/philosopher.md`).

### 3.4. Required Tool Interactions

*   **`read_file`:** Read Memory Bank files (`activeContext.md`, `globalContext.md`, `keyFindings.md`, `documentSummaries.md`, `mode-specific/philosopher.md`).
*   **`insert_content` / `apply_diff`:** Write updates to Memory Bank files.
*   **`switch_mode`:** Delegate to `Researcher` or `Critic`.
*   **`attempt_completion`:** Respond to the user.

### 3.5. Interaction Patterns

*   **User -> Philosopher:** Primary input.
*   **Philosopher -> Researcher:** Delegates research tasks (provides task description, context).
*   **Researcher -> Philosopher:** Returns research results (summaries, data).
*   **Philosopher -> Critic:** Invokes critique (provides statement/context to critique).
*   **Critic -> Philosopher:** Returns critical analysis/questions.

### 3.6. Pseudocode (`.clinerules` Flow)

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

## 4. Mode: `Researcher`

### 4.1. Responsibilities

*   Executes research tasks delegated by `Philosopher`.
*   Formulates queries for RAG (`DB-MCP`), external APIs (`PhilAPI-MCP`), and web search (`Browser-MCP`).
*   Invokes appropriate MCP tools.
*   Parses, filters, and summarizes retrieved information.
*   Logs queries and summaries to Memory Bank.
*   Returns structured results to `Philosopher`.

### 4.2. Workflow Triggers

*   Receiving a task delegation message from `Philosopher` (`on_message` event, specifically checking for delegation context).

### 4.3. Core Decision Logic (`.clinerules`)

*   **Task Analysis:**
    *   Parse the task description received from `Philosopher`.
    *   Identify keywords, concepts, entities, and desired information type (e.g., definitions, arguments, specific paper, general overview).
    *   Consult Memory Bank (`activeContext.md`, `globalContext.md`, `researchQueries.md`, `keyFindings.md`) for relevant context to refine queries.
*   **Source Selection:**
    *   Based on the task and context, decide the best source(s):
        *   Internal RAG DB (`DB-MCP`): For querying ingested texts.
        *   PhilPapers API (`PhilAPI-MCP`): For academic papers, abstracts, metadata.
        *   Web Search (`Browser-MCP` / built-in `fetcher`): For general information, recent events, non-academic sources.
        *   (Future: Other APIs via `PhilAPI-MCP` like Open Library, DOAB).
    *   Prioritize sources (e.g., RAG first, then PhilPapers, then Web). May query multiple sources.
*   **Query Formulation:**
    *   Generate semantic query embeddings for RAG search.
    *   Construct structured queries for `PhilAPI-MCP` (using filters if applicable).
    *   Formulate effective search terms for web search.
    *   Augment queries with context from Memory Bank if helpful.
*   **Tool Invocation:**
    *   Call the chosen MCP server tools (`DB-MCP.query_similar_chunks`, `PhilAPI-MCP.search_philpapers`, `fetcher.fetch_url` or `brave-search.brave_web_search`).
    *   Handle potential errors from MCP calls.
*   **Result Processing:**
    *   Parse JSON results from MCPs.
    *   Filter irrelevant results.
    *   Summarize key information from retrieved chunks, abstracts, or web pages.
    *   Extract relevant metadata (source, authors, date).
*   **Memory Bank Management:**
    *   Log the formulated queries (semantic, API, web) to `researchQueries.md`.
    *   Log summaries of retrieved documents/findings to `documentSummaries.md` or `keyFindings.md`.
    *   Update `activeContext.md` with research progress/status.
*   **Return Results:**
    *   Format results (summaries, key points, source links) into a structured object.
    *   Switch back to `Philosopher` mode using `switch_mode`, passing the results object.

### 4.4. Required Tool Interactions

*   **`read_file`:** Read Memory Bank files (`activeContext.md`, `globalContext.md`, `researchQueries.md`, `keyFindings.md`, `mode-specific/researcher.md`).
*   **`insert_content` / `apply_diff`:** Write updates to Memory Bank files.
*   **`use_mcp_tool`:**
    *   `DB-MCP`: `query_similar_chunks`
    *   `PhilAPI-MCP`: `search_philpapers`, `get_philpapers_details` (potentially `search_other_apis`)
    *   `fetcher`: `fetch_url` (if using built-in fetcher)
    *   `brave-search`: `brave_web_search` (if using Brave Search MCP)
*   **`switch_mode`:** Return results to `Philosopher`.
*   **(Potentially `execute_command`):** If embedding generation for RAG queries is done via a local script.

### 4.5. Interaction Patterns

*   **Philosopher -> Researcher:** Receives research task description.
*   **Researcher -> DB-MCP:** Sends queries, receives chunks/metadata.
*   **Researcher -> PhilAPI-MCP:** Sends queries, receives paper metadata/abstracts.
*   **Researcher -> Browser-MCP / Fetcher / Brave-Search:** Sends search terms/URLs, receives web content/search results.
*   **Researcher -> Philosopher:** Returns structured research results.

### 4.6. Pseudocode (`.clinerules` Flow)

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

## 5. Mode: `Critic`

### 5.1. Responsibilities

*   Critiques statements, arguments, or research findings provided by `Philosopher`.
*   Identifies underlying assumptions, premises, and potential contradictions.
*   Formulates critical questions or alternative perspectives.
*   Aims to stimulate deeper reflection and potentially induce *aporia*.
*   May draw on specific critical methodologies or texts (potentially via `Researcher`).
*   Maintains a critical stance context in Memory Bank.

### 5.2. Workflow Triggers

*   Receiving context/statement to critique from `Philosopher` (`on_message` event).

### 5.3. Core Decision Logic (`.clinerules`)

*   **Context Analysis:**
    *   Parse the input context provided by `Philosopher`.
    *   Identify the main claim, argument, or finding being presented.
    *   Load critical stance history or relevant theoretical context from `mode-specific/critic.md`.
*   **Identify Points for Critique:**
    *   Look for unstated assumptions or premises.
    *   Check for logical fallacies or inconsistencies.
    *   Compare the statement against known counter-arguments or alternative theories (potentially drawing from `keyFindings.md` or requiring delegation to `Researcher`).
    *   Identify potential biases or limitations in the presented information/source.
*   **Formulate Critique:**
    *   Generate critical questions targeting the identified weak points.
    *   Present counter-examples or alternative interpretations.
    *   Frame the critique constructively to encourage further thought (avoid being purely dismissive).
    *   Apply specific critical lenses if configured or requested (e.g., deconstruction, ideology critique).
*   **Research for Critique (Optional):**
    *   If critique requires specific external knowledge (e.g., details of a counter-theory): Formulate a research task and delegate to `Researcher` via `switch_mode`. Store the original critique context to resume upon receiving results.
*   **Memory Bank Management:**
    *   Log the critique provided and the context it addressed in `mode-specific/critic.md`.
    *   Update `activeContext.md` with critique status.
*   **Return Critique:**
    *   Format the critique (questions, observations).
    *   Switch back to `Philosopher` mode using `switch_mode`, passing the critique object.

### 5.4. Required Tool Interactions

*   **`read_file`:** Read Memory Bank files (`activeContext.md`, `globalContext.md`, `keyFindings.md`, `mode-specific/critic.md`).
*   **`insert_content` / `apply_diff`:** Write updates to Memory Bank files.
*   **`switch_mode`:** Return critique to `Philosopher` or delegate research to `Researcher`.
*   **(Potentially `use_mcp_tool`):** If delegating to `Researcher`.

### 5.5. Interaction Patterns

*   **Philosopher -> Critic:** Receives context/statement to critique.
*   **Critic -> Philosopher:** Returns critique (questions, analysis).
*   **Critic -> Researcher (Optional):** Delegates research needed for critique.
*   **Researcher -> Critic (Optional):** Returns research results.

### 5.6. Pseudocode (`.clinerules` Flow)

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

## 6. Mode: `Librarian`

### 6.1. Responsibilities

*   Manages the RAG knowledge base ingestion pipeline.
*   Orchestrates document acquisition via `ZLibrary-MCP`.
*   Handles text extraction (via `ZLibrary-MCP`'s `process_for_rag`).
*   Orchestrates chunking and embedding (via Shell script/`Shell_MCP` or `ChunkerEmbedder-MCP`).
*   Manages database insertion via `DB-MCP`.
*   Logs ingestion progress, metadata, and errors to Memory Bank.

### 6.2. Workflow Triggers

*   Receiving an ingestion command from the User (e.g., "Librarian, ingest book ID 12345").

### 6.3. Core Decision Logic (`.clinerules`)

*   **Parse Ingestion Command:**
    *   Extract necessary information (e.g., book ID, source URL, local file path).
    *   Validate input.
*   **Step 1: Acquisition & Processing (ZLibrary-MCP):**
    *   Call `ZLibrary-MCP.download_book_to_file` with the book ID and `process_for_rag: true`.
    *   Handle the response: Check for success, get the path to the *processed* text file (`processed_path`). Log errors.
*   **Step 2: Chunking & Embedding (Shell Script or Chunker-MCP):**
    *   **Option A (Shell Script):**
        *   Construct the command line arguments for the chunking/embedding script (e.g., `python scripts/chunk_embed_store.py --input <processed_path> --doc-metadata <metadata_json>`). Metadata might come from ZLibrary result or user.
        *   Use `execute_command` (via Shell MCP if available and configured, or built-in if allowed) to run the script.
        *   Monitor script execution (capture stdout/stderr if possible). Handle script errors (non-zero exit code).
    *   **Option B (ChunkerEmbedder-MCP):**
        *   Gather document metadata.
        *   Call `ChunkerEmbedder-MCP.process_text_file` with the `processed_path` and metadata.
        *   Handle the response: Check for success, log errors.
    *   **Decision:** The `.clinerules` should ideally support *one* of these methods based on system configuration, or have a conditional rule. Assume Shell Script via `execute_command` for this pseudocode unless `ChunkerEmbedder-MCP` is explicitly preferred.
*   **Step 3: Database Insertion (Handled by Script/Chunker-MCP):**
    *   The chunking/embedding script (or `ChunkerEmbedder-MCP`) is responsible for calling `DB-MCP` tools (`add_document`, `batch_insert_chunks`) internally. The Librarian mode primarily orchestrates the *call* to the script/MCP, not the DB interaction itself.
*   **Memory Bank Management:**
    *   Log the start of the ingestion process in `activeContext.md`.
    *   Log the specific document being ingested, parameters used, and intermediate file paths in `mode-specific/librarian.md`.
    *   Log success or failure of each major step (acquisition, processing, chunk/embed/store) in `activeContext.md` and `mode-specific/librarian.md`.
*   **Report Completion:**
    *   Once the pipeline finishes (or fails), report the outcome (success, document ID, chunk count, or error message) to the user via `attempt_completion`.

### 6.4. Required Tool Interactions

*   **`read_file`:** Read Memory Bank files (`activeContext.md`, `mode-specific/librarian.md`).
*   **`insert_content` / `apply_diff`:** Write updates to Memory Bank files.
*   **`use_mcp_tool`:**
    *   `ZLibrary-MCP`: `download_book_to_file`
    *   `ChunkerEmbedder-MCP`: `process_text_file` (If using Option B)
*   **`execute_command`:** Run the chunking/embedding Python script (If using Option A). Requires careful path handling and assumes the script exists and Python environment is set up.
*   **`attempt_completion`:** Report final status to the user.

### 6.5. Interaction Patterns

*   **User -> Librarian:** Initiates ingestion command.
*   **Librarian -> ZLibrary-MCP:** Calls download/process tool.
*   **Librarian -> Shell_MCP / `execute_command`:** Runs chunk/embed script.
*   **Librarian -> ChunkerEmbedder-MCP (Alternative):** Calls processing tool.
*   **(Script/Chunker-MCP -> DB-MCP):** Internal interaction, not directly managed by Librarian rules.
*   **Librarian -> User:** Reports completion status.

### 6.6. Pseudocode (`.clinerules` Flow - Assuming Shell Script Option A)

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

## 7. Memory Bank Updates (Draft)

The following updates will be made to the Memory Bank before calling `attempt_completion`.

*   **`memory-bank/activeContext.md`:**
    *   Add entry: `[YYYY-MM-DD HH:MM:SS] - SpecPseudo - Task Start - Generating .clinerules specifications for Philosopher, Researcher, Critic, Librarian modes.`
    *   Add entry: `[YYYY-MM-DD HH:MM:SS] - SpecPseudo - Task Complete - Created docs/philosophy_modes_clinerules_spec.md.`
*   **`memory-bank/globalContext.md`:**
    *   Under `# Progress & Milestones`: Add entry detailing the completion of the `.clinerules` specification.
*   **`memory-bank/mode-specific/spec-pseudocode.md`:**
    *   Append the pseudocode sections generated above under the `## Pseudocode Library` heading, using the standard format.
*   **`memory-bank/feedback/spec-pseudocode-feedback.md`:**
    *   Add entry: `[YYYY-MM-DD HH:MM:SS] - Task: .clinerules Specification`
        *   `Challenge:` Ensuring pseudocode accurately reflects the intended logic flow and interactions described in the architecture, especially for complex multi-step processes like the Librarian's ingestion pipeline.
        *   `Challenge:` Defining clear boundaries and handoffs between modes (e.g., what exactly does Philosopher pass to Researcher?).
        *   `Decision:` Used conceptual helper functions in pseudocode to represent complex analysis or generation steps, focusing on the rule flow and tool interactions.
        *   `Decision:` Explicitly included Memory Bank read/write steps in the pseudocode.
        *   `Insight:` The `.clinerules` need robust error handling for MCP calls and script executions. The interaction between Librarian and the chunking/embedding script needs a well-defined contract (arguments, output format, exit codes).