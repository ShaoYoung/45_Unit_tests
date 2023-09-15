# Тесты

import unittest
from task_3 import calculating_discount


class TestTask3(unittest.TestCase):
    def test_purchase_exception(self):
        self.assertRaisesRegex(ValueError, 'Сумма не может быть меньше нуля', calculating_discount, purchase_amount=-7, discount_amount=100)

    def test_discount_less_zero_exception(self):
        self.assertRaisesRegex(ValueError, 'Размер скидки должен быть от 0 до 100', calculating_discount, purchase_amount=10, discount_amount=-100)

    def test_discount_more_hundred_exception(self):
        self.assertRaisesRegex(ValueError, 'Размер скидки должен быть от 0 до 100', calculating_discount, purchase_amount=10, discount_amount=110)

    def test_calculate_discount(self):
        self.assertEqual(calculating_discount(100, 20), 80, 'calculating_discount не работает')



