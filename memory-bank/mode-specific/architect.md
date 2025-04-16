# Architect Specific Memory
<!-- Entries below should be added reverse chronologically (newest first) -->

## System Diagrams

### Diagram: Philosophical Research Assistant - High-Level (v2) - [2025-04-15 22:10:00]
- **Description:** Updated interaction flow incorporating existing ZLibrary MCP and essential PhilAPI-MCP.
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
**Notes:** This updated diagram reflects the use of the existing `ZLibrary-MCP` for acquisition/processing and the essential nature of the `PhilAPI-MCP`.

## Component Specifications

### Component Specification: `Philosopher` Mode - [2025-04-15 21:54:00]
- **Responsibility**: Primary user interaction, philosophical discourse, methodology application, study assistance, synthesis.
- **Dependencies**: User Input, `Researcher` Mode, `Critic` Mode, Memory Bank.
- **Interfaces Exposed**: User interaction via RooCode chat.
- **Internal Structure (Optional High-Level)**: `.clinerules` defining discourse patterns, methodology selection logic, task decomposition, synthesis prompts.

### Component Specification: `Researcher` Mode - [2025-04-15 22:10:00] (Updated)
- **Responsibility**: Information retrieval (RAG DB, External APIs via `PhilAPI-MCP`, Web), query formulation, result pre-processing.
- **Dependencies**: `Philosopher` Mode, `DB-MCP`, `PhilAPI-MCP`, Browser MCP/Built-in, Memory Bank.
- **Interfaces Exposed**: Internal interface for receiving tasks from `Philosopher` and returning results.
- **Internal Structure (Optional High-Level)**: `.clinerules` defining query generation logic, tool invocation sequences (including `PhilAPI-MCP`), result parsing.

### Component Specification: `Critic` Mode - [2025-04-15 21:54:00]
- **Responsibility**: Critiquing assumptions, identifying contradictions, challenging premises.
- **Dependencies**: `Philosopher` Mode, Memory Bank (potentially dedicated section).
- **Interfaces Exposed**: Internal interface for receiving content/arguments from `Philosopher` and returning critiques.
- **Internal Structure (Optional High-Level)**: `.clinerules` defining critical analysis techniques (Socratic, Deconstructive, etc.), assumption identification logic.

### Component Specification: `Librarian` Mode - [2025-04-15 22:10:00] (Updated)
- **Responsibility**: Managing RAG ingestion pipeline using `ZLibrary-MCP` for acquisition/processing, followed by chunking/embedding (via `ChunkerEmbedder-MCP` or Shell script) and storage via `DB-MCP`.
- **Dependencies**: User Input (for initiation), `ZLibrary-MCP`, `DB-MCP`, `ChunkerEmbedder-MCP` / Shell MCP, Filesystem Tools, Memory Bank.
- **Interfaces Exposed**: User interaction for initiating ingestion. Internal interface for pipeline orchestration.
- **Internal Structure (Optional High-Level)**: `.clinerules` defining ingestion workflow steps using `ZLibrary-MCP`, error handling, invocation of chunking/embedding step, interaction with `DB-MCP`.

### Component Specification: `DB-MCP` Server - [2025-04-15 21:54:00]
- **Responsibility**: Secure interface to PostgreSQL/pgvector database.
- **Dependencies**: PostgreSQL Database.
- **Interfaces Exposed**: MCP Tools (`query_similar_chunks`, `batch_insert_chunks`, `add_document`, `get_document_metadata`, `delete_document`).
- **Internal Structure (Optional High-Level)**: Node.js/Python application using MCP SDK and database drivers. Handles connection pooling, query execution, batching logic, credential management (via env vars).

### Component Specification: `ZLibrary-MCP` Server (Existing) - [2025-04-15 22:10:00]
- **Responsibility**: Search ZLibrary, download books, process downloads for RAG (text extraction).
- **Dependencies**: ZLibrary service, Filesystem (for output).
- **Interfaces Exposed**: MCP Tools (Assumed: `search_books`, `download_book_to_file`, `process_document_for_rag`).
- **Internal Structure (Optional High-Level)**: Assumed Node.js/Python application using MCP SDK, ZLibrary interaction logic (API/scraping), file processing logic (e.g., calling `pandoc` or similar).

