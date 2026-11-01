MCP (Model Context Protocol) – Development Environment Setup
📌 Overview

This repository contains the development environment setup for learning and building MCP (Model Context Protocol) servers using Python.

MCP (Model Context Protocol) is an open protocol that allows AI applications to connect with external tools, resources, and services through a standardized architecture.

The objective of this project is to understand MCP architecture, configure the required development tools, and prepare the environment for building local MCP servers.

🏗️ 1. MCP Architecture

MCP consists of three main components:

Component	Description
Host	The AI application, such as Claude Desktop or a custom AI agent.
Client	Lives inside the host and manages communication with an MCP server.
Server	Provides tools, resources, and prompts to the AI application.
Communication Flow
text
        AI Model
           |
           v
       MCP Client
           |
           v
       MCP Server
           |
           v
     External Tools
           |
           v
       MCP Result
           |
           v
       MCP Client
           |
           v
        AI Model

Example

Consider an AI assistant that books a restaurant table through Swiggy:

Host: Claude Desktop
Client: MCP Client inside Claude
Server: Swiggy MCP Server
Action: Restaurant table booking
Result: Booking confirmation returned to Claude.

The MCP architecture allows AI applications to connect with multiple tools without rewriting the entire agent.

🔌 2. MCP Communication Transports

MCP supports different transport mechanisms for communication between clients and servers.

A. STDIO Transport
Used for local MCP servers.
The client launches the server as a child process.
Communication happens through standard input and standard output.
Suitable for local development and tools running on the same machine.
B. Streamable HTTP Transport
Used when MCP servers are hosted remotely.
Communication happens over HTTP.
Supports streaming responses using Server-Sent Events (SSE).
Suitable for remote MCP servers and distributed applications.

Note: The older HTTP+SSE transport has been superseded by Streamable HTTP. SSE remains available as part of the streaming mechanism.

🧰 3. Technologies and Tools Required

The following tools are required for this development environment:

Tool	Purpose
Python 3.12+	Programming language for developing MCP servers.
uv	Python project and dependency management.
MCP Python SDK	Provides MCP server and client functionality.
ipykernel	Enables Jupyter Notebook kernel support.
Node.js LTS	Required to run MCP Inspector.
npm	Node.js package manager.
npx	Executes MCP Inspector.
Visual Studio Code	Code editor and development environment.
Claude Desktop	MCP host for testing local servers.
🐍 4. Python Environment Setup
Step 1: Install Python 3.12

Install Python using uv:

bash
uv python install 3.12


Verify the installation:

bash
python --version

Step 2: Create the Project Directory
bash
mkdir learning-mcp
cd learning-mcp

Step 3: Initialize the Python Project
bash
uv init --python 3.12


This initializes a Python project and creates the necessary configuration files.

Step 4: Install MCP Python SDK
bash
uv add "mcp[cli]"


This installs:

MCP Python SDK
MCP CLI
Required dependencies for MCP development.

Important: Use quotation marks around "mcp[cli]" to avoid shell interpretation issues.

Step 5: Install IPython Kernel
bash
uv add --dev ipykernel


This enables Jupyter Notebook kernel support.

💻 5. Visual Studio Code Configuration

Open the project in VS Code:

bash
code .


Select the Python interpreter:

Open Visual Studio Code.
Press Ctrl + Shift + P (Windows/Linux) or Cmd + Shift + P (Mac).
Search for Python: Select Interpreter.
Select the Python interpreter inside the project's .venv directory.

This ensures that VS Code uses the correct project environment.

🟢 6. Node.js Installation

MCP Inspector requires Node.js.

It is recommended to install Node.js using a version manager.

Windows

Install nvm-windows using its official installer.

macOS

Install Homebrew and use it to install nvm.

Linux

Install nvm using its official installation script.

Install Node.js LTS

After installing nvm, execute:

bash
nvm install --lts


Verify the installation:

bash
node --version
npm --version
npx --version


All three commands should return version information.

Important: npx is required to launch MCP Inspector.

🔍 7. MCP Inspector

MCP Inspector is a development tool used to inspect, test, and debug MCP servers.

It helps developers:

Connect to local MCP servers.
View available tools.
Test tool execution.
Inspect server responses.
Debug MCP communication.

The Inspector will be used in upcoming MCP server development sessions.

🤖 8. Claude Desktop Installation

Claude Desktop will be used as the MCP Host.

It allows us to:

Connect local MCP servers.
Discover available MCP tools.
Interact with MCP servers through an AI assistant.
Test tool execution and responses.

Install Claude Desktop from its official website:

https://claude.com/download

📂 9. Project Structure

The initial project structure will look similar to this:

text
learning-mcp/
│
├── .venv/
│
├── .gitignore
│
├── .python-version
│
├── pyproject.toml
│
├── uv.lock
│
└── README.md


Additional Python files and MCP server implementations will be added in upcoming development sessions.

Note: The .venv directory should not be committed to GitHub.

🧠 10. MCP SDK Capabilities

The MCP SDK provides functionality on both the server and client sides.

Server Capabilities
Capability	Description
Tools	Actions that an AI model can execute.
Resources	Data that an AI application can read.
Prompts	Reusable prompt templates.
Client Capabilities
Capability	Description
Sampling	Allows an MCP server to request an LLM completion through the client.
Roots	Helps define the scope of accessible resources.
Elicitation	Allows servers to request additional information from users through the client.

Important: Sampling is a client capability, not a server capability exposed to the model.

✅ 11. Environment Setup Checklist

Before starting MCP server development, ensure the following requirements are completed:

Python 3.12+ installed.
uv installed and configured.
Python project initialized using uv init.
MCP SDK installed using uv add "mcp[cli]".
ipykernel installed.
VS Code installed.
Correct Python interpreter selected.
Node.js LTS installed using nvm.
Node.js verified using node --version.
npm verified using npm --version.
npx verified using npx --version.
Claude Desktop installed.
Development environment ready for MCP server development.
🎯 12. Learning Objectives

After completing this setup, we will be ready to:

Understand MCP architecture.
Build our first local MCP server using Python.
Create and expose MCP tools.
Test MCP servers using MCP Inspector.
Connect MCP servers with Claude Desktop.
Execute tools through an AI assistant.
Explore remote MCP servers using Streamable HTTP.
📚 13. Useful Resources
Official MCP Documentation
MCP Python SDK – GitHub
MCP Inspector – GitHub
uv Documentation
Node.js Official Website
nvm-windows – GitHub
Visual Studio Code
Claude Desktop
🚀 What's Next?

The development environment is now ready for the next stage of learning.

Next Step: Building Our First Local MCP Server

We will create a Python-based MCP server, expose custom tools, test them using MCP Inspector, and connect the server to Claude Desktop.

👨‍💻 Author

Learning MCP – Generative AI Development

This repository documents my learning journey into Model Context Protocol (MCP), AI agents, tool calling, and building AI-powered applications.