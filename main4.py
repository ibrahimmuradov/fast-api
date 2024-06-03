from fastapi import FastAPI, HTTPException, Depends, Path
from models4 import GenreChoice, BookBase, BookCreate, Book, Publisher
from contextlib import asynccontextmanager
from db4 import init_db, get_session
from sqlmodel import Session, select
from typing import Annotated


@asynccontextmanager
async def lifespan(app: FastAPI):  # An asynchronous context manager to initialize the
    # database when the application starts

    init_db()
    yield

app = FastAPI(lifespan=lifespan)


@app.get('/book-list')
async def book_list(
        session: Session = Depends(get_session)  # injected database session
) -> list[Book]:
    books = session.exec(select(Book)).all()  # select(Book) - query to select all books

    return books


@app.get('/book-detail/{book_id}')
async def book_detail(
        book_id: Annotated[int, Path(name="The Book ID")],
        session: Session = Depends(get_session)
) -> Book:
    book = session.get(Book, book_id) # .get(Book, book_id) - retrieves a specific book by ID.

    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    return book


@app.post("/book-create")
async def book_create(
        book_data: BookCreate,
        session: Session = Depends(get_session)
) -> Book:
    create_book = Book(name=book_data.name, genre=book_data.genre)

    session.add(create_book)  # adds create book to the session

    if book_data.publishers:
        for publisher in book_data.publishers:
            publisher_obj = Publisher(name=publisher.name, release_date=publisher.release_date, book=create_book)
            session.add(publisher_obj)

    session.commit()  # commits the transaction.
    session.refresh(create_book)  # refreshes the create_book instance to reflect the committed state.

    return create_book
