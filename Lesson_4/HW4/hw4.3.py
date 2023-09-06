# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. 
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

def add_funds(summ, amount):
    if amount % 50 == 0:
        summ += amount
        transactions.append(("Пополнение", amount))
    else:
        print("Сумма должна быть кратной 50")
    return summ

def withdraw_funds(summ, amount):
    commission = max(30, min(0.015 * amount, 600))
    if amount + commission <= summ:
        if amount % 50 == 0:
            summ -= (amount + commission)
            transactions.append(("Снятие", amount))
        else:
            print("Сумма должна быть кратной 50")
    else:
        print("Недостаточно средств")
    return summ

def apply_bonus_or_tax(summ, action_count):
    if action_count % 3 == 0:
        summ *= 1.03
    if summ > 5_000_000:
        summ -= 0.1 * summ
    return summ

summ = 0
action_count = 0
transactions = []

while True:
    action = input("Выберите действие (a - пополнить, o - снять, q - выйти): ")

    if action == "q":
        break

    if action in ["a", "o"]:
        amount = int(input("Введите сумму: "))

        if action == "a":
            summ = add_funds(summ, amount)
        else:
            summ = withdraw_funds(summ, amount)

        action_count += 1
        summ = apply_bonus_or_tax(summ, action_count)

    print(f"Текущий баланс: {summ}")

print("История транзакций:", transactions)
