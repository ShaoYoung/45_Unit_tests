# Задание №1
# Создайте два модуля. Первый модуль генерирует список случайных чисел. Второй модуль находит максимальное число в этом
# списке.
# Вам нужно сначала написать юнит-тесты для каждого модуля, затем написать интеграционный тест, который проверяет,
# что оба модуля работают вместе правильно
from random import randint


def get_random_list(size: int) -> list[int]:
    return [randint(0,100) for _ in range(size)]





