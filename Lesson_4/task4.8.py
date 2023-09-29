""" Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
✔ Напишите функцию, которая при запуске заменяет содержимое переменных
оканчивающихся на s (кроме переменной из одной буквы s) на None.
✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце."""

apples = "many apples"
bananas = "many bananas"

def modify_variables():
    global_vars = globals()
    for name, value in list(global_vars.items()):
        if name.endswith('s') and name != 's':
            new_name = name[:-1]
            if new_name not in global_vars:
                globals()[new_name] = value
                globals()[name] = None

modify_variables()

print(apples)  # Ожидается None
print(apple)   # Ожидается "many apples"
print(bananas) # Ожидается None
print(banana)  # Ожидается "many bananas"
