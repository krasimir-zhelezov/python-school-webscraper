from fastapi import APIRouter, Depends, HTTPException, Request

from app.services.webscraper import WebScraper
from app.services.gemini_bot import GeminiBot

search_router = APIRouter()

@search_router.get("/search/math/{query}")
async def search_for_math(query, request: Request):
    webscraper = request.app.state.webscraper
    gemini_bot = request.app.state.gemini_bot
    
    raw_data = webscraper.search_for_math(query)
    
    data = gemini_bot.process_data(raw_data)
    
    return data

@search_router.get("/search/bg/{query}")
async def search_for_bulgarian(query, request: Request):
    webscraper = request.app.state.webscraper
    gemini_bot = request.app.state.gemini_bot
    
    raw_data = webscraper.search_for_bulgarian(query)
    
    data = gemini_bot.process_data(raw_data)
    
    return data