# Задание №4
# Напишите автоматизированный тест, который выполнит следующие шаги:
# 1. Открывает главную страницу Google.
# 2. Вводит "Selenium" в поисковую строку и нажимает кнопку "Поиск в Google".
# 3. В результатах поиска ищет ссылку на официальный сайт Selenium
# (https://www.selenium.dev) и проверяет, что ссылка действительно присутствует среди
# результатов поиска.

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class TestSelenium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(executable_path='chromedriver.exe'))

    def test_selenium(self):
        self.driver.get('https://google.ru')
        # By.Name ищет. Возвращает строку поиска
        elem = self.driver.find_element(By.NAME, 'q')
        # то, что ищем
        elem.send_keys('Selenium')
        # имитация нажатия кнопки
        elem.send_keys(Keys.RETURN)
        # By.XPATH - путь
        self.assertIn('https://www.selenium.dev', self.driver.find_element(By.XPATH, '/html/body').text)
        # Возвращает текст javascript. Тест не пройдёт.
        # self.assertIn('https://www.selenium.dev', self.driver.page_source)

    def tearDown(self) -> None:
        self.driver.close()
