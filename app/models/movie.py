from sqlalchemy import ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Movie(Base):
    __tablename__ = "peliculas"

    id: Mapped[int] = mapped_column("identificador", primary_key=True)
    title: Mapped[str] = mapped_column("titulo", String(200), nullable=False)
    director_id: Mapped[int] = mapped_column(
        "id_director", ForeignKey("directores.id_director"), nullable=False
    )
    duration: Mapped[int] = mapped_column("duracion", Integer, nullable=False)
    category_id: Mapped[int] = mapped_column(
        "id_categoria", ForeignKey("categorias.identificador"), nullable=False
    )
    synopsis: Mapped[str] = mapped_column("sinopsis", Text, nullable=False)
