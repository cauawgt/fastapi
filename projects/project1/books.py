from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'drama'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'science'},
    {'title': 'Title Five', 'author': 'Author Two', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Six', 'category': 'science'},
]

@app.get("/hello")
async def first_api():
    return {'message': 'Hello Caua! How are you doing? '}

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/test/{dynamic_param}")
async def dynamic_param(dynamic_param: str):
    return {'dynamic_param': dynamic_param}

@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book

@app.get("/books/author/{author_name}")
async def read_books_author(author_name: str):
    books = []
    for book in BOOKS:
        if book.get('author').casefold() == author_name.casefold():
            books.append(book)
    
    return books