# Пользовательский интерфейс

from controller import Controller


class UserInterface:
    def __init__(self):
        self.controller = Controller()

    def start_page(self):
        print('Приложение "Записная книжка"')
        while True:
            for action in self.controller.action_list:
                print(f'{action.id} - {action.description}')
            user_choice = input('Выберите действие -> ')
            for action in self.controller.action_list:
                if action.id == user_choice:
                    action.action()
                    break
            else:
                print('Некорректный ввод. Попробуйте ещё раз.')


if __name__ == '__main__':
    user_interface = UserInterface()
    user_interface.start_page()
