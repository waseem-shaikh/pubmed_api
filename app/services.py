# app/services.py
import requests
from fastapi import HTTPException

BASE_URL = "https://api.pubmed.ncbi.nlm.nih.gov/v3"


async def search_by_date(publication_date: str):
    response = requests.get(f"{BASE_URL}/search?date={publication_date}")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error fetching data")
    return response.json()


async def search_by_title(keyword: str):
    response = requests.get(f"{BASE_URL}/search?title={keyword}")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error fetching data")
    return response.json()


async def search_by_abstract(keyword: str):
    response = requests.get(f"{BASE_URL}/search?abstract={keyword}")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error fetching data")
    return response.json()
