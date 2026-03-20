#!/usr/bin/python3
# -*- coding: utf-8

def find_unique_elements(list1, list2):
    unique_elements = set(list1) ^ set(list2)
    return list(unique_elements)

print("Введите первый список элементов через пробел:")
list1_input = input()
print("Введите второй список элементов через пробел:")
list2_input = input()

list1 = list1_input.split()
list2 = list2_input.split()

result = find_unique_elements(list1, list2)

print(f"\nПервый список: {list1}")
print(f"Второй список: {list2}")
print(f"Уникальные элементы (присутствуют только в одном из списков): {result}")
