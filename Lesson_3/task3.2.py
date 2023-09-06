# Пользователь вводит данные. Сделайте проверку данных
# и преобразуйте если возможно в один из вариантов ниже:
# ✔ Целое положительное число
# ✔ Вещественное положительное или отрицательное число
# ✔ Строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
# ✔ Строку в нижнем регистре в остальных случаях


def transform_data():
    data = input("Enter data: ")
    
    # Check for a positive integer
    try:
        if int(data) > 0:
            return int(data)
    except ValueError:
        pass
    
    # Check for a floating-point number
    try:
        number = float(data)
        return number
    except ValueError:
        pass

    # Convert string to lowercase
    if any(char.isupper() for char in data):
        return data.lower()
    else:
        return data

# Example of usage
result = transform_data()
print(result)
