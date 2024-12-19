import unittest
import json
from app import app


class LibraryAPITest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()

    def test_create_book(self):
        response = self.client.post('/books', json={
            'title': 'Flask 101',
            'author': 'John Doe',
            'year': 2024
        })
        self.assertEqual(response.status_code, 201)

    def test_get_books(self):
        response = self.client.get('/books?page=1&per_page=5')
        self.assertEqual(response.status_code, 200)

    def test_search_books_by_author(self):
        response = self.client.get('/search_books?author=John')
        self.assertEqual(response.status_code, 200)

    def test_delete_book(self):
        response = self.client.delete('/books/1')
        self.assertEqual(response.status_code, 204)

    def test_login(self):
        response = self.client.post('/login', json={'token': 'secret_token'})
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
