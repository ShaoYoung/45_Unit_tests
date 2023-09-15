# Тесты

import unittest
from task_4 import lucky_sum


class TestTask4(unittest.TestCase):
    def test_all_num_13_exception(self):
        self.assertRaisesRegex(ValueError, 'Все числа равны 13', lucky_sum, a=13, b=13, c=13)

    def test_one_num_is_13(self):
        self.assertEqual(lucky_sum(13, 1, 1), 2, 'lucky_sum не работает')
        self.assertEqual(lucky_sum(1, 13, 1), 2, 'lucky_sum не работает')
        self.assertEqual(lucky_sum(1, 1, 13), 2, 'lucky_sum не работает')

    def test_two_num_is_13(self):
        self.assertEqual(lucky_sum(13, 13, 1), 1, 'lucky_sum не работает')
        self.assertEqual(lucky_sum(1, 13, 13), 1, 'lucky_sum не работает')
        self.assertEqual(lucky_sum(13, 1, 13), 1, 'lucky_sum не работает')

    def test_lucky_sum(self):
        self.assertEqual(lucky_sum(1, 1, 1), 3, 'lucky_sum не работает')

