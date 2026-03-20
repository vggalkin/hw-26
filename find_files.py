#!/usr/bin/python3
# -*- coding: utf-8

import os

def find_files():
    path = input("Введите путь к директории: ")
    substring = input("Введите подстроку для поиска: ")

    # Получение списка файлов
    try:
        files = os.listdir(path)

        # Фильтрация файлов, содержащих подстроку
        matching_files = [f for f in files if substring in f]

        # Вывод результата
        if matching_files:
            print("Найденные файлы:")
            for file in matching_files:
                print(f"  {file}")
        else:
            print("Файлы, содержащие подстроку, не найдены")

    except FileNotFoundError:
        print("Ошибка: указанная директория не существует")
    except PermissionError:
        print("Ошибка: недостаточно прав для доступа к директории")

if __name__ == "__main__":
    find_files()
