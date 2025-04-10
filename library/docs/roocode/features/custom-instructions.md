# Custom Instructions

Custom Instructions allow you to personalize how Roo behaves, providing specific guidance that shapes responses, coding style, and decision-making processes.

## What Are Custom Instructions?

Custom Instructions define specific behaviors, preferences, and constraints beyond Roo's basic role definition. Examples include coding style, documentation standards, testing requirements, and workflow guidelines.

## Setting Custom Instructions

### Global Custom Instructions

These instructions apply across all workspaces and maintain your preferences regardless of which project you're working on.

**How to set them:**

![Roo Code Prompts tab showing global custom instructions interface](https://docs.roocode.com/img/custom-instructions/custom-instructions.png)

1.  **Open Prompts Tab:** Click the icon in the Roo Code top menu bar
2.  **Find Section:** Find the "Custom Instructions for All Modes" section
3.  **Enter Instructions:** Enter your instructions in the text area
4.  **Save Changes:** Click "Done" to save your changes

### Workspace-Level Instructions

These instructions only apply within your current workspace, allowing you to customize Roo Code's behavior for specific projects.

#### Workspace-Wide Instructions

Workspace-wide instructions can be defined in a `.roorules` file in your workspace root.

#### Mode-Specific Instructions

Mode-specific instructions can be set in two independent ways that can be used simultaneously:

1.  **Using the Prompts Tab:**
    
    ![Roo Code Prompts tab showing mode-specific custom instructions interface](https://docs.roocode.com/img/custom-instructions/custom-instructions-2.png)
    *   **Open Tab:** Click the icon in the Roo Code top menu bar
    *   **Select Mode:** Under the Modes heading, click the button for the mode you want to customize
    *   **Enter Instructions:** Enter your instructions in the text area under "Mode-specific Custom Instructions (optional)"
    *   **Save Changes:** Click "Done" to save your changes
    
    > **Global Mode Rules**
    > If the mode itself is global (not workspace-specific), any custom instructions you set for it will also apply globally for that mode across all workspaces.

2.  **Using Rule Files:** Create a `.roorules-[mode]` file in your workspace root (e.g., `.roorules-code`)

When both tab instructions and rule files are set for a mode, both sets of instructions will be included in the system prompt.

## How Instructions are Combined

Instructions are placed in the system prompt in this exact format:

```
====USER'S CUSTOM INSTRUCTIONS

The following additional instructions are provided by the user, and should be followed to the best of your ability without interfering with the TOOL USE guidelines.

[Language Preference (if set)]
[Global Instructions]
[Mode-specific Instructions]

Rules:
[.roorules-{mode} rules]
[.roorules rules]
```

## Rules about .rules files

*   **File Location:** All rule files must be placed in the workspace root directory
*   **Empty Files:** Empty or missing rule files are silently skipped
*   **Source Headers:** Each rule file's contents are included with a header indicating its source
*   **Rule Interaction:** Mode-specific rules complement global rules rather than replacing them

## Examples of Custom Instructions

*   "Always use spaces for indentation, with a width of 4 spaces"
*   "Use camelCase for variable names"
*   "Write unit tests for all new functions"
*   "Explain your reasoning before providing code"
*   "Focus on code readability and maintainability"
*   "Prioritize using the most common library in the community"
*   "When adding new features to websites, ensure they are responsive and accessible"

> **Pro Tip: File-Based Team Standards**
> When working in team environments, placing `.roorules` files under version control allows you to standardize Roo's behavior across your entire development team. This ensures consistent code style, documentation practices, and development workflows for everyone on the project.

## Combining with Custom Modes

For advanced customization, combine with [Custom Modes](custom-modes.md) to create specialized environments with specific tool access, file restrictions, and tailored instructions.