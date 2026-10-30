from fastapi import APIRouter, HTTPException, status

from app.schemas.director import DirectorCreate, DirectorRead

router = APIRouter()


@router.get("", response_model=list[DirectorRead])
async def list_directors() -> list[DirectorRead]:
    return []


@router.get("/{director_id}", response_model=DirectorRead)
async def get_director(director_id: int) -> DirectorRead:
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail=f"Director lookup is not implemented yet: {director_id}",
    )


@router.post("", response_model=DirectorRead, status_code=status.HTTP_501_NOT_IMPLEMENTED)
async def create_director(director: DirectorCreate) -> DirectorRead:
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Director creation is not implemented yet",
    )
