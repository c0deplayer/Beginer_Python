# Author: CodePlayer
# Date: 01.03.2021
import string
import random


def generator(n, lenght):
    if n == '1':
        chars = string.ascii_letters + string.digits
    else:
        chars = string.ascii_letters + string.digits + string.punctuation

    return "".join(random.sample(chars, lenght))


def main():
    while True:
        print('''
        +===================================+
            Welcome to Password Generator
        +===================================+
          1. Letters + Digits
          2. Everything w/o whitespaces
          3. Exit
        ''')
        choice = input("Enter one of the available option\n> ")
        if choice == '3':
            print('Have a good day/night ^w^')
            break

        if choice in {'1', '2'}:
            lenght = int(input("Enter the password length\n> "))
            print(f"\n>>>> {generator(choice, lenght)}")
        else:
            print("Invalid option\n")


if __name__ == "__main__":
    main()
