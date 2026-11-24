# Filesystem MCP Server – Complete Project Documentation

## 1. Project Overview

**Project Name:** Filesystem MCP Integration with Claude Desktop

**Objective:**
Build and connect a local Filesystem MCP Server to Claude Desktop using Node.js and NPX.

The purpose is to allow Claude AI to interact with local files and directories through MCP tools.

**Environment:**
- Operating System: Windows 10
- MCP Host: Claude Desktop
- MCP Client: Claude Desktop's MCP client
- MCP Server: Filesystem MCP
- Transport: STDIO
- Runtime: Node.js
- Package Manager: NPM
- Package Runner: NPX
- Configuration Format: JSON
- Terminal: PowerShell / VS Code Terminal

---

# 2. Project Architecture

```text
                 USER
                   |
                   v
             CLAUDE DESKTOP
                (Host)
                   |
              MCP Client
                   |
             STDIO Transport
                   |
                   v
            FILESYSTEM MCP
                (Server)
                   |
             Filesystem Tools
                   |
                   v
              WINDOWS OS
                   |
                   v
          LOCAL PROJECT FILES
```

### Component Explanation

| Component | Responsibility |
|---|---|
| User | Gives instructions to Claude |
| Claude Desktop | MCP Host application |
| MCP Client | Establishes communication with the server |
| MCP Server | Exposes filesystem capabilities |
| STDIO | Communication transport |
| Filesystem Tools | Read, write, search and manage files |
| Windows | Provides access to permitted directories |

---

# 3. Development Environment Setup

Before installing the MCP server, I checked the existing development environment.

### 3.1 Check Node.js

```powershell
node --version
```

Purpose:
Checks whether Node.js is installed and available through PATH.

### 3.2 Check NPM

```powershell
npm --version
```

Purpose:
Checks the Node Package Manager version.

### 3.3 Check NPX

```powershell
npx --version
```

Purpose:
Checks whether NPX is available to execute npm packages.

### 3.4 Locate Node.js

```powershell
where.exe node
```

Purpose:
Finds the actual location of the Node.js executable.

### 3.5 Locate NPM

```powershell
where.exe npm
```

Purpose:
Finds the NPM executable location.

### 3.6 Locate NPX

```powershell
where.exe npx
```

Purpose:
Finds the NPX executable location.

Example location:

```text
C:\nvm4w\nodejs\npx
C:\nvm4w\nodejs\npx.cmd
```

### 3.7 Why use where.exe?

`where.exe` searches for executable files in directories listed in the Windows PATH environment variable.

**Important:** In PowerShell, use `where.exe` instead of simply `where`, because `where` is also an alias for the PowerShell `Where-Object` command.

---

# 4. Understand the Important Commands

| Command | Purpose |
|---|---|
| `node --version` | Checks Node.js version |
| `npm --version` | Checks NPM version |
| `npx --version` | Checks NPX version |
| `where.exe node` | Locates Node.js |
| `where.exe npm` | Locates NPM |
| `where.exe npx` | Locates NPX |
| `pwd` | Displays current directory |
| `cd` | Changes directory |
| `mkdir` | Creates a directory |
| `dir` | Lists directory contents |
| `Get-ChildItem` | Lists files and folders in PowerShell |
| `Test-Path` | Checks whether a file or directory exists |
| `Get-Process` | Displays running processes |
| `Ctrl + C` | Stops a running terminal process |
| `exit` | Exits the terminal session |

---

# 5. Understand Windows Paths

### Example 1: Normal Windows path

```text
C:\LearningZone\MCP-Filesystem
```

### Example 2: Windows path inside JSON

```json
"C:\\LearningZone\\MCP-Filesystem"
```

Why double backslashes?

JSON uses the backslash as an escape character.

For example:
- `\n` represents a newline.
- `\t` represents a tab.
- `\\` represents a literal backslash.

Therefore, Windows paths must use escaped backslashes inside JSON strings.

---

# 6. MCP Package Information

**Package Name:**

```text
@modelcontextprotocol/server-filesystem
```

**Execution Method:**

```powershell
npx -y @modelcontextprotocol/server-filesystem
```

### Command Explanation

| Part | Explanation |
|---|---|
| `npx` | Executes an npm package |
| `-y` | Automatically accepts installation confirmation |
| `@modelcontextprotocol` | Package namespace |
| `server-filesystem` | Filesystem MCP server package |

The package can be downloaded and executed through NPX without manually creating the server source code.

---

# 7. Project Directory

My configured directory:

```text
C:\LearningZone\OpenTrail\PalakurthyShiva-Portfolio\MCP\mcp_servers\learning_mcp
```

This is the directory that I provided as the Filesystem MCP server's allowed root.

**Important:** The Filesystem MCP server can access the configured directory and its permitted subdirectories, not unrestricted access to the entire computer.

---

# 8. Claude Desktop Configuration

### Configuration File

```text
%APPDATA%\Claude\claude_desktop_config.json
```

### Open Configuration Using PowerShell

```powershell
notepad "$env:APPDATA\Claude\claude_desktop_config.json"
```

