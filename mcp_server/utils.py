import requests
import io
from typing import Optional
from pypdf import PdfReader

def extract_text_from_pdf_url(url: str, max_chars: int = 10000) -> str:
    """Downloads a PDF from a URL and extracts text."""
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        
        # Check if the response is actually a PDF
        if 'application/pdf' not in response.headers.get('Content-Type', '').lower():
            return "Error: URL does not point to a PDF file."

        pdf_file = io.BytesIO(response.content)
        reader = PdfReader(pdf_file)
        
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
            if len(text) > max_chars:
                text = text[:max_chars] + "... [Truncated]"
                break
        
        return text.strip() or "Error: No text could be extracted from the PDF."
    except Exception as e:
        return f"Error extracting PDF text: {str(e)}"
