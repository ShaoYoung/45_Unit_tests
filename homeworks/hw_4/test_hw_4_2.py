# Test

import unittest
from unittest.mock import Mock

from hw_4_2 import BookService, BookRepository


class TestBookService(unittest.TestCase):
    def setUp(self) -> None:
        self.book_repository = Mock(BookRepository)

    def test_get_books_by_author(self):
        pass

    def test_get_books_by_genre(self):
        pass


# Mock-объект BookService