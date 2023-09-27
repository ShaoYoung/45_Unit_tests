# Tests

import pytest

from hw_6 import Lists


@pytest.fixture
def lists():
    lists = Lists()
    return lists


# проверка добавления одного списка
def test_add_one_list(lists):
    lists.add_list([1, 2, 3])
    assert lists.first_list == [1, 2, 3], 'test_add_one_list failed'


# проверка добавления двух списков
def test_add_two_lists(lists):
    lists.add_list([1, 2, 3])
    lists.add_list([4.1, 5.2, 6.3])
    assert lists.first_list == [1, 2, 3], 'test_add_two_lists failed'
    assert lists.second_list == [4.1, 5.2, 6.3], 'test_add_two_lists failed'


# проверка добавления трёх списков (третий лишний)
def test_add_three_lists(lists):
    lists.add_list([1, 2, 3])
    lists.add_list([4, 5, 6])
    with pytest.raises(RuntimeError):
        lists.add_list([1, 2, 3]), 'test_add_three_lists failed'


# проверка добавления пустого списка
def test_add_empty_list(lists):
    with pytest.raises(ValueError):
        lists.add_list([]), 'test_add_empty_list failed'


# проверка корректности типов элемента добавляемого списка
def test_type_adding_list(lists):
    with pytest.raises(TypeError):
        lists.add_list([1, '1']), 'test_type_adding_list failed'


# проверка добавления не списка
def test_add_not_list(lists):
    with pytest.raises(TypeError):
        lists.add_list(1), 'test_add_not_list failed'


# проверка сравнения (среднее значение первого списка больше второго)
def test_avg_first_list_higher(lists):
    lists.add_list([4, 5, 6])
    lists.add_list([1, 2, 3])
    assert lists.compare_lists() == 'Первый список имеет большее среднее значение', 'test_avg_first_list_higher failed'


# проверка сравнения (среднее значение второго списка больше первого)
def test_avg_second_list_higher(lists):
    lists.add_list([1.1, 2.2, 3.3])
    lists.add_list([4.6, 5.5, 6.4])
    assert lists.compare_lists() == 'Второй список имеет большее среднее значение', 'test_avg_second_list_higher failed'


# проверка сравнения (средние значения списков равны)
def test_avg_both_lists_equal(lists):
    lists.add_list([2, 2, 2])
    lists.add_list([1, 2, 3])
    assert lists.compare_lists() == 'Средние значения равны', 'test_avg_both_lists_equal failed'


if __name__ == '__main__':
    # ['-v'] - для подробных выводов
    pytest.main(['-v'])
