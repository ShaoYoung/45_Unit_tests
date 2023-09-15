# Задание №6
# Разработайте класс User с методом аутентификации по логину и паролю. Метод должен возвращать true, если
# введенные логин и пароль корректны, иначе false. Протестируйте все методы

class User:
    def __init__(self, login: str, password: str):
        self._login = login
        self._password = password
        self._auth = False

    @property
    def login(self):
        return self._login

    @property
    def password(self):
        return self._password

    def auth(self, login: str, password: str) -> bool:
        if self._login == login and self._password == password:
            self._auth = True
            return True
        return False
