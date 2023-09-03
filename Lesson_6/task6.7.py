
from date_checker import is_valid_date



if __name__ == "__main__":
    date = input("Введите дату в формате DD.MM.YYYY: ")
    if is_valid_date(date):
        print("Дата корректная.")
    else:
        print("Дата некорректна!")