### Final MCP Configuration

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "cmd",
      "args": [
        "/c",
        "C:\\nvm4w\\nodejs\\npx.cmd",
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "C:\\LearningZone\\OpenTrail\\PalakurthyShiva-Portfolio\\MCP\\mcp_servers\\learning_mcp"
      ]
    }
  }
}
```

### Configuration Explanation

| Property | Explanation |
|---|---|
| `mcpServers` | Contains MCP server configurations |
| `filesystem` | Custom server identifier |
| `command` | Command used to launch the server |
| `cmd` | Windows Command Prompt |
| `/c` | Executes the command and exits CMD |
| `npx.cmd` | Windows NPX command script |
| `-y` | Automatically confirms NPX installation |
| Package name | Identifies the Filesystem MCP server |
| Directory path | Specifies the permitted filesystem root |

---

# 9. How to Validate the Configuration

### Check NPX path

```powershell
Test-Path "C:\nvm4w\nodejs\npx.cmd"
```

Expected:

```text
True
```

### Check project directory

```powershell
Test-Path "C:\LearningZone\OpenTrail\PalakurthyShiva-Portfolio\MCP\mcp_servers\learning_mcp"
```

Expected:

```text
True
```

### Validate JSON syntax

```powershell
Get-Content "$env:APPDATA\Claude\claude_desktop_config.json" -Raw | ConvertFrom-Json
```

If valid, PowerShell parses the configuration without a JSON syntax error.

---

# 10. Running the MCP Server

Claude Desktop starts the configured MCP server automatically.

Execution workflow:

1. Open Claude Desktop.
2. Claude reads its MCP configuration.
3. Claude launches the configured command.
4. NPX executes the Filesystem MCP package.
5. The MCP server starts.
6. The server communicates through STDIO.
7. Claude discovers the available MCP tools.
8. Claude can request filesystem operations.

There is no need to manually start a separate terminal process when Claude Desktop launches the configured server.

---

# 11. Filesystem MCP Tools

Some important tools exposed by the server include:

| Tool | Function |
|---|---|
| `read_file` | Reads file contents |
| `read_text_file` | Reads text files |
| `write_file` | Creates or writes files |
| `create_directory` | Creates directories |
| `list_directory` | Lists directory contents |
| `list_allowed_directories` | Lists permitted root directories |
| `search_files` | Searches for files |
| `move_file` | Moves or renames files |
| `get_file_info` | Retrieves file information |
| `delete_file` | Deletes files |

The exact tool list depends on the installed package version.

---

# 12. Practical Testing

After connecting the server, I can test it using Claude Desktop.

### Test 1: List Files

Prompt:

```text
List all files and folders inside my
configured Filesystem MCP directory.
```

### Test 2: Create a File

Prompt:

```text
Create a file named hello.txt
inside my permitted directory.
```

### Test 3: Write Content

Prompt:

```text
Write "My first Filesystem MCP project"
inside hello.txt.
```

### Test 4: Read a File

Prompt:

```text
Read hello.txt and show me its contents.
```

### Test 5: Create a Directory

Prompt:

```text
Create a folder called Python_Practice.
```

### Test 6: Search Files

Prompt:

```text
Search for all Python files inside
my permitted directory.
```

---

# 13. Troubleshooting and Errors

## Issue 1: Incorrect NPX path

Incorrect:

```text
C:\nvm4w\nodejs\npx
```

Correct executable:

```text
C:\nvm4w\nodejs\npx.cmd
```

Use `where.exe npx` to locate the executable.

## Issue 2: Incorrect JSON escaping

Incorrect:

```json
"C:\nvm4w\nodejs\npx.cmd"
```

Correct:

```json
"C:\\nvm4w\\nodejs\\npx.cmd"
```

## Issue 3: Claude Desktop not opening

Troubleshooting performed:

1. Closed Claude Desktop.
2. Checked running Claude processes.
3. Temporarily renamed the configuration file.
4. Checked the Claude logs directory.
5. Located the Claude installation directories.
6. Located multiple Claude executable versions.
7. Tested launching Claude directly.

Useful commands:

```powershell
Get-Process *Claude* -ErrorAction SilentlyContinue
```

```powershell
Get-ChildItem "$env:LOCALAPPDATA\AnthropicClaude" -Filter "Claude.exe" -Recurse
```

```powershell
explorer.exe shell:AppsFolder\com.squirrel.AnthropicClaude.claude
```

## Issue 4: Open Claude configuration

```powershell
notepad "$env:APPDATA\Claude\claude_desktop_config.json"
```

## Issue 5: Check log files

```powershell
Get-ChildItem "$env:APPDATA\Claude\logs" -Recurse -File
```

---

# 14. Important Learning: Client, Server and Tools

### MCP Host
Claude Desktop is the application hosting the MCP integration.

### MCP Client
The MCP client establishes a connection with the MCP server.

### MCP Server
Filesystem MCP exposes filesystem capabilities through the MCP protocol.

### MCP Tools
Tools are operations the AI can request from the server.

### Transport
STDIO is the communication mechanism used between Claude Desktop and this local server.

---

# 15. Project Learning Outcomes

After completing this project, I learned:

1. How to identify Node.js, NPM and NPX installations.
2. How to use `where.exe` to locate executables.
3. How to understand Windows PATH.
4. How to execute an npm package using NPX.
5. How to configure an MCP server using JSON.
6. How to connect a local MCP server to Claude Desktop.
7. How STDIO communication works.
8. How Claude discovers and uses MCP tools.
9. How to troubleshoot JSON and Windows path errors.
10. How to provide restricted local directory access to an AI application.

---

# 16. Future Improvements

- Connect GitHub MCP.
- Connect SQLite MCP.
- Explore MCP Resources.
- Explore MCP Prompts.
- Build custom Python MCP tools.
- Combine multiple MCP servers.
- Develop an AI-powered local project assistant.

---

# 17. Official Learning Resources

- MCP Documentation: https://modelcontextprotocol.io/
- Filesystem MCP: https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem
- Node.js: https://nodejs.org/
- Claude: https://claude.ai/

**Project Status:** Filesystem MCP configuration connected to Claude Desktop.
