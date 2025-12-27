from fastapi import FastAPI, Body, HTTPException, Path, Query
from Book import Book
from BookRequest import BookRequest
from starlette import status

app = FastAPI()

BOOKS = [
    Book(1, "Computer Science Pro", "Theodore", "A very nice book", 7, 2005),
    Book(2, "The Art of Coding", "Sarah Jenkins", "A comprehensive guide to clean code", 9, 2014),
    Book(3, "Data Structures Daily", "Marcus Lee", "Master algorithms in 30 days", 8, 2009),
    Book(4, "Python for Everyone", "Alice Smith", "Beginner friendly introduction", 10, 2003),
    Book(5, "The Silicon Dream", "John Doe", "A history of tech giants", 6, 1987),
    Book(6, "Debugging Life", "Emily White", "A memoir of a software engineer", 8, 2003),
    Book(7, "AI Horizons", "Dr. Alan Grant", "The future of machine learning", 9, 2007),
    Book(8, "Network Ninjas", "Kevin Mitnick", "Advanced cybersecurity tactics", 9, 2021),
    Book(9, "Database Design", "C.J. Date", "Fundamental concepts of SQL", 7, 2024),
    Book(10, "Cloud Native", "Jane Austin", "Deploying scalable applications", 8, 2023)
]

@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS

@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book_id(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    
    raise HTTPException(status_code=404, detail='Item not found')

@app.get("/books/", status_code=status.HTTP_200_OK)
async def read_books_by_rating(rating: int = Query(gt=-1, lt=11)):
    books_returned = []
    for book in BOOKS:
        if book.rating == rating:
            books_returned.append(book)
    
    return books_returned

@app.get("/books/read-books-by-date/", status_code=status.HTTP_200_OK)
async def read_books_by_published_date(published_date: int = Query(gt=1900, lt=2031)):
    books_returned = []
    for book in BOOKS:
        if book.published_date == published_date:
            books_returned.append(book)
    
    return books_returned

@app.post("/create-book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request:BookRequest):
    new_book = Book(**book_request.model_dump()) # converting the request to Book Obj
    BOOKS.append(find_book_id(new_book))

def find_book_id(book: Book):
    # if len(BOOKS) > 0:
    #     book.id = BOOKS[-1].id + 1
    # else:
    #     book.id = 1
    
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1 

    return book

@app.put("/books/update_book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    book_changed = False

    for i in range(len(BOOKS)):
        if book.id == BOOKS[i].id:
            BOOKS[i] = book
            book_changed = True

    if not book_changed:
        raise HTTPException(status_code=404, detail='Item not found')

@app.delete("/books/delete_book/{id_book}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(id_book: int = Path(gt=0)):
    book_changed = False

    for i in range(len(BOOKS)):
        if BOOKS[i].id == id_book:
            BOOKS.pop(id_book)
            book_changed = True
            break
    
    if not book_changed:
        raise HTTPException(status_code=404, detail='Item not found')