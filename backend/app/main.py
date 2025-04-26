from fastapi import FastAPI
from app.routers.search_router import search_router
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="FastAPI with Selenium & Gemini")

app.include_router(search_router, prefix='/api')