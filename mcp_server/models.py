from typing import List, Optional
from pydantic import BaseModel, Field

class Author(BaseModel):
    authorId: Optional[str] = None
    name: str

class Tldr(BaseModel):
    model: Optional[str] = None
    text: str

class OpenAccessPdf(BaseModel):
    url: str
    status: Optional[str] = None

class Paper(BaseModel):
    paperId: str
    url: Optional[str] = None
    title: str
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
    total: int
    offset: int
    next: Optional[int] = None
    data: List[Paper]

class AuthorDetails(Author):
    affiliations: List[str] = []
    paperCount: int = 0
    citationCount: int = 0
    hIndex: int = 0
    papers: List[Paper] = []
