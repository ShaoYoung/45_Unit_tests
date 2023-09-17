# Тесты task_7.py

import unittest
from seminars.seminar_3.task_6.task_6 import User
from seminars.seminar_3.task_7.task_7 import UserRepository


class TestTask7(unittest.TestCase):
    def setUp(self):
        self.user = User('login', 'password')
        self.user_repository = UserRepository()

        # для задания 3.*
        self.user_1 = User('login_1', 'password_1')
        self.user_2 = User('login_2', 'password_2')
        self.user_1.auth(self.user_1.login, self.user_1.password)
        self.user_repository.add_user(self.user_1)
        self.user_2.auth(self.user_2.login, self.user_2.password)
        self.user_repository.add_user(self.user_2)

    def test_add_authorized_user(self):
        self.user.auth(self.user.login, self.user.password)
        self.user_repository.add_user(self.user)
        self.assertTrue(self.user in self.user_repository.repository, 'test_add_authorized_user failed')

    def test_add_unauthorized_user(self):
        self.user.auth('', self.user.password)
        self.user_repository.add_user(self.user)
        self.assertFalse(self.user in self.user_repository.repository, 'test_add_unauthorized_user failed')

    def test_logout_from_admin(self):
        self.user_repository.logout_all_no_admins(self.user_1)
        # print(self.user_repository)
        self.assertTrue(self.user_1 in self.user_repository.repository, 'test_logout_from_admin failed')
        self.assertFalse(self.user_2 in self.user_repository.repository, 'test_logout_from_admin failed')

    def test_logout_from_no_admin(self):
        self.user_repository.logout_all_no_admins(self.user_2)
        # print(self.user_repository)
        self.assertTrue(self.user_1 in self.user_repository.repository, 'test_logout_from_admin failed')
        self.assertTrue(self.user_2 in self.user_repository.repository, 'test_logout_from_admin failed')
