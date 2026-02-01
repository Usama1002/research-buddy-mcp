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

### 1. Environment Setup

Ensure you have Python 3.10+ installed.

```bash
git clone <this-repo>
cd research-buddy-mcp
pip install -r requirements.txt
```

### 2. Configuration

Create a `.env` file in the root directory (or use the one provided):

```env
SEMANTIC_SCHOLAR_API_KEY=your_api_key_here
```

### 3. Usage with Claude Desktop

Add this to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "research-buddy": {
      "command": "python3",
      "args": ["-m", "mcp_server.server"],
      "env": {
        "SEMANTIC_SCHOLAR_API_KEY": "ecfDV5IDYg2d52CPQz1IU39TiPRdxGW71v4FVJzd"
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
