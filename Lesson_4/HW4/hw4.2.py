# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
# где ключ — значение переданного аргумента, а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.

def reverse_key_values(**kwargs):
    return {value if isinstance(value, (int, float, str, tuple)) else str(value): key for key, value in kwargs.items()}

result = reverse_key_values(a=1, b=[2, 3], c="test", d=(4, 5))
print(result)
