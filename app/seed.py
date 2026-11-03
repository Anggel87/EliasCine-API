from datetime import datetime
from decimal import Decimal

from sqlalchemy import select

from app.db.session import SessionLocal
from app.models import Auditorium, Category, Director, Movie, MovieScreening, Seat, Ticket, User


def get_or_create_by_name(db, model, name: str):
    item = db.scalar(select(model).where(model.name == name))
    if item is None:
        item = model(name=name)
        db.add(item)
        db.flush()
    return item


def seed() -> None:
    db = SessionLocal()
    try:
        accion = get_or_create_by_name(db, Category, "Acción")
        aventura = get_or_create_by_name(db, Category, "Aventura")
        ciencia = get_or_create_by_name(db, Category, "Ciencia ficción")
        fantasia = get_or_create_by_name(db, Category, "Fantasía")

        favreau = get_or_create_by_name(db, Director, "Jon Favreau")
        whedon = get_or_create_by_name(db, Director, "Joss Whedon")
        coogler = get_or_create_by_name(db, Director, "Ryan Coogler")
        johnston = get_or_create_by_name(db, Director, "Joe Johnston")
        branagh = get_or_create_by_name(db, Director, "Kenneth Branagh")
        gunn = get_or_create_by_name(db, Director, "James Gunn")
        derrickson = get_or_create_by_name(db, Director, "Scott Derrickson")
        watts = get_or_create_by_name(db, Director, "Jon Watts")
        boden = get_or_create_by_name(db, Director, "Anna Boden")
        russo = get_or_create_by_name(db, Director, "Anthony Russo")

        movies_data = [
            ("Iron Man", favreau, ciencia, 126, "Tony Stark construye una armadura y se convierte en Iron Man.", "/media/movies/iron-man.jpg"),
            ("The Avengers", whedon, accion, 143, "Los Vengadores se reúnen para defender la Tierra.", "/media/movies/the-avengers.jpg"),
            ("Black Panther", coogler, aventura, 134, "T'Challa regresa a Wakanda para asumir su destino.", "/media/movies/black-panther.jpg"),
            ("Captain America: The First Avenger", johnston, accion, 124, "Steve Rogers se convierte en el supersoldado Captain America.", "/media/movies/captain-america-first-avenger.jpg"),
            ("Thor", branagh, fantasia, 115, "Thor aprende a ser digno de su poder y de su martillo.", "/media/movies/thor.jpg"),
            ("Guardians of the Galaxy", gunn, aventura, 121, "Un grupo de inadaptados protege una poderosa gema cósmica.", "/media/movies/guardians-of-the-galaxy.jpg"),
            ("Doctor Strange", derrickson, fantasia, 115, "Un cirujano descubre las artes místicas para proteger el mundo.", "/media/movies/doctor-strange.jpg"),
            ("Spider-Man: Homecoming", watts, accion, 133, "Peter Parker intenta equilibrar su vida escolar con ser Spider-Man.", "/media/movies/spider-man-homecoming.jpg"),
            ("Captain Marvel", boden, ciencia, 123, "Carol Danvers se convierte en una de las heroínas más poderosas.", "/media/movies/captain-marvel.jpg"),
            ("Avengers: Infinity War", russo, accion, 149, "Los héroes enfrentan a Thanos en la batalla por las Gemas del Infinito.", "/media/movies/avengers-infinity-war.jpg"),
        ]
        movies = []
        for title, director, category, length, summary, image in movies_data:
            movie = db.scalar(select(Movie).where(Movie.title == title))
            if movie is None:
                movie = Movie(title=title, director_id=director.id, category_id=category.id, length=length, movie_summary=summary, image=image)
                db.add(movie)
                db.flush()
            else:
                movie.director_id, movie.category_id, movie.length = director.id, category.id, length
                movie.movie_summary, movie.image = summary, image
            movies.append(movie)

        users_data = [("Peter Parker", "peter@demo.local"), ("Wanda Maximoff", "wanda@demo.local")]
        users = []
        for name, email in users_data:
            user = db.scalar(select(User).where(User.email == email))
            if user is None:
                user = User(name=name, email=email, password="demo-password")
                db.add(user)
                db.flush()
            users.append(user)

        auditoriums = []
        for name in ("Sala IMAX", "Sala Marvel 2D"):
            auditorium = get_or_create_by_name(db, Auditorium, name)
            auditoriums.append(auditorium)
            for row, number in (("A", 1), ("A", 2), ("B", 1), ("B", 2), ("C", 1), ("C", 2)):
                seat = db.scalar(select(Seat).where(Seat.auditorium_id == auditorium.id, Seat.row_label == row, Seat.seat_number == number))
                if seat is None:
                    db.add(Seat(auditorium_id=auditorium.id, row_label=row, seat_number=number))
        db.flush()

        for index, movie in enumerate(movies):
            auditorium = auditoriums[index % len(auditoriums)]
            show_date = datetime(2026, 12, 15 + index // 3, 18 + (index % 3) * 2, 0)
            screening = db.scalar(select(MovieScreening).where(MovieScreening.movie_id == movie.id, MovieScreening.auditorium_id == auditorium.id, MovieScreening.date == show_date))
            if screening is None:
                screening = MovieScreening(movie_id=movie.id, auditorium_id=auditorium.id, date=show_date)
                db.add(screening)
                db.flush()
            seat = db.scalar(select(Seat).where(Seat.auditorium_id == auditorium.id, Seat.row_label == "A", Seat.seat_number == 1))
            ticket = db.scalar(select(Ticket).where(Ticket.movie_screening_id == screening.id, Ticket.seat_id == seat.id))
            if ticket is None:
                db.add(Ticket(user_id=users[index % len(users)].id, seat_id=seat.id, movie_screening_id=screening.id, price=Decimal("89.50")))

        db.commit()
        print("Seed completado: 10 películas Marvel, catálogos, usuarios, salas, funciones y boletos.")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
