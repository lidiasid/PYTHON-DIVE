# Создайте модуль с функцией внутри. 
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.

__all__ = ["guess_riddle"]


# Защищенный словарь для хранения результатов
_protected_results = {}

def guess_riddle(riddle, possible_answers, attempts):
    """
    Функция для угадывания загадки.
    Возвращает номер попытки, на которой была угадана загадка, или 0, если попытки закончились.
    """
    print(riddle)
    for i in range(attempts):
        guess = input(f"Попытка {i+1}. Введите ваш ответ: ")
        if guess in possible_answers:
            return i + 1
    return 0

def play_riddles_from_dict(attempts=3):
    """
    Функция, которая хранит словарь загадок и вызывает функцию guess_riddle для каждой из них.
    """
    riddles = {
        "Что может в одно и то же время стоять и ходить?": ["часы"],
        "Что растет вверх головой?": ["лук", "морковка"],
        # Добавьте другие загадки по желанию...
    }

    results = {}
    for riddle, answers in riddles.items():
        attempt = guess_riddle(riddle, answers, attempts)
        record_results(riddle, attempt)
        results[riddle] = attempt

    return results

def record_results(riddle, attempt_number):
    """
    Функция для записи результатов отгадывания в защищенный словарь.
    """
    _protected_results[riddle] = attempt_number

def display_results():
    """
    Функция для отображения результатов в удобном для чтения виде.
    """
    formatted_results = (f"Загадка: '{key}', Отгадано с попытки: {value}" for key, value in _protected_results.items())
    for result in formatted_results:
        print(result)
