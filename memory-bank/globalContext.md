# Global Context

*This file stores overarching project information, decisions, and patterns.*

---

## Product Context
*High-level goals, user needs, constraints.*

---

## System Patterns
*Architectural decisions, component relationships, data flow.*


### [2025-04-15 22:10:00] - System Pattern Update: Philosophical Research Assistant Architecture (v2)
*Architect: Updated design incorporating existing ZLibrary MCP and making PhilAPI-MCP essential.*
- **Description:** Defines a system with `Philosopher`, `Researcher`, `Critic`, and `Librarian` modes. RAG DB access via `DB-MCP`. External API access (PhilPapers) via essential `PhilAPI-MCP`. Document acquisition/processing leverages existing `ZLibrary-MCP`. Chunking/Embedding via optional `ChunkerEmbedder-MCP` or Shell script.
- **Reference:** `docs/philosophy_assistant_architecture.md` (Updated)

#### Dependency Map (Philosophical Assistant) - [2025-04-15 22:10:00]
```mermaid
graph TD
    subgraph RooCode Agent Modes
        User -- Interacts --> Philosopher
        Philosopher -- Delegates Research --> Researcher
        Philosopher -- Engages/Invokes --> Critic
        Critic -- Critiques --> Philosopher
        User -- Initiates Ingestion --> Librarian
    end

    subgraph External Systems & Tools
        DB[(PostgreSQL + pgvector)]
        ExtAPIs{{External APIs (PhilPapers, etc.)}}
        Web((Internet))
        LocalFS[/Local Filesystem/]
    end

    subgraph MCP Servers
        DB_MCP[DB-MCP Server]
        ZLibrary_MCP[ZLibrary-MCP Server (Existing)]
        PhilAPI_MCP[PhilAPI-MCP Server]
        Chunker_MCP[ChunkerEmbedder-MCP (Optional)]
        Shell_MCP[Shell MCP (Alternative for Chunking)]
        Browser_MCP[Browser MCP / Built-in]
    end

    subgraph Memory Bank (Filesystem)
        MB[Memory Bank Files (.md)]
    end

    %% Mode Interactions
    Philosopher -- Reads/Writes --> MB
    Researcher -- Reads/Writes --> MB
    Critic -- Reads/Writes --> MB
    Librarian -- Reads/Writes --> MB

    %% Researcher Interactions
    Researcher -- Uses Tool --> DB_MCP
    Researcher -- Uses Tool --> PhilAPI_MCP
    Researcher -- Uses Tool --> Browser_MCP

    %% Librarian Interactions (Ingestion)
    Librarian -- Uses Tool --> ZLibrary_MCP -- Downloads/Processes --> LocalFS
    Librarian -- Reads Processed File --> LocalFS
    Librarian -- Uses Tool --> Chunker_MCP -- Calls --> DB_MCP
    Librarian -- Uses Tool (Alternative) --> Shell_MCP -- Runs --> ChunkingScript{Chunking/Embedding Script} -- Calls --> DB_MCP
    ChunkingScript -- Reads --> LocalFS

    %% MCP Server Interactions
    DB_MCP -- Accesses --> DB
    PhilAPI_MCP -- Accesses --> ExtAPIs
    Browser_MCP -- Accesses --> Web

    style DB fill:#f9f,stroke:#333,stroke-width:2px
    style ExtAPIs fill:#ccf,stroke:#333,stroke-width:2px
    style Web fill:#9cf,stroke:#333,stroke-width:2px
    style LocalFS fill:#fcc,stroke:#333,stroke-width:2px
    style MB fill:#ff9,stroke:#333,stroke-width:2px
    style ZLibrary_MCP fill:#f6b26b,stroke:#333,stroke-width:2px
```
*(Brief Explanation: User interacts with Philosopher. Researcher uses DB/PhilAPI/Web MCPs. Librarian uses ZLibrary MCP for acquisition/processing, then Chunker/Shell MCP + DB MCP for storage. All modes use Memory Bank.)*


---

## Decision Log
*Key choices made, rationale, and alternatives considered.*


### [2025-04-15 22:10:00] - Architectural Decisions Update: Philosophical Research Assistant (v2)
- **Decision:** Incorporate existing `ZLibrary-MCP` for book acquisition and initial RAG processing (text extraction), simplifying the ingestion pipeline managed by the `Librarian` mode. Remove dedicated `Ingestion-MCP` design.
- **Decision:** Elevate `PhilAPI-MCP` to **essential** status to ensure access to PhilPapers API, as requested. Other APIs (Open Library, DOAB) remain optional extensions for this MCP.
- **Decision:** Retain `DB-MCP` as the essential, secure interface to the PostgreSQL/pgvector database.
- **Decision:** Chunking/Embedding step after ZLibrary processing will be handled either by a script invoked via Shell MCP or an optional dedicated `ChunkerEmbedder-MCP`.
- **Rationale:** Incorporates user feedback regarding existing ZLibrary MCP capabilities and the requirement for PhilPapers access. Simplifies ingestion by leveraging existing tools. Clarifies the role of the PhilAPI MCP.
- **Reference:** `docs/philosophy_assistant_architecture.md` (Updated)

### [2025-04-10 18:45:50] - Zlibrary Integration Approach (ADR-001)
- **Decision:** Implement Zlibrary EPUB acquisition using a standalone Python script (`acquire_epub.py`) leveraging the `sertraline/zlibrary` library.
- **Rationale:** Reduces initial effort vs. MCP server, integrates with Python pipeline. Acknowledges risks of unofficial library dependency and anti-scraping measures.
- **Reference:** `docs/adr-001-zlibrary-epub-acquisition.md`


---

## Progress & Milestones
*Overall status, completed steps, next objectives.*

### [2025-04-10 18:51:20] - Correction: `acquire_epub.py` Implementation
- **Status:** Initial script implementation required correction after user feedback.
- **Details:** Verified correct usage of `zlibrary` package via README. Updated script and requirements accordingly.
- **Learning:** Reinforced need to verify external library details before implementation.


### [2025-04-10 18:45:50] - EPUB Acquisition Script Implemented
- **Status:** Completed initial implementation of `pipelines/acquire_epub.py` for Zlibrary search and download.
- **Details:** Script uses `sertraline-zlib` (assumed), `aiohttp`, `dotenv`, `argparse`. Follows ADR-001.
- **Next:** Testing and refinement based on actual library behavior.


---