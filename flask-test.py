from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

posts = [
    {
        "id": 1,
        "author": "Ivan",
        "title": "My first post"
    },
    {
        "id": 12,
        "author": "Toni",
        "title": "Python is fun"
    }
]

books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"id": 12, "title": "1984", "author": "George Orwell"}
]

@app.route('/')
def index():
    return render_template("flask-test.html", posts=posts)

@app.route('/hello/<name>')
def hello(name):
    return f"Hello, {name}!"

@app.route('/api/books', methods=['GET', 'POST'])
def books_api():
    if request.method == 'POST':
        # Get the new book data from the client
        new_book = request.get_json()

        # Generate a new ID for the book
        new_id = max(book['id'] for book in books) + 1
        new_book['id'] = new_id

        # Add the new book to our list
        books.append(new_book)

        # Return the new book data to the client
        return jsonify(new_book), 201
    else:
        # Handle the GET request
        return jsonify(books)

def find_book_by_id(book_id):
    for book in books:
        if book["id"] == book_id:
            return book

    return None



@app.route('/api/books/<int:id>', methods=['PUT'])
def handle_book(id):
    book = find_book_by_id(id)

    if book is None:
        return '', 404

    new_data = request.get_json()
    book.update(new_data)

    return jsonify(book)

@app.route('/api/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = find_book_by_id(id)
    if book is None:
        return '', 404
    books.remove(book)

    return jsonify(book)

if __name__ == "__main__":
    app.run(debug=True)

