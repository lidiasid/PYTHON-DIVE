import json
import os
import uuid

os.chdir("c:/Users/lida1/Desktop/Python dive/Lesson_8/Task8_2")

def add_user_to_file():
    # Генерируем уникальное имя файла
    file_name = f"users_{uuid.uuid4().hex}.json"

    # Предзаполненные данные
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

        # Добавляем пользователя
        if access_level not in data:
            data[access_level] = {}
        
        # Проверяем уникальность идентификатора
        if identifier not in data[access_level]:
            data[access_level][identifier] = name
        else:
            print("Идентификатор уже существует. Пользователь не будет добавлен.")
            
    # Записываем в новый файл
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)

    print(f"Данные записаны в файл {file_name}.")

if __name__ == "__main__":
    add_user_to_file()
