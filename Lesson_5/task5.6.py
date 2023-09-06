"""
Задание №6
✔ Выведите в консоль таблицу умножения
от 2х2 до 9х10 как на школьной тетрадке.
✔ Таблицу создайте в виде однострочного
генератора, где каждый элемент генератора —
отдельный пример таблицы умножения.
✔ Для вывода результата используйте «принт»
без перехода на новую строку.
"""

for i in range(2, 10):
    print()
    for j in range(2, 10):
        print(f'{i} x {j} = {i * j}',  end='\n')

gen_tab = (f'{i} x {j} = {j * i}' for i in range(2, 10) for j in range(2, 10))
count = 0
for x in gen_tab:
    print(x, end='\n')
    count += 1
    if count % 8 == 0:
        print()

print('\n'.join([' '.join([f"{j}x{i}={i*j}" for j in range(2, 10)]) for i in range(2, 10)]))

gen = (f"\n" if j == 10 else f" {j} * {i} = {i * j} ".ljust(15) for i in
       range(2, 11) for j in range(2, 11))
print(*gen)
