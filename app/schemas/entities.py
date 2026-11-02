from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, ConfigDict, Field

class Read(BaseModel):
    id: int
    model_config = ConfigDict(from_attributes=True)

class NamedCreate(BaseModel):
    name: str
class NamedRead(Read, NamedCreate): pass

class MovieCreate(BaseModel):
    title: str = Field(max_length=75)
    director_id: int | None = None
    length: int | None = Field(default=None, ge=0)
    category_id: int | None = None
    movie_summary: str | None = Field(default=None, max_length=255)
    image: str | None = Field(default=None, max_length=255)
class MovieRead(Read, MovieCreate): pass

class UserCreate(BaseModel):
    name: str = Field(max_length=75)
    email: str = Field(max_length=75)
    password: str = Field(min_length=1, max_length=255)
class UserRead(Read):
    name: str
    email: str

class AuditoriumCreate(NamedCreate): pass
class AuditoriumRead(NamedRead): pass
class SeatCreate(BaseModel):
    seat_number: int = Field(ge=0)
    row_label: str | None = Field(default=None, max_length=2)
    auditorium_id: int
class SeatRead(Read, SeatCreate): pass
class ScreeningCreate(BaseModel):
    date: datetime
    movie_id: int
    auditorium_id: int
class ScreeningRead(Read, ScreeningCreate): pass
class TicketCreate(BaseModel):
    user_id: int
    seat_id: int
    movie_screening_id: int
    price: Decimal | None = Field(default=None, ge=0)
class TicketRead(Read, TicketCreate): pass