### Component Specification: `PhilAPI-MCP` Server (Essential) - [2025-04-15 22:10:00] (Updated)
- **Responsibility**: Abstract interface to PhilPapers API and potentially other philosophy APIs (Open Library, DOAB).
- **Dependencies**: PhilPapers API, potentially other external APIs.
- **Interfaces Exposed**: MCP Tools (`search_philpapers`, `get_philpapers_details`, `search_other_apis` (optional)).
- **Internal Structure (Optional High-Level)**: Node.js/Python application using MCP SDK and HTTP client libraries. Handles API key management (via env vars), request formatting, response parsing.

### Component Specification: `ChunkerEmbedder-MCP` Server (Optional) - [2025-04-15 22:10:00]
- **Responsibility**: Encapsulate chunking and embedding logic for processed text files.
- **Dependencies**: `DB-MCP`, Filesystem, Embedding Model/API.
- **Interfaces Exposed**: MCP Tool (`process_text_file`).
- **Internal Structure (Optional High-Level)**: Python application using MCP SDK. Manages Python environment for NLP/embedding libraries, reads files, performs chunking/embedding, calls `DB-MCP`.

## Interface Definitions

### Interface Definition: `DB-MCP` Tools - [2025-04-15 21:54:00]
- **Purpose**: Define interactions with the RAG database.
#### Method/Endpoint: `query_similar_chunks`
- Input: `{ query_embedding: number[], top_k: number, filters?: Record<string, any> }`
- Output: `{ chunks: Array<{ chunk_id: number, document_id: number, chunk_text: string, chunk_index: number, distance: number, metadata?: Record<string, any> }> }`
- Behavior: Performs vector similarity search in PostgreSQL/pgvector, optionally applying metadata filters. Returns top_k matching chunks.
- Security: Accessed only by authorized modes (`Researcher`, `Librarian`/`ChunkerEmbedder-MCP`). Credentials managed by server via env vars.
#### Method/Endpoint: `batch_insert_chunks`
- Input: `{ chunks: Array<{ document_id: number, chunk_text: string, chunk_index: number, embedding: number[] }> }`
- Output: `{ success: boolean, inserted_count: number, error?: string }`
- Behavior: Inserts multiple chunks and embeddings into the database efficiently using batching.
- Security: Accessed only by authorized modes (`Librarian`/`ChunkerEmbedder-MCP`).
#### Method/Endpoint: `add_document`
- Input: `{ source_uri: string, title?: string, authors?: string, publication_date?: string, metadata_jsonb?: Record<string, any>, extracted_text_hash?: string }`
- Output: `{ doc_id: number }`
- Behavior: Inserts or updates document metadata in the `documents` table.
- Security: Accessed only by authorized modes (`Librarian`/`ChunkerEmbedder-MCP`).
#### Method/Endpoint: `get_document_metadata`
- Input: `{ doc_id?: number, source_uri?: string }`
- Output: `{ metadata: Record<string, any> | null }`
- Behavior: Retrieves metadata for a specific document.
- Security: Accessed only by authorized modes (`Researcher`, `Librarian`/`ChunkerEmbedder-MCP`).
#### Method/Endpoint: `delete_document`
- Input: `{ doc_id: number }`
- Output: `{ success: boolean }`
- Behavior: Deletes a document and all associated chunks.
- Security: Accessed only by authorized modes (potentially `Librarian` or an admin function).

