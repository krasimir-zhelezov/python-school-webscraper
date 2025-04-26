from fastapi import APIRouter, Depends, HTTPException

from app.services.webscraper import WebScraper

search_router = APIRouter()

@search_router.get("/search/math/{query}")
async def search_for_math(query):
    webscraper = WebScraper()
    data = webscraper.search_for_math(query)
    
    return data