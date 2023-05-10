from flask import Flask, render_template, request, redirect, url_for
from models import Book
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get('http://localhost:8000/books')  # Assuming your FastAPI server is running on this address
    books = response.json()
    return render_template('index.html', books=books)

@app.route('/book/<id>')
def get_book(id):
    response = requests.get(f'http://localhost:8000/books/{id}')  
    book = response.json()
    return render_template('book.html', book=book)

@app.route('/add_book', methods=['POST'])
def add_book():
    book = Book(**request.form)
    response = requests.post('http://localhost:8000/books', data=book.json())
    return redirect(url_for('index'))

@app.route('/update_book/<id>', methods=['GET', 'POST'])
def update_book(id):
    if request.method == 'POST':
        book = {k: v for k, v in request.form.items() if v is not None}
        response = requests.put(f'http://localhost:8000/books/{id}', data=json.dumps(book))
        return redirect(url_for('get_book', id=id))
    else:
        response = requests.get(f'http://localhost:8000/books/{id}')  
        book = response.json()
        return render_template('update_book.html', book=book)

@app.route('/delete_book/<id>')
def delete_book(id):
    response = requests.delete(f'http://localhost:8000/books/{id}')  
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(port=5000)
