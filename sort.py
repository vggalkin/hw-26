#!/usr/bin/python3
# -*- coding: utf-8

def main():
    user_input = input("Введите числа через пробел: ")

    if not user_input.strip():
        print("Массив пуст")
        return

    try:
        numbers = list(map(int, user_input.split()))
    except ValueError:
        print("Ошибка: введите только целые числа")
        return

    numbers.sort(reverse=True)

    print("Отсортированный массив по убыванию:")
    print(" ".join(map(str, numbers)))


if __name__ == "__main__":
    main()
