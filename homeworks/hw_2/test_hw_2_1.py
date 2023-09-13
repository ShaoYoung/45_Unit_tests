# Задание 1. Проект Vehicle. Написать следующие тесты с использованием JUnit5 (unittest):

import unittest
from hw_2_1 import Vehicle, Car, Motorcycle

class TestVehicle(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car('Lexus', 'RX300', 2002)
        self.motorcycle = Motorcycle('Harley-Davidson', 'Breakout', 2023)

    # - Проверить, что экземпляр объекта Car также является экземпляром транспортного средства (используя оператор instanceof).
    def test_car_isinstance_vehicle(self):
        self.assertTrue(isinstance(self.car, Vehicle), 'Тест "test_car_isinstance_vehicle" не прошёл')

    # - Проверить, что объект Car создается с 4-мя колесами.
    def test_car_create_with_4_wheels(self):
        self.assertEqual(self.car.num_wheels, 4, 'Тест "test_car_create_with_4_wheels" не прошёл')

    # - Проверить, что объект Motorcycle создается с 2-мя колесами.
    def test_motorcycle_create_with_2_wheels(self):
        self.assertEqual(self.motorcycle.num_wheels, 2, 'Тест "test_motorcycle_create_with_2_wheels" не прошёл')

    # - Проверить, что объект Car развивает скорость 60 в режиме тестового вождения (используя метод testDrive()).
    def test_car_in_test_drive_mode_60(self):
        self.car.test_drive()
        self.assertEqual(self.car.speed, 60, 'Тест "test_car_in_test_drive_mode_60" не прошёл')

    # - Проверить, что объект Motorcycle развивает скорость 75 в режиме тестового вождения (используя метод testDrive()).
    def test_motorcycle_in_test_drive_mode_75(self):
        self.motorcycle.test_drive()
        self.assertEqual(self.motorcycle.speed, 75, 'Тест "test_motorcycle_in_test_drive_mode_75" не прошёл')

    # - Проверить, что в режиме парковки (сначала testDrive, потом park, т.е. эмуляция движения транспорта) машина останавливается (speed = 0).
    def test_car_test_drive_park_0(self):
        self.car.test_drive()
        self.car.park()
        self.assertEqual(self.car.speed, 0, 'Тест "test_car_test_drive_park_0" не прошёл')

    # - Проверить, что в режиме парковки (сначала testDrive, потом park, т.е. эмуляция движения транспорта) мотоцикл останавливается (speed = 0).
    def test_motorcycle_test_drive_park_0(self):
        self.motorcycle.test_drive()
        self.motorcycle.park()
        self.assertEqual(self.motorcycle.speed, 0, 'Тест "test_motorcycle_test_drive_park_0" не прошёл')

