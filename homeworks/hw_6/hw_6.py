"""
Домашнее задание
"""


# Задание 1.
# Создайте программу на Python или Java, которая принимает два списка чисел и выполняет
# следующие действия:
# a. Рассчитывает среднее значение каждого списка.
# b. Сравнивает эти средние значения и выводит соответствующее сообщение:
# - "Первый список имеет большее среднее значение", если среднее значение первого списка больше.
# - "Второй список имеет большее среднее значение", если среднее значение второго списка больше.
# - "Средние значения равны", если средние значения списков равны.
# ● Приложение должно быть написано в соответствии с принципами ООП.
# ● Используйте Pytest (для Python) или JUnit (для Java) для написания тестов, которые проверяют
# правильность работы программы.
# Тесты должны учитывать различные сценарии использования вашего приложения.
# ● Используйте pylint (для Python) или Checkstyle (для Java) для проверки качества кода.
# ● Сгенерируйте отчет о покрытии кода тестами. Ваша цель - достичь минимум 90% покрытия.

# Нужно предоставить:
# - Код программы
# - Код тестов
# - * Отчет pylint/Checkstyle
# - * Отчет о покрытии тестами
# - Объяснение того, какие сценарии покрыты тестами и почему вы выбрали именно эти сценарии.

class Lists:
    """
        self.first_list = [] - первый список
        self.average_first_list = 0 - среднее значение первого списка
        self.second_list = [] - второй список
        self.average_second_list = 0 - среднее значение второго списка
        def add_list(self, lst: list[int | float]) -> None - добавление списка
        def compare_lists(self) -> str - сравнение списков
    """
    def __init__(self):
        self.first_list = []
        self.average_first_list = 0
        self.second_list = []
        self.average_second_list = 0

    def add_list(self, lst: list[int | float]) -> None:
        """
        добавление списка и вычисление среднего значения
        :param lst: list[int | float]
        :return: None
        """
        if isinstance(lst, list):
            if lst:
                for item in lst:
                    if not isinstance(item, int | float):
                        raise TypeError('List elements must be int or float')
                if not self.first_list:
                    self.first_list.extend(lst)
                    self.average_first_list = sum(lst) / len(lst)
                elif not self.second_list:
                    self.second_list.extend(lst)
                    self.average_second_list = sum(lst) / len(lst)
                else:
                    raise RuntimeError('The lists are already filled')
            else:
                raise ValueError('List is empty')
        else:
            raise TypeError('The argument to the add_list function must be list')

    def compare_lists(self) -> str:
        """
        сравнение средних значений списков
        :return: None
        """
        if self.average_first_list > self.average_second_list:
            return 'Первый список имеет большее среднее значение'
        elif self.average_second_list > self.average_first_list:
            return 'Второй список имеет большее среднее значение'
        return 'Средние значения равны'


# if __name__ == '__main__':
#     lists = Lists()
#     lists.add_list([6, 7, 8, 9, 0])
#     lists.add_list([1, 2, 3, 4, 5])
#     print(lists.first_list)
#     print(lists.second_list)
#     print(lists.compare_lists())
