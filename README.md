# Library Management System API

## How to Run the Project
1. Clone the repository: `git clone <repository_url>`
2. Install Flask: `pip install flask`
3. Run the app: `python app.py`
4. The API will be accessible at `http://127.0.0.1:5000`.

## Design Choices
- Implemented RESTful API using Flask.
- In-memory storage for books and members using dictionaries.
- Token-based authentication for protected routes.
- Pagination and search implemented for books.

## Assumptions and Limitations
- The database is in-memory, so data will be lost when the application restarts.
- Authentication is a simple token check (`secret_token`).
- Pagination is based on query parameters `page` and `per_page`.
