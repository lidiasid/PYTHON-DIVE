# Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), которые вы уже решали. 
# Превратите функции в методы класса, а параметры в свойства. 
# Задания должны решаться через вызов методов экземпляра.

import os
import json
import csv
import pickle

class DirectoryWalker:
    def __init__(self, directory_path):
        self.directory_path = directory_path
        self.data = []

    def get_size(self, path):
        total = 0
        if os.path.isdir(path):
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                total += self.get_size(item_path)
        else:
            total += os.path.getsize(path)
        return total

    def walk_directory(self, directory=None, parent=None):
        if directory is None:
            directory = self.directory_path

        for name in os.listdir(directory):
            path = os.path.join(directory, name)

            if os.path.isdir(path):
                obj_type = "Directory"
            else:
                obj_type = "File"

            size = self.get_size(path)
            item = {
                "name": name,
                "parent": parent,
                "type": obj_type,
                "size": size
            }
            self.data.append(item)

            if obj_type == "Directory":
                self.walk_directory(path, parent=name)

    def save_to_json(self, filename):
        with open(filename, "w") as json_file:
            json.dump(self.data, json_file, indent=4)

    def save_to_csv(self, filename):
        keys = self.data[0].keys()
        with open(filename, "w", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(self.data)

    def save_to_pickle(self, filename):
        with open(filename, "wb") as pickle_file:
            pickle.dump(self.data, pickle_file)


if __name__ == "__main__":
    directory_path = "c:/Users/lida1/Desktop/Python dive/Lesson_8"
    walker = DirectoryWalker(directory_path)
    
    walker.walk_directory()
    
    walker.save_to_json("./result.json")
    walker.save_to_csv("./result.csv")
    walker.save_to_pickle("./result.pkl")
