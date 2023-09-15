# Тесты TDD

import unittest
from mood_analyser import MoodAnalyser


class TestMoodAnalyser(unittest.TestCase):
    def setUp(self):
        self.analyser = MoodAnalyser()

    def test_fun_mood(self):
        self.assertEqual(self.analyser.mood_analyser('У меня веселое настроение'), 'веселое')

    def test_sad_mod(self):
        self.assertEqual(self.analyser.mood_analyser('У меня грустное настроение'), 'грустное')

    def test_undefined_mod(self):
        self.assertEqual(self.analyser.mood_analyser('У меня хорошее настроение'), 'неизвестное')


