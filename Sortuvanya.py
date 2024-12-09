def remove_duplicates(input_list):
    return list(set(input_list))

def sort_list(input_list):
    numbers = sorted([x for x in input_list if isinstance(x, (int, float))])  # Сортування чисел
    strings = sorted([x for x in input_list if isinstance(x, str)])  # Сортування рядків
    return numbers + strings  # Об'єднання чисел і рядків

original_list = [1, 2, 3, 4, 5, 6, 3, 4, 5, 7, 6, 5, 4, 3, 4, 5, 4, 3, 'Привіт', 'анаконда']

unique_list = remove_duplicates(original_list)
print(f"Список без повторень: {unique_list}")

sorted_list = sort_list(unique_list)
print(f"Відсортований список: {sorted_list}")