### Interface Definition: `ZLibrary-MCP` Tools (Existing/Assumed) - [2025-04-15 22:10:00]
- **Purpose**: Define interactions for acquiring and processing books from ZLibrary.
#### Method/Endpoint: `search_books` (Assumed)
- Input: `{ query: string, ...filters }`
- Output: `{ results: Array<...> }`
- Behavior: Searches ZLibrary for books.
- Security: Credentials managed by server via env vars. Accessed by `Librarian` (or `Researcher`).
#### Method/Endpoint: `download_book_to_file` (Assumed)
- Input: `{ id: string, format?: string, outputDir?: string, process_for_rag?: boolean }`
- Output: `{ success: boolean, file_path?: string, processed_path?: string, error?: string }`
- Behavior: Downloads book from ZLibrary, optionally processes it for RAG (text extraction) saving results locally.
- Security: Credentials managed by server via env vars. Accessed by `Librarian`.
#### Method/Endpoint: `process_document_for_rag` (Assumed/Internal)
- Input: `{ file_path: string, output_format?: string }`
- Output: `{ success: boolean, processed_path?: string, error?: string }`
- Behavior: Extracts text content from a downloaded file (EPUB, PDF). May be called internally by `download_book_to_file`.
- Security: Internal server logic or accessed by `Librarian`.

### Interface Definition: `PhilAPI-MCP` Tools (Essential) - [2025-04-15 22:10:00] (Updated)
- **Purpose**: Define interactions specifically with PhilPapers API and potentially others.
#### Method/Endpoint: `search_philpapers`
- Input: `{ query: string, filters?: Record<string, any> }`
- Output: `{ results: Array<{ title: string, authors: string[], abstract?: string, url?: string, source_id: string }> }`
- Behavior: Searches PhilPapers API for papers matching the query.
- Security: API keys (if needed) managed by server via env vars. Accessed by `Researcher`.
#### Method/Endpoint: `get_philpapers_details`
- Input: `{ source_id: string }`
- Output: `{ details: Record<string, any> }`
- Behavior: Retrieves detailed information for a specific paper from the PhilPapers API.
- Security: API keys (if needed) managed by server via env vars. Accessed by `Researcher`.
#### Method/Endpoint: `search_other_apis` (Optional)
- Input: `{ query: string, source: 'openlibrary' | 'doab' | '...', filters?: Record<string, any> }`
- Output: `{ results: Array<{ title: string, authors: string[], source_id: string, url?: string }> }`
- Behavior: Searches specified external API (e.g., Open Library) for books/papers matching the query.
- Security: API keys managed by server via env vars. Accessed by `Researcher`.

### Interface Definition: `ChunkerEmbedder-MCP` Tools (Optional) - [2025-04-15 22:10:00]
- **Purpose**: Define interaction for chunking/embedding processed text.
#### Method/Endpoint: `process_text_file`
- Input: `{ file_path: string, doc_metadata: Record<string, any> }`
- Output: `{ success: boolean, doc_id?: number, chunk_count?: number, error?: string }`
- Behavior: Reads text file, performs chunking and embedding, calls `DB-MCP` to store results.
- Security: Accessed by `Librarian`. Manages embedding API keys via env vars.

## Data Models

### Data Model: RAG Database Schema - [2025-04-15 21:54:00]
- **Purpose**: Store processed philosophical texts, chunks, and embeddings for retrieval.
- **Structure**:
  ```sql
  -- documents table
  CREATE TABLE documents (
      doc_id SERIAL PRIMARY KEY,
      source_uri TEXT UNIQUE NOT NULL,
      title TEXT,
      authors TEXT,
      publication_date DATE,
      extracted_text_hash VARCHAR(64),
      metadata_jsonb JSONB,
      last_processed_at TIMESTAMPTZ DEFAULT NOW()
  );

  -- chunks table
  CREATE TABLE chunks (
      chunk_id SERIAL PRIMARY KEY,
      document_id INTEGER NOT NULL REFERENCES documents(doc_id) ON DELETE CASCADE,
      chunk_text TEXT NOT NULL,
      chunk_index INTEGER NOT NULL,
      embedding vector(1536) -- Dimension depends on embedding model
  );

  -- Indexes (HNSW example)
  CREATE INDEX idx_documents_source_uri ON documents (source_uri);
  CREATE INDEX idx_chunks_document_id ON chunks (document_id);
  CREATE INDEX idx_chunks_embedding_cosine ON chunks USING hnsw (embedding vector_cosine_ops) WITH (m = 16, ef_construction = 64);
  ALTER TABLE chunks ADD CONSTRAINT unique_chunk_order UNIQUE (document_id, chunk_index);
  ```
- **Relationships**: `chunks.document_id` references `documents.doc_id`.