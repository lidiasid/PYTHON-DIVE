"""Напишите функцию группового переименования файлов. Она должна:
принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
принимать параметр количество цифр в порядковом номере.
принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
принимать параметр расширение конечного файла.
принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. 
К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение."""



import os
import glob

os.chdir("c:/Users/lida1/Desktop/Python dive/Lesson_7/HomeW_7")
def batch_rename(
        desired_name=None,
        num_digits=4,
        src_extension="txt",
        dest_extension="txt",
        name_range=None
):
    # Формирование шаблона поиска
    search_pattern = f"*.{src_extension}"
    
    # Поиск всех файлов, удовлетворяющих шаблону
    files = glob.glob(search_pattern)
    
    # Проверка, найдены ли файлы
    if not files:
        print(f"No files with .{src_extension} found.")
        return

    counter = 1  # Инициализация счетчика

    for filename in files:
        # Получение имени файла без расширения
        name_without_extension = os.path.splitext(filename)[0]
        
        # Применение диапазона символов, если он задан
        if name_range:
            start, end = name_range
            original_name_part = name_without_extension[start:end]
        else:
            original_name_part = ""
        
        # Формирование нового имени
        new_name = f"{desired_name or ''}{original_name_part}{str(counter).zfill(num_digits)}.{dest_extension}"

        # Переименование файла
        os.rename(filename, new_name)
        
        # Инкремент счетчика
        counter += 1

if __name__ == "__main__":
    batch_rename(desired_name="sample_", num_digits=2, src_extension="txt", dest_extension="log", name_range=(2, 4))