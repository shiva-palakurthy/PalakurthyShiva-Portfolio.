# Hello MCP – Python Calculator Server

## 1. Project Overview

This is my first Python-based Model Context Protocol (MCP) server, built using FastMCP.

The project demonstrates the three main MCP capabilities:

1. Tools
2. Resources
3. Prompts

**Server Name:** `hello-mcp`

**Programming Language:** Python

**MCP Framework:** FastMCP

**Development Tools:** VS Code, Python, uv, Node.js, Git and MCP Inspector

---

## 2. Project Structure

```text
learning_mcp/
│
├── server.py
├── README.md
└── .gitignore
```

The `server.py` file contains the MCP server, tools, resources and prompts.

The `.gitignore` file excludes unnecessary generated files.

```gitignore
__pycache__/
*.pyc
.venv/
```

---

## 3. Understanding MCP Architecture

```text
              Claude Desktop
                    |
                MCP Host
                    |
                MCP Client
                    |
                MCP Server
                 hello-mcp
                    |
          ----------------------
          |          |         |
         Tools    Resources  Prompts
```

### Components

| Component | Description |
|---|---|
| Host | Application that provides the environment for using MCP, such as Claude Desktop |
| Client | Communicates with the MCP server |
| Server | Exposes tools, resources and prompts |
| FastMCP | Python framework for building MCP servers |
| STDIO | Communication transport used for local server connections |

### Three main MCP capabilities

| Capability | Purpose | Example |
|---|---|---|
| Tools | Perform actions | Addition, multiplication |
| Resources | Provide information | Mathematical formulas |
| Prompts | Provide reusable instructions | Mathematics teacher |

**Remember:**

- Tools = Actions
- Resources = Data
- Prompts = Instructions

---

# 4. Installing and Checking Development Tools

The following commands help verify the installed development environment.

### Check executable locations

```powershell
where.exe python
where.exe uv
where.exe git
where.exe node
where.exe npx
```

### Check versions

```powershell
python --version
uv --version
git --version
node --version
npm --version
npx --version
```

### Check environment variables

```powershell
$env:PATH
$env:APPDATA
$env:LOCALAPPDATA
```

**Important:**

- `where.exe` locates executable files.
- `--version` displays the installed version.
- `PATH` contains directories where Windows searches for executable files.
- `APPDATA` and `LOCALAPPDATA` identify application data directories.

---

# 5. Creating the MCP Server

### Import FastMCP

```python
from mcp.server.fastmcp import FastMCP
```

This imports FastMCP from the Python MCP package.

### Initialize the server

```python
mcp = FastMCP("hello-mcp")
```

This creates an MCP server named `hello-mcp`.

---

# 6. MCP Tools

Tools allow Claude to call functions exposed by the MCP server.

We implemented the following mathematical tools.

| No. | Tool | Purpose |
|---|---|---|
| 1 | `add()` | Adds two numbers |
| 2 | `modulus()` | Returns the remainder |
| 3 | `subtract()` | Subtracts two numbers |
| 4 | `multiply()` | Multiplies two numbers |
| 5 | `divide()` | Divides two numbers |
| 6 | `power()` | Calculates the power |
| 7 | `square()` | Calculates the square |
| 8 | `is_even()` | Checks whether a number is even |
| 9 | `multiplication_table()` | Generates a multiplication table |
| 10 | `number_factors()` | Finds factors of a number |

### 6.1 Addition

```python
@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers and return the result."""
    return a + b
```

Example:

Input: 10, 20

Output: 30

### 6.2 Modulus

```python
@mcp.tool()
def modulus(a: float, b: float) -> float:
    """Return the remainder of a divided by b."""
    return a % b
```

Example:

10 % 3 = 1

### 6.3 Subtraction

```python
@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract the second number from the first."""
    return a - b
```

Example:

20 - 10 = 10

### 6.4 Multiplication

```python
@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b
```

Example:

5 × 4 = 20

### 6.5 Division

```python
@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide the first number by the second."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
```

This function uses an `if` condition to prevent division by zero.

### 6.6 Power

```python
@mcp.tool()
def power(a: float, b: float) -> float:
    """Calculate the first number raised to the power of the second."""
    return a ** b
```

