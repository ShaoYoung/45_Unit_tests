# Тесты TDD

import unittest
from task_6 import User


class TestTask6(unittest.TestCase):
    def setUp(self):
        self.user = User('login', 'password')

    def test_successful_auth(self):
        self.assertTrue(self.user.auth(self.user.login, self.user.password))

    def test_wrong_login(self):
        self.assertFalse(self.user.auth('', self.user.password))

    def test_wrong_password(self):
        self.assertFalse(self.user.auth(self.user.login, ''))

    def test_wrong_login_password(self):
        self.assertFalse(self.user.auth('', ''))

