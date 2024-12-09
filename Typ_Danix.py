# Змінні
name = "Патрік"
surname = "Цюпка"
age = 16  # вік

if type(name) == type(surname):
    print(f"Ім'я та прізвище мають однаковий тип даних: {type(name)}")

name_surname_list = [name, surname]
print(f"Список з ім'ям і прізвищем: {name_surname_list}")

if isinstance(age, int):
    print(f"Тип даних віку: {type(age)}")