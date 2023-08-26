# Создайте функцию генератор чисел Фибоначчи

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fibonacci_generator()
for _ in range(10):
    print(next(gen))


""" def fibonacci_generator(max_value=None):
    a, b = 0, 1
    while max_value is None or a <= max_value:
        yield a
        a, b = b, a + b

for num in fibonacci_generator(100):
    print(num) """
