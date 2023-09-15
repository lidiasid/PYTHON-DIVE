import os
import json
import csv
import pickle

def get_size(path):
    total = 0
    if os.path.isdir(path):
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            total += get_size(item_path)
    else:
        total += os.path.getsize(path)
    return total

def walk_directory(directory, parent=None):
    result = []
    for name in os.listdir(directory):
        path = os.path.join(directory, name)
        
        if os.path.isdir(path):
            obj_type = "Directory"
        else:
            obj_type = "File"
        
        size = get_size(path)
        item = {
            "name": name,
            "parent": parent,
            "type": obj_type,
            "size": size
        }
        result.append(item)
        
        if obj_type == "Directory":
            result.extend(walk_directory(path, parent=name))
    
    return result

def save_to_json(data, filename):
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)

def save_to_csv(data, filename):
    keys = data[0].keys()
    with open(filename, "w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

def save_to_pickle(data, filename):
    with open(filename, "wb") as pickle_file:
        pickle.dump(data, pickle_file)

if __name__ == "__main__":
    directory_path = "c:/Users/lida1/Desktop/Python dive/Lesson_8"  
    data = walk_directory(directory_path)

    save_to_json(data, "./result.json")
    save_to_csv(data, "./result.csv")
    save_to_pickle(data, "./result.pkl")
