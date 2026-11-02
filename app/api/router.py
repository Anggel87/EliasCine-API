from fastapi import APIRouter

from app.api.routes import categories, directors, extra, movies

api_router = APIRouter()
api_router.include_router(movies.router, prefix="/movies", tags=["movies"])
api_router.include_router(directors.router, prefix="/directors", tags=["directors"])
api_router.include_router(categories.router, prefix="/categories", tags=["categories"])
api_router.include_router(extra.users_router, prefix="/users", tags=["users"])
api_router.include_router(extra.auditoriums_router, prefix="/auditoriums", tags=["auditoriums"])
api_router.include_router(extra.seats_router, prefix="/seats", tags=["seats"])
api_router.include_router(extra.screenings_router, prefix="/movie-screenings", tags=["movie-screenings"])
api_router.include_router(extra.tickets_router, prefix="/tickets", tags=["tickets"])
