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

### Run the Project

```bash
uv run main.py
```
