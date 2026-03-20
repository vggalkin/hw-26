import string


def main():
    text = input("Введите строку: ")

    upper = sum(1 for c in text if c.isupper())
    lower = sum(1 for c in text if c.islower())
    digits = sum(1 for c in text if c.isdigit())
    punctuation = sum(1 for c in text if c in string.punctuation)

    print(f"Букв в верхнем регистре: {upper}")
    print(f"Букв в нижнем регистре: {lower}")
    print(f"Цифр: {digits}")
    print(f"Символов пунктуации: {punctuation}")


if __name__ == "__main__":
    main()
