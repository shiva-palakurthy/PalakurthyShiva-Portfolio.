# MCP Calculator Server – Learning Notes

## 1. Project Overview

We extended our existing Python MCP server using FastMCP.

**Server name:** `hello-mcp`

**Main objective:** Build a calculator MCP server that supports three MCP capabilities:

1. Tools
2. Resources
3. Prompts

## 2. MCP Architecture

```text
             Claude Desktop
                   |
               MCP Client
                   |
               MCP Server
                hello-mcp
                   |
          ---------------------
          |         |         |
         Tools   Resources  Prompts
```

### Understanding the three capabilities

| Capability | Purpose | Example |
|---|---|---|
| Tools | Perform operations | Addition, subtraction |
| Resources | Provide information | Mathematical formulas |
| Prompts | Provide reusable instructions | Mathematics teacher |

Remember:

- Tools = Actions
- Resources = Data
- Prompts = Instructions

---

# 3. Tools

Tools allow Claude to execute functions provided by an MCP server.

We created the following mathematical tools:

| Tool | Purpose |
|---|---|
| `add()` | Adds two numbers |
| `modulus()` | Returns the remainder |
| `subtract()` | Subtracts two numbers |
| `multiply()` | Multiplies two numbers |
| `divide()` | Divides two numbers |
| `power()` | Calculates the power |
| `square()` | Calculates the square |
| `is_even()` | Checks whether a number is even |
| `multiplication_table()` | Generates a multiplication table |
| `number_factors()` | Finds factors of a number |

### Important Python concepts

**1. Decorator**

```python
@mcp.tool()
```

Registers a Python function as an MCP tool.

**2. Type annotations**

```python
def add(a: float, b: float) -> float:
```

- `a: float` – First input.
- `b: float` – Second input.
- `-> float` – Expected return type.

**3. Docstrings**

```python
"""Add two numbers and return the result."""
```

Provides a description of the tool.

**4. Exception handling**

```python
if b == 0:
    raise ValueError("Cannot divide by zero.")
```

Prevents division by zero.

---

# 4. Resources

Resources provide information or data that an MCP client can read.

We created two resources.

### Resource 1: Mathematical Formulas

URI:

```text
math://formulas
```

Python implementation:

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

### Resource 2: Mathematical Rules

URI:

```text
math://rules
```

Python implementation:

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

Provides mathematical rules and explanations.

### Important Resource concepts

- `@mcp.resource()` registers a function as a resource.
- A URI identifies the resource.
- The function returns information.
- Claude can read the resource contents.

---

# 5. Prompts

Prompts are reusable instruction templates provided by an MCP server.

We created three prompts.

### Prompt 1: Mathematics Teacher

Prompt name:

```text
math_teacher
```

Python implementation:

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

Purpose:

Instructs Claude to teach a mathematical topic with examples.

Example argument:

```text
topic = Modulus
```

### Prompt 2: Calculation Explainer

Prompt name:

```text
calculation_explainer
```

Python implementation:

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

Purpose:

Instructs Claude to explain a mathematical calculation step by step.

Example argument:

```text
expression = 25 ** 3
```

### Prompt 3: Mathematics Quiz

Prompt name:

```text
math_quiz
```

Python implementation:

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

Purpose:

Instructs Claude to conduct a mathematics quiz.

Example argument:

```text
difficulty = medium
```

### Important Prompt concepts

- `@mcp.prompt()` registers a function as an MCP prompt.
- Prompt functions can accept arguments.
- `f"""..."""` is an f-string.
- F-strings allow variables to be inserted into text.
- Prompts provide reusable instructions to Claude.

---

# 6. Difference Between Resource and Prompt

This is an important concept to understand.

| Resource | Prompt |
|---|---|
| Provides information | Provides instructions |
| Identified by a URI | Identified by a prompt name |
| Can return data or text | Returns prompt messages |
| Example: `math://formulas` | Example: `math_teacher` |

Example:

If we ask Claude to teach modulus:

1. The `math_teacher` prompt provides teaching instructions.
2. The `math://formulas` resource provides mathematical information.
3. Claude can use the `modulus` tool to calculate a remainder when needed.

These capabilities can work together, but Claude decides which ones to use. The prompt does not automatically execute tools or read resources.

---

# 7. Running MCP Inspector

MCP Inspector helps us test our MCP server independently of Claude Desktop.

### Command

```powershell
npx -y @modelcontextprotocol/inspector uv run python server.py
```

### Command explanation

| Command | Meaning |
|---|---|
| `npx` | Runs an npm package |
| `-y` | Automatically accepts installation confirmation |
| `@modelcontextprotocol/inspector` | Starts MCP Inspector |
| `uv run` | Runs the application using the project's Python environment |
| `python server.py` | Executes our MCP server |

Open the local Inspector URL shown in the terminal.

Configure the server using STDIO transport if Inspector asks for connection details.

### Inspector tabs

**Tools tab**

Displays registered tools.

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

**Resources tab**

Displays:

- `math://formulas`
- `math://rules`

**Prompts tab**

Displays:

- `math_teacher`
- `calculation_explainer`
- `math_quiz`

### Testing examples

Tools:
- Add 10 and 20.
- Calculate 25 raised to the power of 3.
- Find factors of 24.

Resources:
- Read `math://formulas`.
- Read `math://rules`.

Prompts:
- Run `math_teacher` with topic `Modulus`.
- Run `calculation_explainer` with expression `25 ** 3`.
- Run `math_quiz` with difficulty `medium`.

---

# 8. Troubleshooting

### Issue 1: Function not appearing in Tools

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

Also check that the prompt function is defined before:

```python
if __name__ == "__main__":
    mcp.run()
```

Restart the server after making code changes.

### Issue 4: Failed to save pagination setting

This message may relate to an Inspector interface setting. It does not necessarily indicate an MCP server failure.

Check the server connection and whether the Tools, Resources and Prompts are being discovered.

### Issue 5: Python variable name error

Incorrect:

```python
return factorse
```

Correct:

```python
return factors
```

Also, remember to add `@mcp.tool()` above the multiplication table function.

---

# 9. Important Python Concepts Learned

| Concept | Example | Purpose |
|---|---|---|
| Import | `from mcp.server.fastmcp import FastMCP` | Import functionality |
| Variable | `mcp = FastMCP("hello-mcp")` | Store server object |
| Function | `def add(a, b):` | Define reusable logic |
| Decorator | `@mcp.tool()` | Register an MCP tool |
| Resource decorator | `@mcp.resource()` | Register a resource |
| Prompt decorator | `@mcp.prompt()` | Register a prompt |
| Loop | `for i in range(1, 11)` | Repeat operations |
| Condition | `if b == 0:` | Check conditions |
| List | `factors = []` | Store multiple values |
| Append | `factors.append(i)` | Add an item |
| Return | `return factors` | Return a result |
| F-string | `f"{number}"` | Insert variable values |
| Exception | `raise ValueError()` | Raise an error |

---

# 10. Git Commands

After completing and testing the project:

Check changes:

```bash
git status
```

Stage changes:

```bash
git add .
```

Commit changes:

```bash
git commit -m "Add mathematical resources and prompts to MCP calculator server"
```

Push to GitHub:

```bash
git push origin main
```

Before committing, check that unnecessary files such as `__pycache__` and `.pyc` files are excluded.

---

# 11. Final Learning Summary

Our `hello-mcp` project now covers three major MCP capabilities.

| MCP capability | Implementation | Count |
|---|---|---:|
| Tools | Mathematical operations | 10 |
| Resources | Mathematical formulas and rules | 2 |
| Prompts | Teacher, explainer and quiz | 3 |
