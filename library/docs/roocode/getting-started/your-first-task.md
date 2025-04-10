# Starting Your First Task with Roo Code

Now that you've [configured your AI provider and model](connecting-api-provider.md), you're ready to start using Roo Code! This guide walks you through your first interaction.

## Step 1: Open the Roo Code Panel

Click the Roo Code icon () in the VS Code Activity Bar (vertical bar on the side of the window) to open the chat interface. If you don't see the icon, verify the extension is installed and enabled.

![Roo Code icon in VS Code Activity Bar](https://docs.roocode.com/img/your-first-task/your-first-task.png)

_The Roo Code icon in the Activity Bar opens the chat interface._

## Step 2: Type Your Task

Type a clear, concise description of what you want Roo Code to do in the chat box at the bottom of the panel. Examples of effective tasks:

*   "Create a file named `hello.txt` containing 'Hello, world!'."
*   "Write a Python function that adds two numbers."
*   "Create an HTML file for a simple website with the title 'Roo test'"

No special commands or syntax needed—just use plain English.

![Typing a task in the Roo Code chat interface](https://docs.roocode.com/img/your-first-task/your-first-task-6.png)

_Enter your task in natural language - no special syntax required._

## Step 3: Send Your Task

Press Enter or click the Send icon () to the right of the input box.

## Step 4: Review and Approve Actions

Roo Code analyzes your request and proposes specific actions. These may include:

*   **Reading files:** Shows file contents it needs to access
*   **Writing to files:** Displays a diff with proposed changes (added lines in green, removed in red)
*   **Executing commands:** Shows the exact command to run in your terminal
*   **Using the Browser:** Outlines browser actions (click, type, etc.)
*   **Asking questions:** Requests clarification when needed to proceed

![Reviewing a proposed file creation action](https://docs.roocode.com/img/your-first-task/your-first-task-7.png)

_Roo Code shows exactly what action it wants to perform and waits for your approval._

**Each action requires your explicit approval** (unless auto-approval is enabled):

*   **Approve:** Click the "Approve" button to execute the proposed action
*   **Reject:** Click the "Reject" button and provide feedback if needed

## Step 5: Iterate

Roo Code works iteratively. After each action, it waits for your feedback before proposing the next step. Continue this review-approve cycle until your task is complete.

![Final result of a completed task showing the iteration process](https://docs.roocode.com/img/your-first-task/your-first-task-8.png)

_After completing the task, Roo Code shows the final result and awaits your next instruction._

## Conclusion

You've now completed your first task with Roo Code! Through this process, you've learned:

*   How to interact with Roo Code using natural language
*   The approval-based workflow that keeps you in control
*   The iterative approach Roo Code uses to solve problems step-by-step

This iterative, approval-based workflow is at the core of how Roo Code works—letting AI handle the tedious parts of coding while you maintain complete oversight. Now that you understand the basics, you're ready to tackle more complex tasks, explore different [modes](../basic-usage/using-modes.md) for specialized workflows, or try the [auto-approval feature](../features/auto-approving-actions.md) to speed up repetitive tasks.