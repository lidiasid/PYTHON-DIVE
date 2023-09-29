"""
Задание №4
Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка
csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы
функции.
"""
import csv
import json
import hashlib

def process_csv_to_json(input_csv, output_json):
    output_data = []

    # Открываем CSV файл
    with open(input_csv, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        headers = next(csv_reader)  # Пропускаем строку с заголовками

        # Читаем каждую строку из CSV файла
        for row in csv_reader:
            identifier, name, access_level = row

            # Дополняем ID нулями до 10 цифр
            identifier = identifier.zfill(10)

            # Делаем первую букву имени заглавной
            name = name.capitalize()

            # Создаем хеш на основе имени и идентификатора
            m = hashlib.sha256()
            m.update(name.encode())
            m.update(identifier.encode())
            hashed_value = m.hexdigest()

            # Добавляем обработанные данные в выходной список
            output_data.append({
                'Identifier': identifier,
                'Name': name,
                'Access Level': access_level,
                'Hash': hashed_value
            })

    # Сохраняем результат в JSON файл
    with open(output_json, 'w') as json_file:
        json.dump(output_data, json_file, indent=4)

# Используем функцию
if __name__ == "__main__":
    input_csv = "c:/Users/lida1/Desktop/Python dive/Lesson_8/Task8_2/users_2046e13dc01e4b019202b9d0c230cd43.csv"
    output_json = "c:/Users/lida1/Desktop/Python dive/Lesson_8/Task8_2/processed_users.json"
    process_csv_to_json(input_csv, output_json)


