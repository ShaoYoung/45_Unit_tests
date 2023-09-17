# Задание 2. Разработайте и протестируйте метод numberInInterval, который проверяет, попадает ли переданное число в интервал (25;100)
# public boolean numberInInterval(int n) { … }

# (25; 100) - 25 не включается, 100 не включается, т.е. от 26 до 99
def number_in_interval(n: int) -> bool:
    if not isinstance(n, int):
        raise TypeError('Аргумент должен быть целым числом')
    return n in range(26, 100)


# if __name__ == '__main__':
#     print(number_in_interval(99.5))
