# Research Buddy MCP Server

A powerful literature review assistant for AI agents, powered by the Semantic Scholar Graph API.

## Features

- **Comprehensive Search**: Find papers by keyword with AI-generated TLDRs.
- **Smart Recommendations**: Discovery of related papers using Semantic Scholar's recommendation engine.
- **Paper Details**: Full metadata, abstracts, and citation counts.
- **Citation Graph**: Explore who cited a paper and what a paper references.
- **Author Analysis**: Detailed profiles of researchers and their work.
- **BibTeX Export**: One-click citation strings for your research papers.
- **PDF Extraction**: Extract plain text from Open Access PDFs for immediate reading.
- **Batch Processing**: Efficiently fetch metadata for multiple papers at once.

## Installation

### Option A: Install from GitHub (recommended)

```bash
pip install git+https://github.com/Usama1002/research-buddy-mcp.git
```

### Option B: Install from source (for development)

```bash
git clone https://github.com/Usama1002/research-buddy-mcp.git
cd research-buddy-mcp
pip install -e .
```

### Configuration

Create a `.env` file or set the environment variable:

```env
SEMANTIC_SCHOLAR_API_KEY=your_api_key_here
```

## Usage

### Claude Desktop

Add this to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "research-buddy": {
      "command": "research-buddy-mcp",
      "env": {
        "SEMANTIC_SCHOLAR_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

### Antigravity (Gemini)

Add the following to `~/.gemini/antigravity/mcp_config.json`:

```json
{
  "mcpServers": {
    "research-buddy": {
      "command": "research-buddy-mcp",
      "args": [],
      "env": {
        "SEMANTIC_SCHOLAR_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

### VS Code

Create a `.vscode/mcp.json` in your project root:

```json
{
  "servers": {
    "research-buddy": {
      "command": "research-buddy-mcp",
      "env": {
        "SEMANTIC_SCHOLAR_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

Alternatively, add it globally in your VS Code `settings.json`:

```json
{
  "mcp": {
    "servers": {
      "research-buddy": {
        "command": "research-buddy-mcp",
        "env": {
          "SEMANTIC_SCHOLAR_API_KEY": "your_api_key_here"
        }
      }
    }
  }
}
```

## Tools Provided

| Tool | Description |
| :--- | :--- |
| `search_papers` | Search for papers by query and year. |
| `get_paper_details` | Get full metadata including abstract and TLDR. |
| `get_related_papers` | Get AI-driven recommendations based on a paper. |
| `get_citations` | List papers that cited a specific work. |
| `get_references` | List papers referenced by a specific work. |
| `get_author_details` | Get author h-index and publication list. |
| `get_paper_bibtex` | Get ready-to-use BibTeX for a paper. |
| `read_pdf_text` | Extract text from an Open Access PDF URL. |

## License
MIT
