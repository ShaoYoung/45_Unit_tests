# *Задание 1. *Представьте, что вы работаете над разработкой простого приложения для записной книжки, которое позволяет пользователям добавлять, редактировать и удалять контакты.
# Ваша задача - придумать как можно больше различных тестов (юнит-тесты, интеграционные тесты, сквозные тесты) для этого приложения.
# Напишите название каждого теста, его тип и краткое описание того, что этот тест проверяет.

# *Задание 2. *Ниже список тестовых сценариев. Ваша задача - определить тип каждого теста (юнит-тест, интеграционный тест, сквозной тест) и объяснить, почему вы так решили.
# Проверка того, что функция addContact корректно добавляет новый контакт в список контактов"".
# ""Проверка того, что при добавлении контакта через пользовательский интерфейс, контакт корректно отображается в списке контактов"".
# ""Проверка полного цикла работы с контактом: создание контакта, его редактирование и последующее удаление"".

# Тесты

import unittest
from contact import Contact
from user_interface import UserInterface


class TestNotebook(unittest.TestCase):
    def setUp(self) -> None:
        self.user_interface = UserInterface()

    # Проверка того, что функция addContact корректно добавляет новый контакт в список контактов
    # Тип теста - юнит-тест. Проверяется отельная функция отдельного модуля.
    def test_add_contact(self):
        contact = Contact('name_1', '+79130000000')
        self.user_interface.controller.add_contact(contact)
        self.assertTrue(contact in self.user_interface.controller.notebook.records, 'test_add_contact failed')

    # Проверка того, что при добавлении контакта через пользовательский интерфейс, контакт корректно отображается в списке контактов
    # Тип теста - интеграционный тест. Проверяется несколько компонентов приложения (но не всё приложение в целом).
    def test_add_user_and_show_contacts(self):
        contact = Contact('name_1', '+79130000000')
        self.user_interface.controller.add_contact(contact)
        self.assertTrue(str(contact) in str(self.user_interface.controller.notebook), 'test_add_user_and_show_contacts failed')

    # Проверка полного цикла работы с контактом: создание контакта, его редактирование и последующее удаление
    # Тип теста - сквозной. Проверяется работа приложения от начала до конца.
    def test_full_cycle(self):
        name = 'name_1'
        contact = Contact(name)
        self.user_interface.controller.notebook.add_contact(contact)
        found_contact = self.user_interface.controller.notebook.find_contact(name)
        name_new = 'name_new'
        phone_new = '+79130000000'
        self.user_interface.controller.notebook.edit_contact(found_contact, name_new, phone_new)
        found_contact = self.user_interface.controller.notebook.find_contact(name_new)
        self.assertTrue(found_contact in self.user_interface.controller.notebook.records, 'test_full_cycle (add and edit contact) failed')
        self.user_interface.controller.notebook.del_contact(found_contact)
        self.assertFalse(found_contact in self.user_interface.controller.notebook.records, 'test_full_cycle (del contact) failed')

#  =====
# Для данного приложения дополнительно можно разработать следующие тесты:
# test_correct_user_choice - Проверка корректности отработки выбора пользователя (запуск необходимого метода notebook). Тип теста - интеграционный.
# test_find_contact - Проверка поиска контакта по имени. Тип теста - юнит-тест.
# test_exit - Проверка корректного завершения приложения. Тип теста - сквозной (сокращённый вариант).




