# Задание 2. У вас есть класс BookService, который использует интерфейс BookRepository для получения
# информации о книгах из базы данных. Ваша задача написать unit-тесты для BookService, используя
# Mockito для создания мок-объекта BookRepository.
# т.е. BookService для Python

from abc import ABC, abstractmethod


class BookRepository(ABC):

    @abstractmethod
    def get_books_by_author(self, author: str):
        pass

    @abstractmethod
    def get_books_by_genre(self, genre: str):
        pass


class BookService(BookRepository):

    def get_books_by_author(self, author: str):
        if author.title() == 'ПУШКИН':
            return 'Евгений Онегин'
        return None

    def get_books_by_genre(self, genre: str):
        if genre.lower() == 'сказки':
            return 'Сказка о попе и о работнике его Балде'
        return None
