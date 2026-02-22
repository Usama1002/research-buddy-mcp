from typing import List, Optional
from pydantic import BaseModel, Field


class Author(BaseModel):
    authorId: Optional[str] = None
    name: Optional[str] = "Unknown"


class Tldr(BaseModel):
    model: Optional[str] = None
    text: Optional[str] = ""


class OpenAccessPdf(BaseModel):
    url: Optional[str] = None
    status: Optional[str] = None


class Paper(BaseModel):
    paperId: Optional[str] = None
    url: Optional[str] = None
    title: Optional[str] = "Untitled"
    abstract: Optional[str] = None
    venue: Optional[str] = None
    year: Optional[int] = None
    citationCount: Optional[int] = 0
    referenceCount: Optional[int] = 0
    influentialCitationCount: Optional[int] = 0
    authors: List[Author] = []
    tldr: Optional[Tldr] = None
    openAccessPdf: Optional[OpenAccessPdf] = None
    citationStyles: Optional[dict] = None


class PaperSearchResult(BaseModel):
    total: Optional[int] = 0
    offset: Optional[int] = 0
    next: Optional[int] = None
    data: List[Paper] = []  # Default to empty list when API returns no results


class AuthorDetails(BaseModel):
    authorId: Optional[str] = None
    name: Optional[str] = "Unknown"
    affiliations: List[str] = []
    paperCount: int = 0
    citationCount: int = 0
    hIndex: int = 0
    papers: List[Paper] = []
