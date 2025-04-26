from fastapi import FastAPI
from app.routers.search_router import search_router
from app.services.gemini_bot import GeminiBot
from app.services.webscraper import WebScraper
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="FastAPI with Selenium & Gemini")
app.state.webscraper = WebScraper()
app.state.gemini_bot = GeminiBot()

app.include_router(search_router, prefix='/api')