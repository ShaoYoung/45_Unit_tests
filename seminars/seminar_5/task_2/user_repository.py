# Задание №2
# У вас есть два класса - UserService и UserRepository. UserService использует UserRepository для
# получения информации о пользователе. Ваша задача - написать интеграционный тест, который
# проверяет, что UserService и UserRepository работают вместе должным образом.

class UserRepository:
    def get_user_by_id(self, user_id: int) -> str:
        return f'User {user_id}'
