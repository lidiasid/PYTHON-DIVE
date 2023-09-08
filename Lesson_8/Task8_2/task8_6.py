"""
Задание №6
Напишите функцию, которая преобразует pickle файл
хранящий список словарей в табличный csv файл.
Для тестированию возьмите pickle версию файла из задачи
4 этого семинара.
Функция должна извлекать ключи словаря для заголовков
столбца из переданного файла.
"""

import csv
import pickle

def pickle_to_csv(pickle_file_path, csv_file_path):
    # Чтение данных из pickle файла
    with open(pickle_file_path, "rb") as pkl_file:
        data = pickle.load(pkl_file)

    # Получение заголовков из ключей словаря
    if data:
        headers = data[0].keys()

        # Запись данных в CSV файл
        with open(csv_file_path, "w", newline="") as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=headers)
            
            # Запись заголовков
            csv_writer.writeheader()

            # Запись данных
            for row in data:
                csv_writer.writerow(row)

if __name__ == "__main__":
    pickle_file_path = "c:/Users/lida1/Desktop/Python dive/Lesson_8/Task8_2/processed_users.pkl"  
    csv_file_path = "c:/Users/lida1/Desktop/Python dive/Lesson_8/Task8_2/converted_users.csv"  
    pickle_to_csv(pickle_file_path, csv_file_path)


