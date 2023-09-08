# Задача 4

from datetime import datetime

def happy_NY():
    assert datetime.now() < datetime(year=2023, month=1, day=1, hour=0, minute=0, second=0), '2024 ещё не наступил'




if __name__ == '__main__':
    happy_NY()




