from pydantic import BaseModel


class BookCreateUpdateSchema(BaseModel):
    name: str
    genre: str


class BookListSchema(BaseModel):
    id: int
    name: str
    genre: str
