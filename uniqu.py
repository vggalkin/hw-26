#!/usr/bin/python3
# -*- coding: utf-8

def check_tuple_uniqueness():
    try:
        user_input = input("Введите элементы кортежа через пробел: ")

        if not user_input.strip():
            print("Кортеж пуст")
            return

        my_tuple = tuple(map(int, user_input.split()))

        unique_elements = set(my_tuple)

        print(f"Исходный кортеж: {my_tuple}")
        print(f"Количество элементов: {len(my_tuple)}")
        print(f"Количество уникальных элементов: {len(unique_elements)}")

        if len(my_tuple) == len(unique_elements):
            print("✓ Все элементы уникальны")
        else:
            print("✗ Есть повторяющиеся элементы")
            duplicates = len(my_tuple) - len(unique_elements)
            print(f"Количество повторений: {duplicates}")

    except ValueError:
        print("Ошибка: введите только целые числа")


if __name__ == "__main__":
    check_tuple_uniqueness()
