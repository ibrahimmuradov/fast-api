from fastapi import FastAPI, HTTPException
from enum import Enum
from schemas import GenreChoice, Book

app = FastAPI()


BOOKS = [
    {"id": 1, "name": "Red Dragon", "genre": "thriller", "publisher": [
        {"name": "G. P. Putnams, Dell Publishing (USA)", "release_date": "1981-10-01"}
    ]},
    {"id": 2, "name": "Hannibal", "genre": "Thriller", "publisher": [
        {"name": "Delacorte Press", "release_date": "1999-06-08"}
    ]},
    {"id": 3, "name": "Harry Potter And The Cursed Child", "genre": "Fantasy"},
    {"id": 4, "name": "Steve Jobs", "genre": "Biography"},
]


@app.get('/book-list')
async def book_list(genre: GenreChoice | None = None) -> list[Book]:  # | None - With this condition, if genre value is
    # None, = None - use this code, set default value None. 'genre: GenreChoice | None = None' we can also use this
    # code in this way 'genre: GenreChoice = None'
    # also using this code -> list[Book] we set the object to return and its type ->

    if genre:
        return [
            Book(**book) for book in BOOKS if book['genre'].lower() == genre.value
        ]  # Since the value coming from the url is automatically lowercase, we compare the BOOKS genre
        # value by making it lowercase using the lower method
    return [
        Book(**book) for book in BOOKS
    ]


@app.get('/book-detail/{book_id}')
async def book_detail(book_id: int) -> Book:
    book = next((Book(**book) for book in BOOKS if book["id"] == book_id), None)

    if book is None:
        # error not found
        raise HTTPException(status_code=404, detail='Book not found')

    return book


@app.get('/books/genre/{genre}')
async def book_genre(genre: GenreChoice) -> list[dict]:
    return [
        book for book in BOOKS if book['genre'].lower() == genre.value
    ]
