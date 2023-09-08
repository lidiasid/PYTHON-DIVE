"""
Задание №5
Напишите функцию, которая ищет json файлы в указанной
директории и сохраняет их содержимое в виде
одноимённых pickle файлов.
"""

import os
import json
import pickle

def json_to_pickle_in_directory(directory_path):
    # Получаем список всех файлов в директории
    for filename in os.listdir(directory_path):
        # Проверяем, является ли файл JSON-файлом
        if filename.endswith(".json"):
            json_path = os.path.join(directory_path, filename)
            pickle_path = os.path.join(directory_path, filename.replace(".json", ".pkl"))
            
            # Читаем JSON-файл
            with open(json_path, "r") as json_file:
                data = json.load(json_file)
            
            # Сохраняем данные в pickle-файл
            with open(pickle_path, "wb") as pickle_file:
                pickle.dump(data, pickle_file)

if __name__ == "__main__":
    directory_path = "c:/Users/lida1/Desktop/Python dive/Lesson_8/Task8_2" 
    json_to_pickle_in_directory(directory_path)