Example:

2 ** 3 = 8

### 6.7 Square

```python
@mcp.tool()
def square(a: float) -> float:
    """Return the square of a number."""
    return a ** 2
```

Example:

5 ** 2 = 25

### 6.8 Even Number Checker

```python
@mcp.tool()
def is_even(number: int) -> bool:
    """Check whether a number is even."""
    return number % 2 == 0
```

Example:

Input: 10

Output: True

### 6.9 Multiplication Table

```python
@mcp.tool()
def multiplication_table(number: int) -> str:
    """Generate a multiplication table from 1 to 10."""

    table = []

    for i in range(1, 11):
        result = number * i
        table.append(f"{number} x {i} = {result}")

    return "\n".join(table)
```

Important Python concepts:

- `for` – Repeats a block of code.
- `range(1, 11)` – Generates numbers from 1 to 10.
- `append()` – Adds an item to a list.
- `f-string` – Inserts variables into strings.
- `join()` – Combines strings using a separator.
- `\n` – Creates a new line.

### 6.10 Number Factors

```python
@mcp.tool()
def number_factors(number: int) -> list[int]:
    """Find all factors of a number."""

    factors = []

    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)

    return factors
```

Example:

Input: 12

Output: `[1, 2, 3, 4, 6, 12]`

Important: The returned variable must be `factors`, not `factorse`.

---

# 7. MCP Resources

Resources provide information or data that an MCP client can read.

We created two mathematical resources.

## 7.1 Mathematical Formulas

**Resource URI:**

`math://formulas`

```python
@mcp.resource("math://formulas")
def mathematical_formulas() -> str:
    """Provide commonly used mathematical formulas."""

    return """
    MATHEMATICAL FORMULAS

    1. Addition: a + b
    2. Subtraction: a - b
    3. Multiplication: a * b
    4. Division: a / b
    5. Modulus: a % b
    6. Power: a ** b
    7. Square: a ** 2
    8. Even Number: number % 2 == 0
    """
```

Purpose:

Provides mathematical formulas to Claude.

## 7.2 Mathematical Rules

**Resource URI:**

`math://rules`

```python
@mcp.resource("math://rules")
def mathematical_rules() -> str:
    """Provide basic mathematical rules."""

    return """
    MATHEMATICAL RULES

    1. Division by zero is not allowed.
    2. A number is even if divisible by 2.
    3. A number is odd if not divisible by 2.
    4. Factors divide a number without a remainder.
    5. Square means multiplying a number by itself.
    6. Modulus returns the remainder after division.
    """
```

Purpose:

Provides mathematical rules and information to Claude.

### Important Resource concepts

- `@mcp.resource()` registers a function as a resource.
- A URI identifies the resource.
- A resource function returns information.
- Claude can read the resource contents.

---

# 8. MCP Prompts

Prompts provide reusable instruction templates to the MCP client.

We created three prompts.

## 8.1 Mathematics Teacher

**Prompt name:** `math_teacher`

```python
@mcp.prompt()
def math_teacher(topic: str) -> str:
    """Generate instructions for teaching a mathematical topic."""

    return f"""
    Act as a friendly mathematics teacher.

    Teach me about: {topic}

    Follow these steps:
    1. Explain the concept in simple English.
    2. Explain the formula.
    3. Give three practical examples.
    4. Show the calculations step by step.
    5. Give me two practice questions.
    """
```

Example argument:

`topic = Modulus`

Purpose:

Instructs Claude to teach mathematical topics with examples.

## 8.2 Calculation Explainer

**Prompt name:** `calculation_explainer`

```python
@mcp.prompt()
def calculation_explainer(expression: str) -> str:
    """Generate instructions for explaining a calculation."""

    return f"""
    Explain this mathematical expression: {expression}

    Follow these steps:
    1. Identify the mathematical operation.
    2. Explain the formula.
    3. Show the calculation step by step.
    4. Provide the final answer.
    5. Explain the result in simple English.
    """
```

Example argument:

`expression = 25 ** 3`

Purpose:

Instructs Claude to explain a calculation step by step.

## 8.3 Mathematics Quiz

**Prompt name:** `math_quiz`

