# Создаем список словарей с информацией о студентах и их оценках
groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Вадим",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [3, 3, 3]
    },
    {
        "name": "Михаил",
        "surname": "Кожанов",
        "exams": ["РКПО", "СП", "ПКСП"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Николай",
        "surname": "Климов",
        "exams": ["ОС", "Английский", "ПКСП"],
        "marks": [5, 5, 5]
    }
]

# Определяем функцию для вывода информации о студентах
def print_students(students):
    # Выводим заголовки таблицы
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    # Проходим по списку студентов и выводим их данные
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))

# Вызываем функцию для вывода информации о студентах
print_students(groupmates)

# Получаем среднюю оценку от пользователя
mid = input("Средняя оценка: ")

# Определяем функцию для вывода информации о студентах с оценкой выше средней
def print_students_1(students):
    # Выводим заголовки таблицы
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    # Проходим по списку студентов и выводим данные только для тех, у кого средняя оценка выше заданной
    for student in students:
        if sum(student["marks"]) / len(student["marks"]) > float(mid):
            print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))

# Вызываем функцию для вывода информации о студентах с оценкой выше средней
print_students_1(groupmates)
