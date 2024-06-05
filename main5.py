from fastapi import FastAPI, HTTPException, Depends, Path
from fastapi.responses import JSONResponse, HTMLResponse
from models5 import Book, Publisher
from schemas5 import BookListSchema, BookCreateUpdateSchema
from contextlib import asynccontextmanager
from services.choices5 import Genre
from db5 import SessionLocal
from sqlmodel import Session, select
from typing import Annotated, List


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/book/list", response_model=List[BookListSchema],
         summary="List of books", description="List of books",
         tags=['Book'])
async def color_list(db: SessionLocal = Depends(get_db)):
    books = db.query(Book).all()

    if books is None:
        content = {
            "message": "Any books not found"
        }
        status_code = 404
        return JSONResponse(content=content, status_code=status_code)

    book_list = [
        {
            "id": c.id,
            "name": c.name,
            "genre": c.genre,
        }
        for c in books
    ]
    return book_list
