""" Функция принимает на вход три списка одинаковой длины:
✔ имена str,
✔ ставка int,
✔ премия str с указанием процентов вида «10.25%».
✔ Вернуть словарь с именем в качестве ключа и суммой
премии в качестве значения.
✔ Сумма рассчитывается как ставка умноженная на процент премии. """


def calculate_bonus(names, wages, bonuses):
    return {name: wage * (float(bonus[:-1]) / 100) for name, wage, bonus in zip(names, wages, bonuses)}

names = ["Alice", "Bob", "Charlie"]
wages = [1000, 1200, 1100]
bonuses = ["10%", "5.5%", "7%"]

print(calculate_bonus(names, wages, bonuses))