```python
@mcp.prompt()
def math_quiz(difficulty: str = "easy") -> str:
    """Generate instructions for a mathematics quiz."""

    return f"""
    Act as a mathematics quiz master.

    Difficulty level: {difficulty}

    Instructions:
    1. Generate five mathematical questions.
    2. Include addition, subtraction, multiplication,
       division and modulus.
    3. Ask one question at a time.
    4. Wait for my answer.
    5. Check my answer and explain any mistakes.
    """
```

Example argument:

`difficulty = medium`

Purpose:

Instructs Claude to conduct a mathematics quiz.

### Important Prompt concepts

- `@mcp.prompt()` registers a function as an MCP prompt.
- Prompt functions can accept arguments.
- `f"""..."""` is an f-string.
- Prompts provide reusable instructions.
- Prompts do not automatically execute tools or read resources.

---

# 9. Difference Between Tools, Resources and Prompts

| Feature | Tools | Resources | Prompts |
|---|---|---|---|
| Main purpose | Perform actions | Provide information | Provide instructions |
| Registration | `@mcp.tool()` | `@mcp.resource()` | `@mcp.prompt()` |
| Identifier | Tool name | Resource URI | Prompt name |
| Example | `add()` | `math://formulas` | `math_teacher` |

### Example workflow

Suppose the user asks:

"Teach me modulus with an example."

A possible workflow:

1. Claude uses the `math_teacher` prompt for teaching instructions.
2. Claude reads `math://formulas` for mathematical information.
3. Claude calls the `modulus` tool if a calculation is needed.
4. Claude explains the result.

Claude decides which available capabilities to use based on the request.

---

# 10. Running the MCP Server

Our server starts with:

```python
if __name__ == "__main__":
    mcp.run()
```

Explanation:

- `__name__` is a special Python variable.
- When the file is executed directly, its value is `"__main__"`.
- `mcp.run()` starts the MCP server.

Run the server directly using:

```powershell
uv run python server.py
```

---

# 11. MCP Inspector

MCP Inspector is a development tool used to test MCP servers.

### Start MCP Inspector

Open the terminal in the `learning_mcp` directory.

Run:

```powershell
npx -y @modelcontextprotocol/inspector uv run python server.py
```

### Command explanation

| Command | Meaning |
|---|---|
| `npx` | Executes an npm package |
| `-y` | Automatically accepts the package installation prompt |
| `@modelcontextprotocol/inspector` | MCP Inspector package |
| `uv run` | Runs a command in the project's Python environment |
| `python server.py` | Executes the MCP server |

Open the local URL displayed in the terminal.

Configure STDIO transport if the Inspector asks for connection details.

### Inspector tabs

**Tools**

Expected tools:

- add
- modulus
- subtract
- multiply
- divide
- power
- square
- is_even
- multiplication_table
- number_factors

**Resources**

Expected resources:

- `math://formulas`
- `math://rules`

**Prompts**

Expected prompts:

- `math_teacher`
- `calculation_explainer`
- `math_quiz`

### Testing

Tools:

- Add 10 and 20.
- Calculate 25 raised to the power of 3.
- Find factors of 24.

Resources:

- Read `math://formulas`.
- Read `math://rules`.

Prompts:

- Run `math_teacher` with `Modulus`.
- Run `calculation_explainer` with `25 ** 3`.
- Run `math_quiz` with `medium`.

---

# 12. Connecting MCP Server to Claude Desktop

Claude Desktop can connect to a local MCP server using its configuration file.

### Configuration file location

```text
%APPDATA%\Claude\claude_desktop_config.json
```

Open it using PowerShell:

```powershell
notepad "$env:APPDATA\Claude\claude_desktop_config.json"
```

### Example configuration

```json
{
  "mcpServers": {
    "hello-mcp": {
      "command": "uv",
      "args": [
        "--directory",
        "C:\\LearningZone\\OpenTrail\\PalakurthyShiva-Portfolio\\MCP\\mcp_servers\\learning_mcp",
        "run",
        "python",
        "server.py"
      ]
    }
  }
}
```

Explanation:

