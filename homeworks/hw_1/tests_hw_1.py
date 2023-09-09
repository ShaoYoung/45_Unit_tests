# Задание 1. Тесты класса Calculator

from hw_1 import Calculator


def test_purchase_amount_not_number(calculator: Calculator):
    try:
        calculator.calculate_discount('Not a number', 0)
        raise Exception('Ожидалась ошибка "ArithmeticError", но получился неожиданный результат')
    except Exception as e:
        print(f'Тесты на "Сумма покупки не число" пройдены. Возникла ошибка {e}')


def test_discount_amount_not_int(calculator: Calculator):
    try:
        calculator.calculate_discount(100, 50.5)
        raise Exception('Ожидалась ошибка "ArithmeticError", но получился неожиданный результат')
    except Exception as e:
        print(f'Тесты на "type(discount_amount) = int" пройдены. Возникла ошибка {e}')


def test_all_discount_amount(calculator: Calculator):
    for i in range(101):
        assert calculator.calculate_discount(100, i) == 100 * (
                    100 - i) / 100, f'Тесты на все возможные значения процента скидки не пройдены. Ошибка на проценте {i}'
    print('Тесты на все возможные значения процента скидки пройдены.')


if __name__ == '__main__':
    calculator = Calculator()
    test_purchase_amount_not_number(calculator)
    test_discount_amount_not_int(calculator)
    test_all_discount_amount(calculator)
