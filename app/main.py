from fastapi import FastAPI, HTTPException, Query
from app.services import search_by_date, search_by_title, search_by_abstract

from app.schemas import PublishDateModel

app = FastAPI(swagger_ui_parameters={"defaultModelsExpandDepth": -1})


@app.get("/search/date")
async def search_date(publication_date: str = Query(
        ...,
        description="Publication date in YYYY-MM-DD format.",
        example="2024-11-09"
            )
        ):
    try:
        PublishDateModel(publication_date=publication_date)
    except ValueError:
        raise HTTPException(status_code=404, detail="Publication date must be in YYYY-MM-DD format.")
    return await search_by_date(publication_date)


@app.get("/search/title")
async def search_title(keyword: str = Query(
        ...,
        description="Search by Publication Title keywords",
        example="acl+regeneration"
            )
        ):
    return await search_by_title(keyword)


@app.get("/search/abstract")
async def search_abstract(keyword: str = Query(
        ...,
        description="Search within the Abstracts of Articles",
        example="genetic+mutations"
            )
        ):
    return await search_by_abstract(keyword)
