"""
Задание №2
Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
При нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списков-
архивов
list-архивы также являются свойствами экземпляра
"""

class Archive:
    
    number_archive = []
    string_archive = []
    
    def __init__(self, number, string):
        
        self.number = number
        self.string = string
        
        Archive.number_archive.append(number)
        Archive.string_archive.append(string)

    def show_archives(self):
        
        print(f"Number Archive: {Archive.number_archive}")
        print(f"String Archive: {Archive.string_archive}")

    def __str__(self):
        
        return f"Archive Object -> Number: {self.number}, String: {self.string}"

a1 = Archive(1, "One")
a2 = Archive(2, "Two")
a3 = Archive(3, "Three")

a1.show_archives()  

print(a1)  
print(a2)  
print(a3)  
