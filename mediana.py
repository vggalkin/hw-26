#!/usr/bin/python3
# -*- coding: utf-8

def find_median(numbers):
    if not numbers:
        return None

    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    mid = n // 2

    if n % 2 == 1:
        return sorted_numbers[mid]
    else:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2

print("Введите числа через пробел:")
user_input = input()

try:
    numbers = [float(x) for x in user_input.split()]

    if not numbers:
        print("Список пуст. Невозможно найти медиану.")
    else:
        median = find_median(numbers)
        print(f"Исходный список: {numbers}")
        print(f"Медиана: {median}")

except ValueError:
    print("Ошибка: введите только числа, разделенные пробелами.")
