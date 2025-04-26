from fastapi import APIRouter, Depends, HTTPException

search_router = APIRouter()

@search_router.get("/search/math/{query}")
async def search_for_math(query):
    return f'searching for {query}'