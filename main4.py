from fastapi import FastAPI, HTTPException, Depends, Path
from models4 import GenreChoice, BookBase, BookCreate, Book, Publisher
from contextlib import asynccontextmanager
from db4 import init_db, get_session
from sqlmodel import Session
from typing import Annotated


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)


@app.get('/book-detail/{book_id}')
async def book_detail(
        book_id: Annotated[int, Path(name="The Book ID")],
        session: Session = Depends(get_session)
) -> Book:
    book = session.get(Book, id=book_id)

    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    return book


@app.post("/book-create")
async def book_create(
        book_data: BookCreate,
        session: Session = Depends(get_session)
) -> Book:
    create_book = Book(name=book_data.name, genre=book_data.genre)

    session.add(create_book)

    if book_data.publishers:
        for publisher in book_data.publishers:
            publisher_obj = Publisher(name=publisher.name, release_date=publisher.release_date, book=create_book)
            session.add(publisher_obj)

    session.commit()
    session.refresh(create_book)

    return create_book
