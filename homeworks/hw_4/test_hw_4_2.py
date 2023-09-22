# Test

import unittest
# patch создаёт mock-объект
from unittest.mock import patch

from hw_4_2 import BookService, BookRepository, Book


class TestBookService(unittest.TestCase):
    def setUp(self) -> None:
        with patch('hw_4_2.BookRepository') as mock_book_repository:
            self.book_service = BookService(mock_book_repository)
            mock_book_repository.return_value

    def test_add_book(self):
        self.book = Book(1, 'first', '1', 'genre_1')
        self.book_service.add_book(self.book)
        # assert_called() - проверка вызова метода
        self.book_service.book_repository.add_book.assert_called()

    def test_get_books_by_author(self):
        author = 'Пушкин'
        self.book_service.get_books_by_author(author)
        self.book_service.book_repository.get_books_by_author.assert_called_once_with(author)

    def test_get_books_by_genre(self):
        genre = 'Проза'
        self.book_service.get_books_by_genre(genre)
        self.book_service.book_repository.get_books_by_genre.assert_called_once_with(genre)

    def test_get_all_books(self):
        self.book_service.get_all_books()
        self.book_service.book_repository.return_value()
