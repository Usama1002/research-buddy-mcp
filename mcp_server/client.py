import os
import requests
import time
from typing import List, Optional, Dict, Any
from .models import Paper, PaperSearchResult, AuthorDetails, Author
from dotenv import load_dotenv

load_dotenv()

class SemanticScholarClient:
    BASE_URL = "https://api.semanticscholar.org/graph/v1"
    REC_URL = "https://api.semanticscholar.org/recommendations/v1"

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("SEMANTIC_SCHOLAR_API_KEY")
        self.headers = {"x-api-key": self.api_key} if self.api_key else {}

    def _make_request(self, method: str, url: str, params: Optional[Dict] = None, json_data: Optional[Dict] = None) -> Any:
        """Handles HTTP requests with basic retry logic."""
        for attempt in range(3):
            try:
                response = requests.request(method, url, headers=self.headers, params=params, json=json_data)
                if response.status_code == 429:
                    # Rate limited - wait and retry
                    time.sleep(2 ** attempt)
                    continue
                response.raise_for_status()
                data = response.json()
                # Guard against non-dict responses (e.g. empty arrays)
                return data if data is not None else {}
            except requests.exceptions.RequestException as e:
                if attempt == 2:
                    raise Exception(f"API request failed: {str(e)}")
                time.sleep(1)
        return {}

    def search_papers(self, query: str, limit: int = 10, year: Optional[str] = None, fields: str = "paperId,title,year,authors,tldr,citationCount") -> PaperSearchResult:
        url = f"{self.BASE_URL}/paper/search"
        params = {"query": query, "limit": limit, "fields": fields}
        if year: params["year"] = year
        data = self._make_request("GET", url, params=params)
        if not isinstance(data, dict):
            return PaperSearchResult()
        return PaperSearchResult(**data)

    def get_paper_details(self, paper_id: str, fields: str = "paperId,title,abstract,tldr,authors,year,venue,citationCount,referenceCount,openAccessPdf,url,influentialCitationCount,citationStyles") -> Paper:
        url = f"{self.BASE_URL}/paper/{paper_id}"
        params = {"fields": fields}
        data = self._make_request("GET", url, params=params)
        return Paper(**data)

    def get_recommendations(self, paper_id: str, limit: int = 10, fields: str = "paperId,title,year,authors,citationCount") -> List[Paper]:
        url = f"{self.REC_URL}/papers"
        params = {"fields": fields}
        payload = {"positivePaperIds": [paper_id], "limit": limit}
        data = self._make_request("POST", url, params=params, json_data=payload)
        return [Paper(**p) for p in data.get("recommendedPapers", [])]

    def get_citations(self, paper_id: str, limit: int = 20, offset: int = 0, fields: str = "paperId,title,year,authors") -> List[Paper]:
        url = f"{self.BASE_URL}/paper/{paper_id}/citations"
        formatted_fields = ",".join([f"citingPaper.{f.strip()}" for f in fields.split(",")])
        params = {"fields": formatted_fields, "limit": limit, "offset": offset}
        data = self._make_request("GET", url, params=params)
        return [Paper(**p["citingPaper"]) for p in data.get("data", []) if p.get("citingPaper")]

    def get_references(self, paper_id: str, limit: int = 20, offset: int = 0, fields: str = "paperId,title,year,authors") -> List[Paper]:
        url = f"{self.BASE_URL}/paper/{paper_id}/references"
        formatted_fields = ",".join([f"citedPaper.{f.strip()}" for f in fields.split(",")])
        params = {"fields": formatted_fields, "limit": limit, "offset": offset}
        data = self._make_request("GET", url, params=params)
        return [Paper(**p["citedPaper"]) for p in data.get("data", []) if p.get("citedPaper")]

    def get_author_details(self, author_id: str, fields: str = "name,affiliations,paperCount,citationCount,hIndex,papers.title,papers.year,papers.paperId") -> AuthorDetails:
        url = f"{self.BASE_URL}/author/{author_id}"
        params = {"fields": fields}
        data = self._make_request("GET", url, params=params)
        return AuthorDetails(**data)

    def batch_get_papers(self, paper_ids: List[str], fields: str = "paperId,title,year,authors,tldr,citationCount") -> List[Paper]:
        url = f"{self.BASE_URL}/paper/batch"
        params = {"fields": fields}
        payload = {"ids": paper_ids}
        data = self._make_request("POST", url, params=params, json_data=payload)
        if not isinstance(data, list):
            return []
        return [Paper(**p) for p in data if isinstance(p, dict)]
