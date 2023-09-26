"""
Задание №4
📌 Вспоминаем задачу из семинара 8 про сериализацию данных,
где в бесконечном цикле запрашивали имя, личный
идентификатор и уровень доступа (от 1 до 7) сохраняя
информацию в JSON файл.
📌 Напишите класс пользователя, который хранит эти данные в
свойствах экземпляра.
📌 Отдельно напишите функцию, которая считывает информацию
из JSON файла и формирует множество пользователей.
"""

import json

class User:
    def __init__(self, name: str, user_id: str,  level: str = '0') -> None:
        self.name = name
        self.user_id = user_id
        self.level = level

    def __str__(self):
        return f'User:{self.name}, id:{self.user_id},  level:{self.level}'


user_group = set()
def load_users(path):
    with open(path, 'r', encoding='UTF-8') as js_f:
        user_dict = json.load(js_f)
    for level, user_list in user_dict.items():
        for id, name in user_list.items():
            user_group.add(User(name, id, level))


if __name__ == '__main__':

    load_users('task13_4.json.json')
    print(*user_group)

    # for el in user_group:
    #     print(el)