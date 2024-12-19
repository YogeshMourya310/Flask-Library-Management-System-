from flask import Flask, render_template, request, redirect, url_for, jsonify
from models import Book, Member
from database import add_book, add_member, get_books, get_book, delete_book
import json

app = Flask(__name__)

# A simple token-based authentication system (very basic)
API_TOKEN = "secret_token"

def authenticate(token: str):
    return token == API_TOKEN

@app.route('/')
def index():
    books = get_books()  # Retrieve all books
    return render_template('index.html', books=books)  # Render the index.html template

@app.route('/add_book', methods=['GET', 'POST'])
def add_book_route():
    if request.method == 'POST':
        data = request.form
        title = data['title']
        author = data['author']
        year = int(data['year'])
        book_id = len(get_books()) + 1
        book = Book(book_id, title, author, year)
        add_book(book)  # Save the book
        return redirect(url_for('index'))  # Redirect to the homepage after adding the book
    return render_template('add_book.html')  # Render the add_book.html template

@app.route('/search_books', methods=['GET'])
def search_books():
    title = request.args.get('title')
    author = request.args.get('author')
    books = get_books()  # Get all books

    # Filter books based on search query
    if title:
        books = [book for book in books if title.lower() in book.title.lower()]
    if author:
        books = [book for book in books if author.lower() in book.author.lower()]

    return render_template('search_books.html', books=books)  # Render the search_books.html template

@app.route('/delete_book/<int:book_id>', methods=['GET', 'POST'])
def delete_book_route(book_id):
    book = get_book(book_id)
    if request.method == 'POST':
        delete_book(book_id)  # Delete the book
        return redirect(url_for('index'))  # Redirect to the homepage after deleting the book
    return render_template('delete_book.html', book=book)  # Render the delete_book.html template

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        token = request.form['token']
        if token == API_TOKEN:
            return redirect(url_for('index'))  # Redirect to home page after successful login
        else:
            return "Unauthorized", 401
    return render_template('login.html')  # Render the login.html template

# The following are placeholder API routes, which you can use to add new functionality or test via Postman, curl, etc.

@app.route('/api/books', methods=['GET'])
def api_get_books():
    books = get_books()
    return jsonify([book.to_dict() for book in books])  # Convert books to dicts for easy JSON response

@app.route('/api/book/<int:book_id>', methods=['GET'])
def api_get_book(book_id):
    book = get_book(book_id)
    return jsonify(book.to_dict())  # Convert single book to dict and return as JSON

@app.route('/api/book', methods=['POST'])
def api_add_book():
    data = request.json
    book_id = len(get_books()) + 1
    book = Book(book_id, data['title'], data['author'], data['year'])
    add_book(book)
    return jsonify(book.to_dict()), 201  # Return the new book as JSON

@app.route('/api/book/<int:book_id>', methods=['DELETE'])
def api_delete_book(book_id):
    delete_book(book_id)
    return jsonify({"message": "Book deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
