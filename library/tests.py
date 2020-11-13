import json

from django.test import TestCase, Client

from .models import Book


# Create your tests here.
class BookTestCase(TestCase):
    book1 = {
        'id': 1,
        'title': 'book1 title',
        'year': 2020,
        'genre': 'comedy',
        'annotation': 'a-a-a-a-a',
    }
    book2 = {
        'id': 2,
        'title': 'book2 title',
        'year': 1988,
        'genre': 'tragedy',
        'annotation': 'b-b-b-b-b',
    }

    def setUp(self):
        book1 = Book.objects.create(**self.book1)
        book2 = Book.objects.create(**self.book2)

    def test_books_list(self):
        client = Client()
        response = client.get('/books/')
        self.assertEqual(response.status_code, 200)



