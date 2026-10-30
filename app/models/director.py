from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Director(Base):
    __tablename__ = "directores"

    id: Mapped[int] = mapped_column("id_director", primary_key=True)
    name: Mapped[str] = mapped_column("director", String(150), nullable=False)
