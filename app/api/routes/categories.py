from fastapi import APIRouter, HTTPException, status

from app.schemas.category import CategoryCreate, CategoryRead

router = APIRouter()


@router.get("", response_model=list[CategoryRead])
async def list_categories() -> list[CategoryRead]:
    return []


@router.get("/{category_id}", response_model=CategoryRead)
async def get_category(category_id: int) -> CategoryRead:
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail=f"Category lookup is not implemented yet: {category_id}",
    )


@router.post("", response_model=CategoryRead, status_code=status.HTTP_501_NOT_IMPLEMENTED)
async def create_category(category: CategoryCreate) -> CategoryRead:
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Category creation is not implemented yet",
    )
