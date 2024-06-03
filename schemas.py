from enum import Enum
from pydantic import BaseModel
from datetime import date


class GenreChoice(Enum):
    THRILLER = "thriller"
    FANTASY = "fantasy"
    BIOGRAPHY = "biography"


class Publisher(BaseModel):
    name: str
    release_date: date


class Book(BaseModel):
    id: int
    name: str
    genre: str
    publisher: list[Publisher] = []  # set default list value use = []
