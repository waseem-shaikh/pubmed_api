# tests/test_services.py
import pytest
import responses
from app.services import search_by_date
from fastapi import HTTPException
from datetime import date

# Mock response data
mock_success_response = {
    "header": {
        "type": "esearch",
        "version": "0.3"
    },
    "esearchresult": {
        "count": "34",
        "retmax": "20",
        "retstart": "0",
        "idlist": [
            "39307168", "39307167", "39307166", "39307165", "39307164",
            "39307163", "39307162", "39307161", "39307160", "39307159",
            "39307158", "39307157", "39066740", "39041483", "39016465",
            "39016349", "39016341", "39007685", "39004925", "39003759"
        ],
        "translationset": [],
        "querytranslation": "2024/11/09[Date - Publication]"
    }
}

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmode=json"


@pytest.mark.asyncio
@responses.activate
async def test_search_by_date_success():
    test_date = date(2024, 11, 9)
    # Mock the external API call
    responses.add(
        responses.GET,
        f"{BASE_URL}&term={test_date}[dp]",
        json=mock_success_response,
        status=200,
        headers={"content-type": "application/json"}
    )

    result = await search_by_date(test_date)
    assert result == mock_success_response  # Check if the function returns the mock response correctly


@pytest.mark.asyncio
@responses.activate
async def test_search_by_date_failure():
    test_date = date(2024, 11, 9)
    # Mock a failed response from the API
    responses.add(
        responses.GET,
        f"{BASE_URL}&term={test_date}[dp]",
        json={"detail": "Error fetching data"},
        status=500,
        headers={"content-type": "application/json"}
    )

    with pytest.raises(HTTPException) as exc_info:
        await search_by_date(test_date)
    assert exc_info.value.status_code == 500
    assert exc_info.value.detail == "Error fetching data"
