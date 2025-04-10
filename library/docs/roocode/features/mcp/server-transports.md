# MCP Server Transports: STDIO & SSE

Model Context Protocol (MCP) supports two primary transport mechanisms for communication between Roo Code and MCP servers: Standard Input/Output (STDIO) and Server-Sent Events (SSE). Each has distinct characteristics, advantages, and use cases.

## STDIO Transport

STDIO transport runs locally on your machine and communicates via standard input/output streams.

### How STDIO Transport Works

1.  The client (Roo Code) spawns an MCP server as a child process
2.  Communication happens through process streams: client writes to server's STDIN, server responds to STDOUT
3.  Each message is delimited by a newline character
4.  Messages are formatted as JSON-RPC 2.0

    ```
    Client                    Server
    |---- JSON message ------>| (via STDIN)
    |<---- JSON message ------| (via STDOUT)
    ```

### STDIO Characteristics

*   **Locality**: Runs on the same machine as Roo Code
*   **Performance**: Very low latency and overhead (no network stack involved)
*   **Simplicity**: Direct process communication without network configuration
*   **Relationship**: One-to-one relationship between client and server
*   **Security**: Inherently more secure as no network exposure

### When to Use STDIO

STDIO transport is ideal for:

*   Local integrations and tools running on the same machine
*   Security-sensitive operations
*   Low-latency requirements
*   Single-client scenarios (one Roo Code instance per server)
*   Command-line tools or IDE extensions

### STDIO Implementation Example

```javascript
import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';

const server = new Server({
  name: 'local-server',
  version: '1.0.0'
});

// Register tools...

// Use STDIO transport
const transport = new StdioServerTransport(server);
transport.listen();
```

## SSE Transport

Server-Sent Events (SSE) transport runs on a remote server and communicates over HTTP/HTTPS.

### How SSE Transport Works

1.  The client (Roo Code) connects to the server's SSE endpoint via HTTP GET request
2.  This establishes a persistent connection where the server can push events to the client
3.  For client-to-server communication, the client makes HTTP POST requests to a separate endpoint
4.  Communication happens over two channels:
    *   Event Stream (GET): Server-to-client updates
    *   Message Endpoint (POST): Client-to-server requests

    ```
    Client                             Server
    |---- HTTP GET /events ----------->| (establish SSE connection)
    |<---- SSE event stream -----------| (persistent connection)
    |                                  |
    |---- HTTP POST /message --------->| (client request)
    |<---- SSE event with response ----| (server response)
    ```

### SSE Characteristics

*   **Remote Access**: Can be hosted on a different machine from Roo Code
*   **Scalability**: Can handle multiple client connections concurrently
*   **Protocol**: Works over standard HTTP (no special protocols needed)
*   **Persistence**: Maintains a persistent connection for server-to-client messages
*   **Authentication**: Can use standard HTTP authentication mechanisms

### When to Use SSE

SSE transport is better for:

*   Remote access across networks
*   Multi-client scenarios
*   Public services
*   Centralized tools that many users need to access
*   Integration with web services

### SSE Implementation Example

```javascript
import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { SSEServerTransport } from '@modelcontextprotocol/sdk/server/sse.js';
import express from 'express';

const app = express();
const server = new Server({
  name: 'remote-server',
  version: '1.0.0'
});

// Register tools...

// Use SSE transport
const transport = new SSEServerTransport(server);
app.use('/mcp', transport.requestHandler());

app.listen(3000, () => {
  console.log('MCP server listening on port 3000');
});
```

## Hybrid Approaches

Some scenarios benefit from a hybrid approach:

1.  **STDIO with Network Access**: A local STDIO server that acts as a proxy to remote services
2.  **SSE with Local Commands**: A remote SSE server that can trigger operations on the client machine through callbacks
3.  **Gateway Pattern**: STDIO servers for local operations that connect to SSE servers for specialized functions

## Choosing Between STDIO and SSE

Consideration

STDIO

SSE

**Location**

Local machine only

Local or remote

**Clients**

Single client

Multiple clients

**Performance**

Lower latency

Higher latency (network overhead)

**Setup Complexity**

Simpler

More complex (requires HTTP server)

**Security**

Inherently secure

Requires explicit security measures

**Network Access**

Not needed

Required

**Scalability**

Limited to local machine

Can distribute across network

**Deployment**

Per-user installation

Centralized installation

**Updates**

Distributed updates

Centralized updates

**Resource Usage**

Uses client resources

Uses server resources

**Dependencies**

Client-side dependencies

Server-side dependencies

## Configuring Transports in Roo Code

For detailed information on configuring STDIO and SSE transports in Roo Code, including example configurations, see the [Understanding Transport Types](using-mcp-in-roo.md#understanding-transport-types) section in the Using MCP in Roo Code guide.