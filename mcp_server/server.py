from typing import List, Optional
from fastmcp import FastMCP
from .client import SemanticScholarClient
from .utils import extract_text_from_pdf_url

# Initialize FastMCP server
mcp = FastMCP("Research Buddy")
client = SemanticScholarClient()

@mcp.tool()
def search_papers(query: str, limit: int = 10, year: Optional[str] = None):
    """
    Search for academic papers by query.
    - query: Keyword or natural language query.
    - limit: Number of results (default 10).
    - year: Year range (e.g. '2020-2024') or specific year.
    """
    return client.search_papers(query=query, limit=limit, year=year)

@mcp.tool()
def get_paper_details(paper_id: str):
    """
    Get full metadata for a specific paper.
    - paper_id: Semantic Scholar ID, DOI, arXiv ID, etc.
    """
    return client.get_paper_details(paper_id)

@mcp.tool()
def get_related_papers(paper_id: str, limit: int = 10):
    """
    Get recommended papers based on a seed paper ID.
    - paper_id: The ID of the paper to find recommendations for.
    - limit: Number of results (default 10).
    """
    return client.get_recommendations(paper_id, limit=limit)

@mcp.tool()
def get_citations(paper_id: str, limit: int = 20):
    """
    Retrieve papers that cited the given paper.
    - paper_id: The paper ID.
    - limit: Max results (default 20).
    """
    return client.get_citations(paper_id, limit=limit)

@mcp.tool()
def get_references(paper_id: str, limit: int = 20):
    """
    Retrieve papers that this paper references.
    - paper_id: The paper ID.
    - limit: Max results (default 20).
    """
    return client.get_references(paper_id, limit=limit)

@mcp.tool()
def get_author_details(author_id: str):
    """
    Get author profile and their papers.
    - author_id: Semantic Scholar Author ID.
    """
    return client.get_author_details(author_id)

@mcp.tool()
def get_paper_bibtex(paper_id: str) -> str:
    """
    Get the BibTeX citation for a paper.
    - paper_id: The paper ID.
    """
    details = client.get_paper_details(paper_id, fields="citationStyles,title")
    if details.citationStyles:
        return details.citationStyles.get("bibtex", "BibTeX not available for this paper.")
    return "BibTeX not available for this paper."

@mcp.tool()
def batch_get_papers(paper_ids: List[str]):
    """
    Retrieve details for multiple papers at once.
    - paper_ids: List of paper IDs.
    """
    return client.batch_get_papers(paper_ids)

@mcp.tool()
def read_pdf_text(url: str, max_chars: int = 10000) -> str:
    """
    Download and extract text from an open-access PDF.
    - url: Direct URL to the PDF.
    - max_chars: Max characters to extract (default 10000).
    """
    return extract_text_from_pdf_url(url, max_chars=max_chars)

if __name__ == "__main__":
    mcp.run()
