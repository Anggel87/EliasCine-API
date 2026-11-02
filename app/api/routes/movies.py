from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session
from app.api.crud import create_item, delete_item, get_item, list_items, update_item
from app.db.session import get_db
from app.models import Movie
from app.schemas.entities import MovieCreate, MovieRead

router = APIRouter()
@router.get("", response_model=list[MovieRead])
def list_movies(skip: int = Query(0, ge=0), limit: int = Query(100, ge=1, le=100), db: Session = Depends(get_db)): return list_items(db, Movie, skip, limit)
@router.get("/{movie_id}", response_model=MovieRead)
def get_movie(movie_id: int, db: Session = Depends(get_db)): return get_item(db, Movie, movie_id)
@router.post("", response_model=MovieRead, status_code=status.HTTP_201_CREATED)
def create_movie(movie: MovieCreate, db: Session = Depends(get_db)): return create_item(db, Movie, movie)
@router.put("/{movie_id}", response_model=MovieRead)
def update_movie(movie_id: int, movie: MovieCreate, db: Session = Depends(get_db)): return update_item(db, Movie, movie_id, movie)
@router.delete("/{movie_id}")
def delete_movie(movie_id: int, db: Session = Depends(get_db)): return delete_item(db, Movie, movie_id)
