# Installing Roo Code

Roo Code is a VS Code extension that brings AI-powered coding assistance directly to your editor. Install using one of these methods:

1.  **VS Code Marketplace (Recommended)** - fastest method for standard VS Code and Cursor users
2.  **Open VSX Registry** - for VS Code-compatible editors like VSCodium

## VS Code Marketplace

1.  Open VS Code
2.  Access Extensions: Click the Extensions icon in the Activity Bar or press `Ctrl+Shift+X` (Windows/Linux) or `Cmd+Shift+X` (macOS)
3.  Search for "Roo Code"
4.  Select "Roo Code" by RooVeterinaryInc and click **Install**
5.  Reload VS Code if prompted

After installation, find the Roo Code icon () in the Activity Bar to open the Roo Code panel.

![VS Code marketplace with Roo Code extension ready to install](https://docs.roocode.com/img/installing/installing.png)

_VS Code marketplace with Roo Code extension ready to install_

## Open VSX Registry

For VS Code-compatible editors without Marketplace access (like VSCodium and Windsurf):

1.  Open your editor
2.  Access the Extensions view
3.  Search for "Roo Code"
4.  Select "Roo Code" by RooVeterinaryInc and click **Install**
5.  Reload if prompted

![Open VSX Registry with Roo Code extension ready to install](https://docs.roocode.com/img/installing/installing-1.png)

_Open VSX Registry with Roo Code extension ready to install_

## Manual Installation from VSIX

If you prefer to download and install the VSIX file directly:

1.  **Download the VSIX file:**
    
    *   Find official releases on the [Roo Code GitHub Releases page](https://github.com/RooVetGit/Roo-Code/releases)
    *   Download the `.vsix` file from the latest release
2.  **Install in VS Code:**
    
    *   Open VS Code
    *   Access Extensions view
    *   Click the "..." menu in the Extensions view
    *   Select "Install from VSIX..."
    *   Browse to and select your downloaded `.vsix` file

![VS Code's Install from VSIX dialog](https://docs.roocode.com/img/installing/installing-2.png)

_Installing Roo Code using VS Code's "Install from VSIX" dialog_

## Development Builds

Developer Information Only

This section is intended only for developers contributing to Roo Code.

If you're building Roo Code from source:

1.  Run `npm run build` in the project directory
2.  Find the generated VSIX file in the `bin/` directory
3.  In VS Code, open Extensions view and select "Install from VSIX..." from the "..." menu
4.  Browse to and select your generated `.vsix` file

![VS Code's Install from VSIX dialog](https://docs.roocode.com/img/installing/installing-2.png)

_Installing a development build using VS Code's "Install from VSIX" dialog_

## Troubleshooting

![VS Code Output panel showing Roo Code logs for troubleshooting](https://docs.roocode.com/img/installing/installing-4.png)

_VS Code Output panel showing Roo Code logs for troubleshooting_

**Extension Not Visible**

*   Restart VS Code
*   Verify Roo Code is listed and enabled in Extensions
*   Try disabling and re-enabling
*   Check Output panel for errors (View → Output, select "Roo Code")

**Installation Problems**

*   Ensure stable internet connection
*   Verify VS Code version 1.84.0 or later
*   If VS Code Marketplace is inaccessible, try the Open VSX Registry method

## Getting Support

If you encounter issues not covered here:

*   Join our [Discord community](https://discord.gg/roocode) for real-time support
*   Submit issues on [GitHub](https://github.com/RooVetGit/Roo-Code/issues)
*   Visit our [Reddit community](https://www.reddit.com/r/RooCode)