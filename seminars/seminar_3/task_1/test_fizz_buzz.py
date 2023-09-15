# Тесты

import unittest
from fizzbuzz import fizz_buzz

class TestFizzBuzz(unittest.TestCase):
    def test_fizzbuzz_15(self):
        self.assertEqual(fizz_buzz(45), 'fizzbuzz')

    def test_fizzbuzz_3(self):
        self.assertEqual(fizz_buzz(3), 'fizz')

    def test_fizzbuzz_5(self):
        self.assertEqual(fizz_buzz(5), 'buzz')

    def test_fizzbuzz_nothing(self):
        self.assertEqual(fizz_buzz(11), '11')

# coverage run -m unittest test_fizz_buzz
# coverage report -m
# coverage html


