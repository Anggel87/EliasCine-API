from datetime import datetime
from decimal import Decimal

from sqlalchemy import BigInteger, CHAR, DateTime, ForeignKey, Numeric, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Director(Base):
    __tablename__ = "directors"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)


class Category(Base):
    __tablename__ = "categories"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(25), nullable=False)


class Movie(Base):
    __tablename__ = "movies"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(75), nullable=False)
    director_id: Mapped[int | None] = mapped_column(ForeignKey("directors.id"), nullable=True)
    length: Mapped[int | None] = mapped_column(SmallInteger, nullable=True)
    category_id: Mapped[int | None] = mapped_column(ForeignKey("categories.id"), nullable=True)
    movie_summary: Mapped[str | None] = mapped_column(String(255), nullable=True)
    image: Mapped[str | None] = mapped_column(String(255), nullable=True)


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(75), nullable=False)
    email: Mapped[str] = mapped_column(String(75), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)


class Auditorium(Base):
    __tablename__ = "auditoriums"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(75), nullable=False)


class Seat(Base):
    __tablename__ = "seats"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    seat_number: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    row_label: Mapped[str | None] = mapped_column(CHAR(2), nullable=True)
    auditorium_id: Mapped[int] = mapped_column(ForeignKey("auditoriums.id"), nullable=False)


class MovieScreening(Base):
    __tablename__ = "movie_screenings"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    movie_id: Mapped[int] = mapped_column(ForeignKey("movies.id"), nullable=False)
    auditorium_id: Mapped[int] = mapped_column(ForeignKey("auditoriums.id"), nullable=False)


class Ticket(Base):
    __tablename__ = "tickets"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    seat_id: Mapped[int] = mapped_column(ForeignKey("seats.id"), nullable=False)
    movie_screening_id: Mapped[int] = mapped_column(ForeignKey("movie_screenings.id"), nullable=False)
    price: Mapped[Decimal | None] = mapped_column(Numeric(8, 2), nullable=True)
