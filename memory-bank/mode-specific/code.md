# Code Specific Memory

## Implementation Notes
<!-- Append notes for features/components using the format below -->
### Implementation: `acquire_epub.py` (Corrected) - [2025-04-10 18:51:30]
- **Approach**: Implemented standalone Python script based on ADR-001 for Zlibrary search and download, corrected after verifying library details.
- **Key Files Modified/Created**:
    - `pipelines/acquire_epub.py`: Rewritten script using correct `zlibrary` methods (`AsyncZlib`, `login`, `search`, `fetch`, `Extension`, `Language`).
    - `requirements.txt`: Corrected dependency to `zlibrary`, added `aiohttp`.
    - `.env`: Created placeholder for credentials.
- **Notes**: Uses `asyncio`, `aiohttp` for async operations and manual download. Implements explicit login and fetches full book details to get download URL as per library README. Enabled library debug logging. Still requires testing with actual credentials.



## Technical Debt Log
<!-- Append new or resolved tech debt items using the format below -->

## Dependencies Log
<!-- Append new dependencies using the format below -->
### Dependency: zlibrary - [2025-04-10 18:51:30]
- **Version**: Latest (as per `pip install`)
- **Purpose**: Unofficial Z-Library API interaction (login, search, fetch details).
- **Used by**: `pipelines/acquire_epub.py`
- **Config notes**: Requires ZLIBRARY_EMAIL and ZLIBRARY_PASSWORD in `.env`. Correct package name verified.

### Dependency: aiohttp - [2025-04-10 18:51:30]
- **Version**: Latest (as per `pip install`)
- **Purpose**: Asynchronous HTTP client for handling downloads and session management.
- **Used by**: `pipelines/acquire_epub.py`
- **Config notes**: Used for manual download, leveraging session cookies established by `zlibrary.login()`.



## Code Patterns Log
<!-- Append new code patterns using the format below -->