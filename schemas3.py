from enum import Enum
from pydantic import BaseModel, validator
from datetime import date


class GenreChoice(Enum):
    THRILLER = "thriller"
    FANTASY = "fantasy"
    BIOGRAPHY = "biography"


class GenreModel(Enum):  # GenreModel model based on book model, this is different from
    # the GenreChoice model
    THRILLER = "Thriller"
    FANTASY = "Fantasy"
    BIOGRAPHY = "Biography"


class Publisher(BaseModel):
    name: str
    release_date: date


class BookBase(BaseModel):
    name: str
    genre: GenreModel
    publisher: list[Publisher] = []  # set default list value use = []


class BookCreate(BookBase):
    @validator('genre', pre=True)  # first parameter 'genre' declares the field name, pre=True - parameter
    # declares the priority execution of this validator function
    def title_case_genre(cls, value):
        return value.title()  # capitalizes the first letter of the word


class BookWithID(BookBase):
    id: int



