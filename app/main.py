# app/main.py
from fastapi import FastAPI, HTTPException
from app.services import search_by_date, search_by_title, search_by_abstract

app = FastAPI()


@app.get("/search/date")
async def search_date(publication_date: str):
    return await search_by_date(publication_date)


@app.get("/search/title")
async def search_title(keyword: str):
    return await search_by_title(keyword)


@app.get("/search/abstract")
async def search_abstract(keyword: str):
    return await search_by_abstract(keyword)
