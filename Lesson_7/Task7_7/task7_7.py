"""
Задание №7
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

"""


import os
import shutil

def sort_files(src_folder):
    # Словарь для хранения расширений файлов и соответствующих им папок
    file_extensions = {
        'images': ['.jpg', '.png', '.gif'],
        'videos': ['.mp4', '.mkv', '.flv'],
        'text': ['.txt', '.pdf', '.doc'],
        # добавьте больше категорий по мере необходимости
    }

    # Создание папок, если они ещё не существуют
    for folder in file_extensions.keys():
        os.makedirs(os.path.join(src_folder, folder), exist_ok=True)

    # Обход всех файлов в исходной папке
    for filename in os.listdir(src_folder):
        if os.path.isfile(os.path.join(src_folder, filename)):  # Проверяем, является ли объект файлом
            file_ext = os.path.splitext(filename)[1]  # Получаем расширение файла

            # Поиск соответствующей папки
            for folder, extensions in file_extensions.items():
                if file_ext in extensions:
                    # Перемещение файла
                    shutil.move(
                        os.path.join(src_folder, filename),
                        os.path.join(src_folder, folder, filename)
                    )
                    break  # Выходим из цикла после первого совпадения

if __name__ == "__main__":
    src_folder = "path/to/source/folder"  # замените на путь к вашей папке
    sort_files(src_folder)
