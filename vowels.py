#!/usr/bin/python3
# -*- coding: utf-8

def replace_vowels(text):
    vowels = 'аеёиоуыэюяАЕЁИОУЫЭЮЯaeiouyAEIOUY'
    result = ''

    for char in text:
        if char in vowels:
            result += '-'
        else:
            result += char

    return result

print("Введите строку:")
user_input = input()

output = replace_vowels(user_input)
print(f"\nИсходная строка: {user_input}")
print(f"Результат: {output}")

