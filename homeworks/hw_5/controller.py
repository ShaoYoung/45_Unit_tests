# Controller

from sys import exit
from notebook import Notebook
from contact import Contact


class Controller:
    class ControllerAction:
        def __init__(self, action_id: str, description: str, function):
            self.id = action_id
            self.description = description
            self.function = function

        def action(self):
            if self.function == exit:
                exit()
            self.function()

    def __init__(self):
        self.action_list = []
        self.action_list.append(self.ControllerAction('0', 'Завершение программы', exit))
        self.action_list.append(self.ControllerAction('1', 'Добавить новый контакт', self.add_contact))
        self.action_list.append(self.ControllerAction('2', 'Редактировать контакт', self.edit_contact))
        self.action_list.append(self.ControllerAction('3', 'Удалить контакт', self.del_contact))
        self.action_list.append(self.ControllerAction('4', 'Просмотр записной книжки', self.show_notebook))
        self.notebook = Notebook()

    def add_contact(self, contact: Contact = None):
        if not contact:
            name, phone = input('Введите имя и телефон контакта (через пробел) -> ').split()
            contact = Contact(name, phone)
        self.notebook.add_contact(contact)

    def show_notebook(self):
        print('В записной книжке есть следующие контакты')
        print(self.notebook)

    def del_contact(self):
        name = input('Введите имя контакта -> ')
        contact = self.notebook.find_contact(name)
        if contact:
            self.notebook.del_contact(contact)
            print(f'Контакт {name} удалён')
        else:
            print(f'В записной книжке нет контакта с именем {name}')

    def edit_contact(self):
        name = input('Введите имя контакта, которого надо редактировать -> ')
        contact = self.notebook.find_contact(name)
        if contact:
            new_name = input('Введите новое имя контакта -> ')
            new_phone = input('Введите новый телефон контакта -> ')
            self.notebook.edit_contact(contact, new_name, new_phone)
        else:
            print(f'В записной книжке нет контакта с именем {name}')
