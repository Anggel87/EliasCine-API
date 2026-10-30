from pydantic import BaseModel, ConfigDict


class MovieBase(BaseModel):
    title: str
    director_id: int
    duration: int
    category_id: int
    synopsis: str


class MovieCreate(MovieBase):
    pass


class MovieRead(MovieBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
