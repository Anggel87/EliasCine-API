from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session
from app.api.crud import create_item, delete_item, get_item, list_items, update_item
from app.db.session import get_db
from app.models import Category
from app.schemas.entities import NamedCreate, NamedRead

router = APIRouter()
@router.get("", response_model=list[NamedRead])
def list_categories(skip: int = Query(0, ge=0), limit: int = Query(100, ge=1, le=100), db: Session = Depends(get_db)): return list_items(db, Category, skip, limit)
@router.get("/{category_id}", response_model=NamedRead)
def get_category(category_id: int, db: Session = Depends(get_db)): return get_item(db, Category, category_id)
@router.post("", response_model=NamedRead, status_code=status.HTTP_201_CREATED)
def create_category(category: NamedCreate, db: Session = Depends(get_db)): return create_item(db, Category, category)
@router.put("/{category_id}", response_model=NamedRead)
def update_category(category_id: int, category: NamedCreate, db: Session = Depends(get_db)): return update_item(db, Category, category_id, category)
@router.delete("/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)): return delete_item(db, Category, category_id)
