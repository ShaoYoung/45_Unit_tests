# Тесты hw_3_1.py

import unittest
from hw_3_1 import even_odd_number


class TestEvenOddNumber(unittest.TestCase):

    def test_even(self):
        self.assertTrue(even_odd_number(4), 'test_even failed')

    def test_odd(self):
        self.assertFalse(even_odd_number(5), 'test_odd failed')


