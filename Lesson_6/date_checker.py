# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999]. 
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь. 
# Проверку года на високосность вынести в отдельную защищённую функцию.

__all__ = ["is_valid_date"]


def _is_leap_year(year):
    """Проверяет, является ли год високосным."""
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    return True

def is_valid_date(date_str):
    """Проверяет корректность даты."""
    try:
        day, month, year = map(int, date_str.split('.'))
        
        if not (1 <= year <= 9999):
            return False
        
        if month == 2:
            if _is_leap_year(year) and 1 <= day <= 29:
                return True
            elif 1 <= day <= 28:
                return True
            else:
                return False

        if month in [4, 6, 9, 11] and 1 <= day <= 30:
            return True
        
        if month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31:
            return True
        
        return False

    except ValueError:
        return False

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Использование: python date_checker.py DD.MM.YYYY")
    else:
        date_str = sys.argv[1]
        if is_valid_date(date_str):
            print("Дата корректна!")
        else:
            print("Дата некорректна!")
