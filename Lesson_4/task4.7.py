""" Функция получает на вход словарь с названием компании в качестве ключа
и списком с доходами и расходами (3-10 чисел) в качестве значения.
✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
прибыльные, верните истину, а если хотя бы одна убыточная — ложь. """

def are_all_companies_profitable(data):
    for company, transactions in data.items():
        if sum(transactions) < 0:
            return False
    return True

companies = {
    "CompanyA": [100, 300, -50, -30, 80],   
    "CompanyB": [200, 100, -150, -60],     
    "CompanyC": [300, 400, -100, -100],   
}

print(are_all_companies_profitable(companies))  

