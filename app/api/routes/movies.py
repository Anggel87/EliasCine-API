from fastapi import APIRouter, HTTPException, status

from app.schemas.movie import MovieCreate, MovieRead

router = APIRouter()


@router.get("", response_model=list[MovieRead])
async def list_movies() -> list[MovieRead]:
    return []


@router.get("/{movie_id}", response_model=MovieRead)
async def get_movie(movie_id: int) -> MovieRead:
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail=f"Movie lookup is not implemented yet: {movie_id}",
    )


@router.post("", response_model=MovieRead, status_code=status.HTTP_501_NOT_IMPLEMENTED)
async def create_movie(movie: MovieCreate) -> MovieRead:
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Movie creation is not implemented yet",
    )
