"""
Задание №7
Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader.
Распечатайте его как pickle строку.
"""
import pickle

def read_csv_and_pickle(csv_file_path):
    data = []
    headers = None

    # Чтение CSV-файла и заполнение списка словарей
    with open(csv_file_path, 'r') as csv_file:
        lines = csv_file.readlines()
        headers = lines[0].strip().split(',')
        
        for line in lines[1:]:
            values = line.strip().split(',')
            row = {headers[i]: values[i] for i in range(len(headers))}
            data.append(row)

    # Сериализация списка словарей в pickle-строку
    pickle_string = pickle.dumps(data)
    
    # Вывод pickle-строки (можно также сохранить в файл или использовать как-то иначе)
    print(pickle_string)

if __name__ == "__main__":
    csv_file_path = "c:/Users/lida1/Desktop/Python dive/Lesson_8/Task8_2/converted_users.csv"  
    read_csv_and_pickle(csv_file_path)


