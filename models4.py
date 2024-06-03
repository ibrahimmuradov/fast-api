from enum import Enum
from pydantic import BaseModel, validator
from datetime import date
from sqlmodel import SQLModel, Field, Relationship


class GenreChoice(Enum):
    THRILLER = "Thriller"
    FANTASY = "Fantasy"
    BIOGRAPHY = "Biography"


class PublisherBase(SQLModel):
    name: str
    release_date: date
    book_id: int | None = Field(default=None, foreign_key="book.id")


class Publisher(PublisherBase, table=True):
    id: int = Field(default=None, primary_key=True)
    book: "Book" = Relationship(back_populates="publishers")


class BookBase(SQLModel):
    name: str
    genre: GenreChoice


class BookCreate(BookBase):
    publishers: list[PublisherBase] | None = None

    @validator('genre', pre=True)
    def title_case_genre(cls, value):
        return value.title()


class Book(BookBase, table=True):
    id: int = Field(default=None, primary_key=True)
    publishers: list[Publisher] = Relationship(back_populates="book")



