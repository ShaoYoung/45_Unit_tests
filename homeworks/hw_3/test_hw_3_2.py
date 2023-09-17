# Тесты hw_3_2.py

import unittest
from hw_3_2 import number_in_interval


class TestNumberInInterval(unittest.TestCase):

    def test_in_interval(self):
        self.assertTrue(number_in_interval(50), 'test_in_interval failed')

    def test_out_interval(self):
        self.assertFalse(number_in_interval(0), 'test_out_interval failed')

    def test_n_is_not_int(self):
        self.assertRaisesRegex(TypeError, 'Аргумент должен быть целым числом', number_in_interval, n=50.5)




