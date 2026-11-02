from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session
from app.api.crud import create_item, delete_item, get_item, list_items, update_item
from app.db.session import get_db
from app.models import Director
from app.schemas.entities import NamedCreate, NamedRead

router = APIRouter()
@router.get("", response_model=list[NamedRead])
def list_directors(skip: int = Query(0, ge=0), limit: int = Query(100, ge=1, le=100), db: Session = Depends(get_db)): return list_items(db, Director, skip, limit)
@router.get("/{director_id}", response_model=NamedRead)
def get_director(director_id: int, db: Session = Depends(get_db)): return get_item(db, Director, director_id)
@router.post("", response_model=NamedRead, status_code=status.HTTP_201_CREATED)
def create_director(director: NamedCreate, db: Session = Depends(get_db)): return create_item(db, Director, director)
@router.put("/{director_id}", response_model=NamedRead)
def update_director(director_id: int, director: NamedCreate, db: Session = Depends(get_db)): return update_item(db, Director, director_id, director)
@router.delete("/{director_id}")
def delete_director(director_id: int, db: Session = Depends(get_db)): return delete_item(db, Director, director_id)
