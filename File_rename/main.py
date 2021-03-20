# Author: CodePlayer
# Date: 16.03.2021
import os
import re


def renaming(path, name, ext, num):
    renamed_file = 0

    for count, filename in enumerate(os.listdir(path)):
        try:
            new = path + (name + str(count + 1) + ext)
            old = path + filename
            os.rename(old, new)
            renamed_file += 1

            if count == num:
                break
        except FileExistsError as exc:
            print(exc)
    return renamed_file


def sanitised_input(prompt, regex):
    while True:
        value = input(prompt)
        if re.search(regex, value):
            return value
        print("Invalid input")


def main():
    while True:
        try:
            print('''
            +---------------------------+
                  Files rename tool       
            +---------------------------+
            ''')
            path = sanitised_input(
                "Enter the path of the files (e.g. C:\\Screenshots\\Test) \n> ",
                r"^[a-zA-Z]:[\\\/](?:[\w]+[\\\/])*([\w]+)$")
            path += "\\"
            print(
                f"|  There are {len(os.listdir(path))} files in this location  |")
            name = sanitised_input(
                "Enter the new files name \n> ", r"^[\w\-.][\w\-. ]*$")
            ext = sanitised_input(
                "Enter the files extension (e.g. 'txt') \n> ", r"^[a-zA-Z0-9]+$")
            ext = "." + ext
            num = int(sanitised_input(
                "How many files should I rename (alphabetical sorting) \n> ", r"^[1-9]\d*$"))
            print("Renaming files...")
            success = renaming(path, name, ext, num - 1)
            print(
                f"\nRenamed files:  Successfully {success}  Failed {num - success}\n")
            cont = input("Do you want to continue [y/n]? ").lower()
            if not cont in {"y", "yes"}:
                print("Have a good day/night")
                break
        except FileNotFoundError as exc:
            print(exc)


if __name__ == "__main__":
    main()
