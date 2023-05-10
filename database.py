from motor.motor_asyncio import AsyncIOMotorClient
from models import Book
from bson import ObjectId
from typing import Optional

client = AsyncIOMotorClient('mongodb://localhost:27017')
database = client['bookStoreDB']
collection = database['books']

# Convert MongoDB's "_id" field to "id"
def book_helper(book) -> dict:
    return {
        "id": str(book["_id"]),
        "title": book["title"],
        "author": book["author"],
        "description": book["description"],
        "price": book["price"],
        "stock": book["stock"],
    }

# Retrieve all books present in the database
async def retrieve_books():
    books = []
    async for book in collection.find():
        books.append(book_helper(book))
    return books

# Add a new book into to the database
async def add_book(book_data: dict) -> dict:
    book = await collection.insert_one(book_data)
    new_book = await collection.find_one({"_id": book.inserted_id})
    return book_helper(new_book)

# Retrieve a book with a matching ID
async def retrieve_book(id: str) -> dict:
    book = await collection.find_one({"_id": ObjectId(id)})
    if book:
        return book_helper(book)

# Update a book with a matching ID
async def update_book(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    book = await collection.find_one({"_id": ObjectId(id)})
    if book:
        updated_book = await collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_book:
            return True
        return False

# Delete a book from the database
async def delete_book(id: str):
    book = await collection.find_one({"_id": ObjectId(id)})
    if book:
        await collection.delete_one({"_id": ObjectId(id)})
        return True

# Search books
async def search_books(title: Optional[str] = None, author: Optional[str] = None, min_price: Optional[float] = None, max_price: Optional[float] = None):
    query = {}

    if title:
        query['title'] = {'$regex': title}
    if author:
        query['author'] = {'$regex': author}
    if min_price and max_price:
        query['price'] = {'$gte': min_price, '$lte': max_price}
    elif min_price:
        query['price'] = {'$gte': min_price}
    elif max_price:
        query['price'] = {'$lte': max_price}

    books = []
    async for book in collection.find(query):
        books.append(book_helper(book))
    return books