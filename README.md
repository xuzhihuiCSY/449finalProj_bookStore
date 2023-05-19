# 449finalProj_bookStore

xu zhihui
Quoc Luong

# Online Bookstore API

This project provides an API for an online bookstore. It allows users to perform various operations such as adding books, listing books, searching for books, updating book information, deleting books, selling books, and retrieving book statistics.

## Technologies Used

- Python
- FastAPI
- Flask

## Installation

1. Clone the repository:
   git clone <repository-url>

2. Navigate to the project directory:
   cd <project-directory>

3. Create a virtual environment (optional but recommended):
   python -m venv env

4. Activate the virtual environment:

- For Windows:
  ```
  .\env\Scripts\activate
  ```
- For macOS/Linux:
  ```
  source env/bin/activate
  ```

5. Install the required packages:
   pip install -r requirements.txt

6. Start the FastAPI server:
   uvicorn main:app --reload

The server will start running on `http://localhost:8000`.

7. Start the Flask web application (optional, if you want to use the web interface):
   flask run

The web application will be accessible at `http://localhost:5000`.

## API Endpoints

- `GET /books`: List all books.
- `GET /books/{id}`: Get details of a single book.
- `POST /books`: Add a new book.
- `PUT /books/{id}`: Update information for a book.
- `DELETE /books/{id}`: Delete a book.
- `GET /search`: Search for books based on title, author, or price range.
- `PUT /sell_book/{id}`: Sell a specified quantity of a book.
- `GET /books_count`: Count the total number of books.
- `GET /best_selling_book`: Get the best-selling book.

## Web Interface

A web interface is provided to interact with the API. It allows you to view, add, update, and delete books. It also provides search functionality and displays book statistics.

To access the web interface, open your web browser and go to `http://localhost:5000`.
