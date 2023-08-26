import os

# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


def split_path(path):
    dirname, filename = os.path.split(path)
    basename, extension = os.path.splitext(filename)
    return dirname, basename, extension

path = "/home/user/documents/myfile.txt"
print(split_path(path))  
