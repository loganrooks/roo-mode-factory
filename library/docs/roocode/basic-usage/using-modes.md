# Using Modes

Modes in Roo Code are specialized personas that tailor the assistant's behavior to your current task. Each mode offers different capabilities, expertise, and access levels to help you accomplish specific goals.

## Why Use Different Modes?

*   **Task specialization:** Get precisely the type of assistance you need for your current task
*   **Safety controls:** Prevent unintended file modifications when focusing on planning or learning
*   **Focused interactions:** Receive responses optimized for your current activity
*   **Workflow optimization:** Seamlessly transition between planning, implementing, debugging, and learning

## Switching Between Modes

Four ways to switch modes:

1.  **Dropdown menu:** Click the selector to the left of the chat input
    
    ![Using the dropdown menu to switch modes](https://docs.roocode.com/img/modes/modes.png)
2.  **Slash command:** Type `/architect`, `/ask`, `/debug`, or `/code` in the chat input
    
    ![Using slash commands to switch modes](https://docs.roocode.com/img/modes/modes-1.png)
3.  **Toggle command/Keyboard shortcut:** Use the keyboard shortcut below, applicable to your operating system. Each press cycles through the available modes in sequence, wrapping back to the first mode after reaching the end.
    
    | Operating System | Shortcut |
    | :--------------- | :------- |
    | macOS            | `⌘ + .`  |
    | Windows          | `Ctrl + .` |
    | Linux            | `Ctrl + .` |
    
4.  **Accept suggestions:** Click on mode switch suggestions that Roo offers when appropriate
    
    ![Accepting a mode switch suggestion from Roo](https://docs.roocode.com/img/modes/modes-2.png)

## Built-in Modes

### Code Mode (Default)

| Aspect          | Details                                                                                       |
| :-------------- | :-------------------------------------------------------------------------------------------- |
| **Description** | A skilled software engineer with expertise in programming languages, design patterns, and best practices |
| **Tool Access** | Full access to all tool groups: `read`, `edit`, `browser`, `command`, `mcp`                   |
| **Ideal For**   | Writing code, implementing features, debugging, and general development                       |
| **Special Features** | No tool restrictions—full flexibility for all coding tasks                                  |

### Ask Mode

| Aspect          | Details                                                                                       |
| :-------------- | :-------------------------------------------------------------------------------------------- |
| **Description** | A knowledgeable technical assistant focused on answering questions without changing your codebase |
| **Tool Access** | Limited access: `read`, `browser`, `mcp` only (cannot edit files or run commands)             |
| **Ideal For**   | Code explanation, concept exploration, and technical learning                                 |
| **Special Features** | Optimized for informative responses without modifying your project                          |

### Architect Mode

| Aspect          | Details                                                                                       |
| :-------------- | :-------------------------------------------------------------------------------------------- |
| **Description** | An experienced technical leader and planner who helps design systems and create implementation plans |
| **Tool Access** | Access to `read`, `browser`, `mcp`, and restricted `edit` (markdown files only)               |
| **Ideal For**   | System design, high-level planning, and architecture discussions                              |
| **Special Features** | Follows a structured approach from information gathering to detailed planning               |

### Debug Mode

| Aspect          | Details                                                                                       |
| :-------------- | :-------------------------------------------------------------------------------------------- |
| **Description** | An expert problem solver specializing in systematic troubleshooting and diagnostics             |
| **Tool Access** | Full access to all tool groups: `read`, `edit`, `browser`, `command`, `mcp`                   |
| **Ideal For**   | Tracking down bugs, diagnosing errors, and resolving complex issues                           |
| **Special Features** | Uses a methodical approach of analyzing, narrowing possibilities, and fixing issues         |

## Custom Modes

Create your own specialized assistants by defining tool access, file permissions, and behavior instructions. Custom modes help enforce team standards or create purpose-specific assistants. See [Custom Modes documentation](../features/custom-modes.md) for setup instructions.