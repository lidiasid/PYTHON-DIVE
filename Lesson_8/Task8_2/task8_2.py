"""
Задание №2
Напишите функцию, которая в бесконечном цикле
запрашивает имя, личный идентификатор и уровень
доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в
JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо
от уровня доступа.
При перезапуске функции уже записанные в файл данные
должны сохраняться.

"""


"""
Задание №3
Напишите функцию, которая сохраняет созданный в
прошлом задании файл в формате CSV.
"""
import json
import csv
import os
import uuid

os.chdir("c:/Users/lida1/Desktop/Python dive/Lesson_8/Task8_2")

# Функция для создания JSON файла с пользователями
def add_user_to_file():
    file_name = f"users_{uuid.uuid4().hex}.json"
    pre_filled_data = [
        {"name": "Alice", "identifier": "id1", "access_level": "1"},
        {"name": "Bob", "identifier": "id2", "access_level": "2"},
        {"name": "Carol", "identifier": "id3", "access_level": "1"},
        {"name": "Dave", "identifier": "id4", "access_level": "3"}
    ]

    data = {}
    
    for user_data in pre_filled_data:
        name = user_data["name"]
        identifier = user_data["identifier"]
        access_level = user_data["access_level"]

        if access_level not in data:
            data[access_level] = {}

        if identifier not in data[access_level]:
            data[access_level][identifier] = name
        else:
            print("Идентификатор уже существует. Пользователь не будет добавлен.")

    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)

    print(f"Данные записаны в файл {file_name}.")
    return file_name  # Возвращаем имя созданного файла для дальнейшего использования

# Функция для конвертации JSON в CSV
def json_to_csv(json_file_name):
    csv_file_name = f"users_{uuid.uuid4().hex}.csv"

    with open(json_file_name, "r") as json_file:
        json_data = json.load(json_file)

    with open(csv_file_name, "w", newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Identifier", "Name", "Access Level"])

        for access_level, users in json_data.items():
            for identifier, name in users.items():
                writer.writerow([identifier, name, access_level])
    
    print(f"Данные сохранены в файл {csv_file_name}.")

if __name__ == "__main__":
    json_file_name = add_user_to_file()
    json_to_csv(json_file_name)
