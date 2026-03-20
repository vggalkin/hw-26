#!/usr/bin/python3
# -*- coding: utf-8


input1 = input("Введите элементы первого списка через пробел: ")
list1 = list(map(int, input1.split()))

input2 = input("Введите элементы второго списка через пробел: ")
list2 = list(map(int, input2.split()))

common_elements = set(list1).intersection(set(list2))

if common_elements:
    print("Элементы, присутствующие в обоих списках:", sorted(common_elements))
else:
    print("Общих элементов не найдено")
