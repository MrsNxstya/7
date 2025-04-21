from datetime import datetime

students = {
    "ivanov01": {
        "прізвище": "Іванов",
        "ім'я": "Олександр",
        "по батькові": "Сергійович",
        "дата народження": (2008, 4, 21)
    },
    "petrenko02": {
        "прізвище": "Петренко",
        "ім'я": "Марія",
        "по батькові": "Іванівна",
        "дата народження": (2008, 5, 10)
    },
    "shevchenko03": {
        "прізвище": "Шевченко",
        "ім'я": "Артем",
        "по батькові": "Олегович",
        "дата народження": (2009, 4, 21)
    },
    "bondar04": {
        "прізвище": "Бондар",
        "ім'я": "Ірина",
        "по батькові": "Петрівна",
        "дата народження": (2008, 8, 30)
    },
    "tkachenko05": {
        "прізвище": "Ткаченко",
        "ім'я": "Дмитро",
        "по батькові": "Андрійович",
        "дата народження": (2008, 11, 1)
    }
}

def show_all_students(students_dict):
    for key, data in students_dict.items():
        print(f"{data['прізвище']} {data['ім\'я']} {data['по батькові']}, народж. {data['дата народження']}")

def add_student(students_dict, key, surname, name, patronymic, birthdate):
    students_dict[key] = {
        "прізвище": surname,
        "ім'я": name,
        "по батькові": patronymic,
        "дата народження": birthdate
    }

def remove_student(students_dict, key):
    if key in students_dict:
        del students_dict[key]
    else:
        print(f"Запис з ключем '{key}' не знайдено.")

def show_sorted_students(students_dict):
    for key in sorted(students_dict.keys()):
        data = students_dict[key]
        print(f"{data['прізвище']} {data['ім\'я']} ({key})")

def check_birthdays_today(students_dict):
    today = datetime.today()
    found = False
    for data in students_dict.values():
        year, month, day = data["дата народження"]
        if month == today.month and day == today.day:
            print(f"Сьогодні день народження у: {data['ім\'я']} {data['прізвище']}")
            found = True
    if not found:
        print("Сьогодні ніхто не святкує день народження.")

print("Всі учні:")
show_all_students(students)
print("\nСписок за відсортованими ключами:")
show_sorted_students(students)

print("\nПеревірка на іменинників:")
check_birthdays_today(students)

print("\nДодавання нового учня:")
add_student(students, "melnyk06", "Мельник", "Анна", "Василівна", (2008, 6, 12))
show_all_students(students)

print("\nВидалення учня 'tkachenko05':")
remove_student(students, "tkachenko05")
show_all_students(students)
