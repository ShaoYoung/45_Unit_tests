# Задание №2
# Разработайте тесты для метода firstLast6, где на вход подается массив чисел, а метод
# возвращает true, если первое или последнее число в массиве равно 6, иначе false.

def first_last_6(lst: list[int]) -> bool:
    return lst[0] == 6 or lst[-1] == 6


if __name__ == '__main__':
    print(first_last_6([6, 4, 6]))
