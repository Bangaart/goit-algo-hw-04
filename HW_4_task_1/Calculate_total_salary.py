# У вас є текстовий файл, який містить інформацію про місячні заробітні плати розробників у вашій компанії.
# Кожен рядок у файлі містить прізвище розробника та його заробітну плату, які розділені комою без пробілів.
#
# Ваше завдання - розробити функцію total_salary(path), яка аналізує цей файл і повертає загальну та середню суму заробітної плати всіх розробників.
#
# Вимоги до завдання:
#
# Функція total_salary(path) має приймати один аргумент - шлях до текстового файлу (path).
# Файл містить дані про заробітні плати розробників, розділені комами. Кожен рядок вказує на одного розробника.
# Функція повинна аналізувати файл, обчислювати загальну та середню суму заробітної плати.
# Результатом роботи функції є кортеж із двох чисел: загальної суми зарплат і середньої заробітної плати.


def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            new_list =[ int(item.split(",")[1]) for item in file.readlines()]
            average_salary = sum(new_list) // len(new_list)
            total_salar = sum(new_list)
    except (FileNotFoundError, FileExistsError):
        print("File doesn't exist ")
    except UnicodeDecodeError:
        print("File has no UTF-8 encoding")
    return (average_salary,total_salar)


total, average = total_salary("Salaries.txt")  #Use relative path but can use absolute path also like r"C:/Users/Arthur/PycharmProjects/For Tests/Homework_4/HW_4_task_1/Salaries.txt"
