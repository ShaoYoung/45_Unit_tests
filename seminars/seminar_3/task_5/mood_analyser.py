# Задание №5
# Примените подход TDD для создания нового класса MoodAnalyser, который оценивает настроение
# выраженное во фразах.

class MoodAnalyser:
    def mood_analyser(self, msg: str) -> str:
        words = ('грустное', 'веселое')
        for word in words:
            if word in msg:
                return word
        return 'неизвестное'

        # if 'груст' in msg:
        #     return 'грустное'
        # elif 'весел' in msg:
        #     return 'веселое'


if __name__ == '__main__':
    analyser = MoodAnalyser()
    print(analyser.mood_analyser('веселое'))



