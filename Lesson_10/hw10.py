# Доработаем задания 5-6. Создайте класс-фабрику.

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, *args):
        if animal_type == 'Fish':
            return Fish(*args)
        elif animal_type == 'Bird':
            return Bird(*args)
        elif animal_type == 'Mammal':
            return Mammal(*args)
        else:
            raise ValueError(f"Invalid animal type: {animal_type}")

class Animal:
    def __init__(self, kind, name, age):
        self._kind = kind
        self._name = name
        self._age = age

    def display_info(self):
        return f"Вид: {self._kind}, Кличка: {self._name}, Возраст: {self._age}"

class Fish(Animal):
    def __init__(self, kind, name, age, size):
        super().__init__(kind, name, age)
        self._size = size

    def display_info(self):
        return super().display_info() + f", Размер: {self._size} см"

class Bird(Animal):
    def __init__(self, kind, name, age, color):
        super().__init__(kind, name, age)
        self._color = color

    def display_info(self):
        return super().display_info() + f", Цвет: {self._color}"

class Mammal(Animal):
    def __init__(self, kind, name, age, spec):
        super().__init__(kind, name, age)
        self._spec = spec

    def display_info(self):
        return super().display_info() + f", Особенности: {self._spec}"

if __name__ == '__main__':
    f1 = AnimalFactory.create_animal('Fish', 'Карась', 'Федя', 1, 15)
    b1 = AnimalFactory.create_animal('Bird', 'Воробей', 'Чирик', 2, 'Серый')
    m1 = AnimalFactory.create_animal('Mammal', 'Кошка', 'Мурзик', 3, 'Шерстистая')

    for animal in [f1, b1, m1]:
        print(animal.display_info())

