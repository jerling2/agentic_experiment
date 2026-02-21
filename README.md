# Agentic Experiment

## Quick Start Guide

### Install `uv`

If you don't have `uv` installed, run:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Or via Homebrew:

```bash
brew install uv
```

### Install Dependencies

Clone the repo and install dependencies using `uv`:

```bash
uv sync
```

This will create a virtual environment and install all required packages specified in `pyproject.toml`.

### Run the Script

```bash
uv run main.py
```

### Run the LangGraph Dev Server

```bash
uv run langgraph dev
```

### Debug with `debugpy`

1. **(VSCode)** Attach the debugger:
   - Open the **Run and Debug** panel (`Ctrl+Shift+D` / `Cmd+Shift+D`)
   - Select **"Python Debugger: Remote Attach"** from the dropdown
   - Press **F5** or click on the "Run and Debug" Icon to attach


2. Instrument the MCP server to listen for a remote `debugpy` on port 5678.
```bash
uv run python -m debugpy --listen 5678 --wait-for-client main.py

>> Starting MCP server '<Server Name>' with transport 'http' on http://127.0.0.1:8000/mcp
```
> Note: if this command hangs, it's most likely waiting to handshake the debugger.


3a. (Optional - Global Download) Download MCP Inspector CLI Tool

In a separate terminal, run:

```bash
npm install -g @modelcontextprotocol/inspector 2>&1
```

then run,

```bash
mcp-inspector http://localhost:8000/mcp
```

3b. (Optional - Single Use) Run MCP Inspector CLI Tool

In a seprate terminal, run:

```bash
npx @modelcontextprotocol/inspector http://localhost:8000/mcp
```

That's about it: set breakpoints in the code, and use the mcp-inspector UI to test the server.