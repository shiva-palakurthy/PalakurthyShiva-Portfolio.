# Hello MCP Server

A beginner-friendly Model Context Protocol (MCP) server built using Python and the MCP Python SDK.

This project is part of my GenAI and MCP learning journey.

## Features

The server currently provides calculator tools:

- `add` – Adds two numbers.
- `modulus` – Returns the remainder of a division.

More tools will be added as the project develops.

## Technologies Used

- Python
- Model Context Protocol (MCP)
- UV – Python package and project manager
- Claude Desktop
- MCP Inspector

## Project Structure

```text
learning_mcp/
├── server.py
├── pyproject.toml
├── uv.lock
├── .gitignore
└── README.md
```

## Installation

Clone the repository and navigate to this folder:

```bash
cd MCP/mcp_servers/learning_mcp
```

Install the project dependencies:

```bash
uv sync
```

## Run the MCP Inspector

```bash
uv run mcp dev server.py
```

## Claude Desktop Integration

Configure Claude Desktop to launch the server using UV and the project directory.

## Learning Goals

- Understand MCP architecture.
- Build custom MCP tools using Python.
- Connect local MCP servers to Claude Desktop.
- Test tools using MCP Inspector.
- Develop practical GenAI applications.

## Author

Palakurthy Shiva

---

*This project is actively being developed as part of my MCP learning journey.*