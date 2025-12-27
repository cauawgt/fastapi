from fastapi import FastAPI, Body
from Book import Book
from BookRequest import BookRequest

app = FastAPI()

BOOKS = [
    Book(1, "Computer Science Pro", "Theodore", "A very nice book", 7),
    Book(2, "The Art of Coding", "Sarah Jenkins", "A comprehensive guide to clean code", 9),
    Book(3, "Data Structures Daily", "Marcus Lee", "Master algorithms in 30 days", 8),
    Book(4, "Python for Everyone", "Alice Smith", "Beginner friendly introduction", 10),
    Book(5, "The Silicon Dream", "John Doe", "A history of tech giants", 6),
    Book(6, "Debugging Life", "Emily White", "A memoir of a software engineer", 8),
    Book(7, "AI Horizons", "Dr. Alan Grant", "The future of machine learning", 9),
    Book(8, "Network Ninjas", "Kevin Mitnick", "Advanced cybersecurity tactics", 9),
    Book(9, "Database Design", "C.J. Date", "Fundamental concepts of SQL", 7),
    Book(10, "Cloud Native", "Jane Austin", "Deploying scalable applications", 8)
]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.post("/create-book")
async def create_book(book_request:BookRequest):
    new_book = Book(**book_request.dict()) # converting the request to Book Obj
    BOOKS.append(find_book_id(new_book))

def find_book_id(book: Book):
    # if len(BOOKS) > 0:
    #     book.id = BOOKS[-1].id + 1
    # else:
    #     book.id = 1
    
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1 

    return book
