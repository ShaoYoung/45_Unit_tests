# Покрыть тестами функцию вычисления квадратного корня

from math import sqrt


def square_root(num: float) -> float:
    if num < 0:
        raise Exception(f'Число {num} должно быть больше нуля')
    # assert num > 0, 'Число должно быть больше нуля'
    return sqrt(num)

def test_square_root_positive():
    assert square_root(25) == 5, 'Тест с положительными числами провален'

def test_square_root_zero():
    assert square_root(0) == 0, 'Тест с нулём провален'

def test_square_root_negative():
    try:
        square_root(-5)
        raise Exception('Ожидалась ошибка, но получился неожиданный результат')
    except RuntimeError:
        print('Тесты на отрицательные числа пройдены')

if __name__ == '__main__':
    test_square_root_positive()
    test_square_root_zero()
    test_square_root_negative()

    print(square_root(10))
