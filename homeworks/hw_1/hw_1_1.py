# Задание 1.
# В классе Calculator создайте метод calculateDiscount, который принимает сумму покупки и процент скидки и возвращает сумму с учетом скидки.
# Ваша задача - проверить этот метод с использованием библиотеки AssertJ. Если метод calculateDiscount
# получает недопустимые аргументы, он должен выбрасывать исключение ArithmeticException.
# Не забудьте написать тесты для проверки этого поведения.


class Calculator:

    def calculate_discount(self, purchase_amount: float, discount_amount: int) -> float:
        # print(type(purchase_amount))
        if not (isinstance(purchase_amount, int) or isinstance(purchase_amount, float)):
            raise ArithmeticError(f'Недопустимое значение {purchase_amount}')
        if not (isinstance(discount_amount, int) and (discount_amount in range(101))):
            raise ArithmeticError(f'Недопустимое значение {discount_amount}')
        total_amount = purchase_amount * (100 - discount_amount) / 100
        return total_amount


if __name__ == '__main__':
    calculator = Calculator()
    print(calculator.calculate_discount(100.5, 10))
