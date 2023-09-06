# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант. 
# *Верните все возможные варианты комплектации рюкзака.


items = {
    "tent": 5,
    "sleeping bag": 3,
    "cooking set": 2,
    "food": 4,
    "water": 3,
    "clothes": 2,
    "phone": 1,
    "lamp": 1,
    "map": 1,
    "rope": 6,
    "knife": 1,
    "sunscreen": 1
}

def fit_in_backpack(items, capacity):
    backpack = []
    for item, weight in sorted(items.items(), key=lambda x: x[1]):
        if weight <= capacity:
            backpack.append(item)
            capacity -= weight
    return backpack

capacity = 30
print(fit_in_backpack(items, capacity))
