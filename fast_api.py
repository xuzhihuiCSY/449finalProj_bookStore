from fastapi import FastAPI, HTTPException
from typing import List,Optional
from models import Book
import database

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to my online bookstore API!"}

@app.post("/books", response_description="Add new book", response_model=Book)
async def create_book(book: Book):
    book = await database.add_book(book.dict())
    return book

@app.get("/books", response_description="List all books", response_model=List[Book])
async def list_books():
    books = await database.retrieve_books()
    return books

@app.get("/books/{id}", response_description="Get a single book", response_model=Book)
async def show_book(id: str):
    book = await database.retrieve_book(id)
    if book is None:
        raise HTTPException(status_code=404, detail=f"Book {id} not found")
    return book

@app.put("/books/{id}", response_description="Update a book", response_model=Book)
async def update_book(id: str, book: Book):
    book = {k: v for k, v in book.dict().items() if v is not None}
    
    updated_book = await database.update_book(id, book)
    if updated_book:
        return await database.retrieve_book(id)
    else:
        raise HTTPException(status_code=404, detail=f"Book {id} not found")

@app.delete("/books/{id}", response_description="Delete a book")
async def delete_book(id: str):
    delete_result = await database.delete_book(id)
    if delete_result:
        return {"msg": f"Book {id} deleted"}
    else:
        raise HTTPException(status_code=404, detail=f"Book {id} not found")

@app.get("/search", response_description="Search books", response_model=List[Book])
async def search_books(title: Optional[str] = None, author: Optional[str] = None, min_price: Optional[float] = None, max_price: Optional[float] = None):
    books = await database.search_books(title, author, min_price, max_price)
    return books

