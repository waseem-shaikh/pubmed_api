# tests/test_main.py
import pytest
from fastapi import status

@pytest.mark.asyncio
async def test_search_date_valid(client):
    response = client.get("/search/date", params={"publication_date": "2024-11-09"})
    assert response.status_code == status.HTTP_200_OK
    # Additional checks here based on expected response structure/content

@pytest.mark.asyncio
async def test_search_date_invalid_format(client):
    response = client.get("/search/date", params={"publication_date": "2024-09"})
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Publication date must be in YYYY-MM-DD format."}

@pytest.mark.asyncio
async def test_search_title(client):
    response = client.get("/search/title", params={"keyword": "cancer research"})
    assert response.status_code == status.HTTP_200_OK
    # Additional checks for expected response content

@pytest.mark.asyncio
async def test_search_abstract(client):
    response = client.get("/search/abstract", params={"keyword": "genetic mutations"})
    assert response.status_code == status.HTTP_200_OK
    # Additional checks for expected response content
