from fastapi import FastAPI, HTTPException
from schemas3 import GenreChoice, BookBase, BookCreate, BookWithID

app = FastAPI()


BOOKS = [
    {"id": 1, "name": "Red Dragon", "genre": "Thriller", "publisher": [
        {"name": "G. P. Putnams, Dell Publishing (USA)", "release_date": "1981-10-01"}
    ]},
    {"id": 2, "name": "Hannibal", "genre": "Thriller", "publisher": [
        {"name": "Delacorte Press", "release_date": "1999-06-08"}
    ]},
    {"id": 3, "name": "Harry Potter And The Cursed Child", "genre": "Thriller"},
    {"id": 4, "name": "Steve Jobs", "genre": "Biography"},
]


@app.get('/book-list')
async def book_list(
        genre: GenreChoice = None,
        has_publisher: bool = False
) -> list[BookWithID]:
    books = [BookWithID(**book) for book in BOOKS]

    if genre:
        books = [
            book for book in books if book.genre.value.lower() == genre.value
        ]
    if has_publisher:
        books = [
            book for book in books if len(book.publisher) > 0
        ]

    return books


@app.post("/book-create")
async def book_create(book_data: BookCreate) -> BookWithID:
    book_id = BOOKS[-1]["id"] + 1  # for create new id - BOOKS[-1]["id"] get BOOKS datas last id
    # and increase id value by 1
    create_book = BookWithID(id=book_id, **book_data.model_dump()).model_dump()  # model dump - get object
    # values as dictionary
    BOOKS.append(create_book)

    return create_book


