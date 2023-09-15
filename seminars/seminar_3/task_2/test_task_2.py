# Тесты

import unittest
from task_2 import first_last_6


class TestTask2(unittest.TestCase):
    def test_first_6(self):
        self.assertTrue(first_last_6([6, 8, 9, 4]))

    def test_last_6(self):
        self.assertTrue(first_last_6([8, 9, 4, 6]))

    def test_without_6(self):
        self.assertFalse(first_last_6([8, 9, 4, 1]))

    def test_first_last_6(self):
        self.assertFalse(first_last_6([6, 8, 9, 4, 6]))

