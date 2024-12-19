from models import Book, Member
from typing import List, Dict

# In-memory storage for books and members
books_db: Dict[int, Book] = {}
members_db: Dict[int, Member] = {}

def get_books() -> List[Book]:
    return list(books_db.values())

def get_members() -> List[Member]:
    return list(members_db.values())

def add_book(book: Book):
    books_db[book.book_id] = book

def add_member(member: Member):
    members_db[member.member_id] = member

def get_book(book_id: int) -> Book:
    return books_db.get(book_id)

def get_member(member_id: int) -> Member:
    return members_db.get(member_id)

def delete_book(book_id: int):
    if book_id in books_db:
        del books_db[book_id]
