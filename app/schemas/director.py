from pydantic import BaseModel, ConfigDict


class DirectorBase(BaseModel):
    name: str


class DirectorCreate(DirectorBase):
    pass


class DirectorRead(DirectorBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
