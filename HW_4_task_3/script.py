# Розробіть скрипт, який приймає шлях до директорії в якості аргументу командного рядка і візуалізує структуру цієї директорії,
# виводячи імена всіх піддиректорій та файлів. Для кращого візуального сприйняття, імена директорій та файлів мають відрізнятися за кольором.

# Вимоги до завдання:
#
# Створіть віртуальне оточення Python для ізоляції залежностей проєкту.
# Скрипт має отримувати шлях до директорії як аргумент при запуску. Цей шлях вказує, де знаходиться директорія, структуру якої потрібно відобразити.
# Використання бібліотеки colorama для реалізації кольорового виведення.
# Скрипт має коректно відображати як імена директорій, так і імена файлів, використовуючи рекурсивний спосіб обходу директорій (можна, за бажанням,
# використати не рекурсивний спосіб).
# Повинна бути перевірка та обробка помилок, наприклад, якщо вказаний шлях не існує або він не веде до директорії.


from colorama import Fore
import sys
from pathlib import Path

def print_tree(path, indent = ""):
    try:
    # """Recursively prints directory structure"""
        for item in sorted(Path(path).iterdir()):  # Sort for consistency
            if item.is_dir():
                print(f"{Fore.YELLOW}{indent}├── {Fore.RED}{item.name}")
            else:
                print(f"{Fore.YELLOW}{indent}├── {Fore.GREEN}{item.name}")

            if item.is_dir():  # Recursively print subdirectories
                print_tree( item, indent + "|   ")
    except (NotADirectoryError, FileNotFoundError):
        print(f"File doesn't exist or it is not a directory. Please check the correctness of the path {path}")
if __name__ == "__main__":
    path = sys.argv[1]
    # path = "C://Users//Arthur//Desktop//Storage"
    print_tree(path)