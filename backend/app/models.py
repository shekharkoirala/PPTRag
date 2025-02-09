from pydantic import BaseModel
from typing import Any

class SearchRequest(BaseModel):
    query: str

class SearchResponse(BaseModel):
    results: str

class ComparisonRequest(BaseModel):
    doc1_id: str
    doc2_id: str

class ComparisonResponse(BaseModel):
    comparison: str
