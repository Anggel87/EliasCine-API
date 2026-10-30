from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Category(Base):
    __tablename__ = "categorias"

    id: Mapped[int] = mapped_column("identificador", primary_key=True)
    name: Mapped[str] = mapped_column("categoria", String(100), nullable=False)
