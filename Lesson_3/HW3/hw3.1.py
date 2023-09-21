# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.

def find_duplicates(input_list):
    return list({item for item in input_list if input_list.count(item) > 1})

input_list = [1, 2, 1, 2, 3, 4, 5, 6, 5, 9]
print(find_duplicates(input_list)) 