- `mcpServers` – Contains the configured MCP servers.
- `hello-mcp` – Name assigned to the server.
- `command` – Executable used to start the server.
- `args` – Arguments passed to the executable.
- `--directory` – Specifies the project directory.
- `run` – Runs the Python application using uv.
- `python server.py` – Executes the server file.

After saving the configuration, restart Claude Desktop.

**Important:** Use escaped backslashes (`\\`) in Windows paths inside JSON.

---

# 13. Git Commands

### Check Git status

```bash
git status
```

Displays modified, staged and untracked files.

### Stage changes

```bash
git add .
```

Stages changes in the current repository.

### Commit changes

```bash
git commit -m "Add mathematical resources and prompts to MCP calculator server"
```

Creates a commit with a descriptive message.

### Push changes

```bash
git push origin main
```

Uploads committed changes to the remote GitHub repository.

### Pull changes

```bash
git pull origin main
```

Downloads and integrates changes from the remote main branch.

### Check remote repository

```bash
git remote -v
```

Displays configured remote repositories.

### Check line-ending configuration

```bash
git config --get core.autocrlf
```

Checks Git's automatic line-ending conversion setting.

---

# 14. Understanding LF and CRLF

Git may display this warning:

```text
warning: LF will be replaced by CRLF
the next time Git touches the file
```

### Difference

| Type | Meaning | Common usage |
|---|---|---|
| LF | Line Feed (`\n`) | Linux and macOS |
| CRLF | Carriage Return + Line Feed (`\r\n`) | Windows |

This is a line-ending warning, not a Python or MCP error.

Git can automatically convert line endings between the working directory and repository.

---

# 15. Troubleshooting

### Issue 1: Tool not appearing

Check whether the function has:

```python
@mcp.tool()
```

### Issue 2: Resource not appearing

Check whether the function has:

```python
@mcp.resource("math://formulas")
```

### Issue 3: Prompt not appearing

Check whether the function has:

```python
@mcp.prompt()
```

Make sure the function is defined before:

```python
if __name__ == "__main__":
    mcp.run()
```

Restart the server after changing code.

### Issue 4: Failed to save pagination setting

MCP Inspector may show:

```text
Failed to save pagination setting
```

This can be an Inspector interface or setting issue. It does not necessarily mean the MCP server has failed.

Check the connection and server capabilities separately.

### Issue 5: Python NameError

Incorrect:

```python
return factorse
```

Correct:

```python
return factors
```

### Issue 6: Multiplication table not appearing

Make sure the function has the tool decorator:

```python
@mcp.tool()
def multiplication_table(number: int) -> str:
```

### Issue 7: Python cache files appearing in Git

Create `.gitignore`:

```gitignore
__pycache__/
*.pyc
.venv/
```

If cache files were already staged:

```bash
git restore --staged -- __pycache__/
```

If they are already tracked, use:

```bash
git rm -r --cached __pycache__
```

---

# 16. Learning Outcomes

By working on this project, I have learned:

1. What MCP is and why it is used.
2. How to create a Python MCP server using FastMCP.
3. How to create and register MCP tools.
4. How to create resources using `@mcp.resource()`.
5. How to create prompts using `@mcp.prompt()`.
6. How to use Python functions, loops, conditions and lists.
7. How to use Python type annotations and docstrings.
8. How to run an MCP server using uv.
9. How to test an MCP server using MCP Inspector.
10. How to connect a local MCP server to Claude Desktop.
11. How to use Git commands to manage project changes.

---

# 17. Next Learning Goals

Topics to explore next:

- MCP Host, Client and Server in more technical detail.
- STDIO transport and Streamable HTTP.
- Static and dynamic resources.
- Resource templates and URI parameters.
- Prompt arguments and message structures.
- MCP server debugging.
- Connecting external MCP servers.
- Building practical MCP applications.
- Understanding how AI agents use MCP tools.

---

## Final Project Summary

| MCP capability | Implemented | Count |
|---|---|---:|
| Tools | Mathematical operations | 10 |
| Resources | Mathematical formulas and rules | 2 |
| Prompts | Teacher, calculation explainer and quiz | 3 |

**Project:** hello-mcp

**Framework:** FastMCP

**Language:** Python

**Testing:** MCP Inspector

**Host application:** Claude Desktop

