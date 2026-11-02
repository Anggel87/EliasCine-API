from collections.abc import Callable
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session
from app.api.crud import create_item, delete_item, get_item, list_items, update_item
from app.db.session import get_db
from app.models import Auditorium, MovieScreening, Seat, Ticket, User
from app.schemas.entities import AuditoriumCreate, AuditoriumRead, ScreeningCreate, ScreeningRead, SeatCreate, SeatRead, TicketCreate, TicketRead, UserCreate, UserRead

def crud_router(model, create_schema, read_schema, parameter: str):
    router = APIRouter()
    @router.get("", response_model=list[read_schema])
    def list_route(skip: int = Query(0, ge=0), limit: int = Query(100, ge=1, le=100), db: Session = Depends(get_db)): return list_items(db, model, skip, limit)
    @router.get("/{item_id}", response_model=read_schema)
    def get_route(item_id: int, db: Session = Depends(get_db)): return get_item(db, model, item_id)
    @router.post("", response_model=read_schema, status_code=status.HTTP_201_CREATED)
    def create_route(data: create_schema, db: Session = Depends(get_db)): return create_item(db, model, data)
    @router.put("/{item_id}", response_model=read_schema)
    def update_route(item_id: int, data: create_schema, db: Session = Depends(get_db)): return update_item(db, model, item_id, data)
    @router.delete("/{item_id}")
    def delete_route(item_id: int, db: Session = Depends(get_db)): return delete_item(db, model, item_id)
    return router

users_router = crud_router(User, UserCreate, UserRead, "user_id")
auditoriums_router = crud_router(Auditorium, AuditoriumCreate, AuditoriumRead, "auditorium_id")
seats_router = crud_router(Seat, SeatCreate, SeatRead, "seat_id")
screenings_router = crud_router(MovieScreening, ScreeningCreate, ScreeningRead, "screening_id")
tickets_router = crud_router(Ticket, TicketCreate, TicketRead, "ticket_id")
