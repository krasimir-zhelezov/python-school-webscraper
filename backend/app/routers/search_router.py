from fastapi import APIRouter, Depends, HTTPException

from app.services.webscraper import WebScraper
from app.services.gemini_bot import GeminiBot

search_router = APIRouter()

@search_router.get("/search/math/{query}")
async def search_for_math(query):
    webscraper = WebScraper()
    raw_data = webscraper.search_for_math(query)
    
    gemini_bot = GeminiBot()
    data = gemini_bot.process_data(raw_data)
    
    return data

@search_router.get("/search/bg/{query}")
async def search_for_bulgarian(query):
    webscraper = WebScraper()
    raw_data = webscraper.search_for_bulgarian(query)
    
    gemini_bot = GeminiBot()
    data = gemini_bot.process_data(raw_data)
    
    return data