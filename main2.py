from fastapi import FastAPI, HTTPException
from schemas import GenreChoice, Book

app = FastAPI()


BOOKS = [
    {"id": 1, "name": "Red Dragon", "genre": "thriller", "publisher": [
        {"name": "G. P. Putnams, Dell Publishing (USA)", "release_date": "1981-10-01"}
    ]},
    {"id": 2, "name": "Hannibal", "genre": "Thriller", "publisher": [
        {"name": "Delacorte Press", "release_date": "1999-06-08"}
    ]},
    {"id": 3, "name": "Harry Potter And The Cursed Child", "genre": "thriller"},
    {"id": 4, "name": "Steve Jobs", "genre": "Biography"},
]


@app.get('/book-list')
async def book_list(  # can also write function syntax like this
        genre: GenreChoice = None,
        has_publisher: bool = False  # set has_publisher parameter for filter has publisher
) -> list[Book]:
    books = [Book(**book) for book in BOOKS]

    if genre:
        # if genre is not None, filter genre use GenreChoice class
        books = [
            book for book in books if book.genre.lower() == genre.value
        ]
    if has_publisher:
        # if has_publisher is True, filter books that have publishers
        books = [
            book for book in books if len(book.publisher) > 0
        ]

    return books
