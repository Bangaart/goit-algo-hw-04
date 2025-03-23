# У вас є текстовий файл, який містить інформацію про котів.
# Кожен рядок файлу містить унікальний ідентифікатор кота, його ім'я та вік, розділені комою.

# Ваше завдання - розробити функцію get_cats_info(path), яка читає цей файл та повертає список словників з інформацією про кожного кота.
#
# Вимоги до завдання:
#
# Функція get_cats_info(path) має приймати один аргумент - шлях до текстового файлу (path).
# Файл містить дані про котів, де кожен запис містить унікальний ідентифікатор, ім'я кота та його вік.
# Функція має повертати список словників, де кожен словник містить інформацію про одного кота.


def get_cats_info(path):

    try:
        with open (path, "r", encoding="utf-8") as file:
            cats_list = [item.strip().split(",") for item in file.readlines()]
            cats_info_list = []
            for item in cats_list:
                cats_info_list.append({"id": item[0], "name" : item[1], "age" : item[2]})
    except (FileNotFoundError,FileExistsError):
        print("Can't find file or it was already created")
    except UnicodeDecodeError:
        print("File is not in UTF-8 encoding")
    else:
        for item in cats_list:                        # move returned list in block else
            cats_info_list.append({"id": item[0], "name": item[1], "age": item[2]})
        return cats_info_list

cats_info = get_cats_info("cats_info.txt")
print(cats_info)