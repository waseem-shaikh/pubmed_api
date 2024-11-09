import requests
from fastapi import HTTPException
from app.config import BASE_URL
from datetime import date


async def search_by_date(publication_date: date):
    query_url = f"{BASE_URL}&term={publication_date}[dp]"
    response = requests.get(query_url)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error fetching data")
    return response.json()


async def search_by_title(keyword: str):
    # https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=cancer+research
    response = requests.get(f"{BASE_URL}&term={keyword}[Title]")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error fetching data")
    return response.json()


async def search_by_abstract(keyword: str):
    response = requests.get(f"{BASE_URL}&term={keyword}[Abstract]")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error fetching data")
    return response.json()
