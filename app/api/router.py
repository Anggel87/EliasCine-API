from fastapi import APIRouter

from app.api.routes import categories, directors, movies

api_router = APIRouter()
api_router.include_router(movies.router, prefix="/movies", tags=["movies"])
api_router.include_router(directors.router, prefix="/directors", tags=["directors"])
api_router.include_router(categories.router, prefix="/categories", tags=["categories"])
