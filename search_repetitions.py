#!/usr/bin/python3
# -*- coding: utf-8

import sys

def search_repetitions():
    if sys.platform == 'win32':
        import io
        sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8', errors='replace')
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

    try:
        str1 = input("Введите первую строку: ")
        str2 = input("Введите вторую строку: ")
    except UnicodeDecodeError:
        str1 = sys.stdin.buffer.readline().decode('utf-8', errors='replace').strip()
        str2 = sys.stdin.buffer.readline().decode('utf-8', errors='replace').strip()

    common_chars = set(str1) & set(str2)

    if common_chars:
        print("Общие символы:", common_chars)
        print("Отсортированные общие символы:", sorted(common_chars))
    else:
        print("Общих символов не найдено")


if __name__ == "__main__":
    search_repetitions()
