# Author: CodePlayer
# Date: 16.03.2021
from multiprocessing.sharedctypes import Value
import os
import re


def renaming(path, name, ext):
    renamed_file = 0

    for count, filename in enumerate(os.listdir(path)):
        try:
            new = path + (name + str(count + 1) + ext)
            old = path + filename
            os.rename(old, new)
            renamed_file += 1
        except FileExistsError as exc:
            print(exc)
    return renamed_file


def sanitised_input(prompt, regex):
    while True:
        value = input(prompt)
        if re.search(f"{regex}", value):
            return value
        print("Invalid input")


def main():
    while True:
        print('''
        +---------------------------+
              Files rename tool       
        +---------------------------+
        ''')
        path = sanitised_input(
            "Enter the path of the files (e.g. C:\\Screenshots\\Test\\) \n> ",
            r"^[a-zA-Z]:[\\\/](?:[\w]+[\\\/])*([\w]+)\\$")
        lenght_dir = len(os.listdir(path))
        print(f"|  There are {lenght_dir} files in this location  |")
        name = sanitised_input(
            "Enter the new files name \n> ", r"^[\w\-.][\w\-. ]*$")
        ext = sanitised_input(
            "Enter the files extension (e.g. '.txt') \n> ", r"^\.[a-zA-Z0-9]+$")
        print("Renaming files...")
        success = renaming(path, name, ext)
        print(
            f"\nRenamed files:  Successfully {success}  Failed {lenght_dir - success}\n")
        cont = input("Do you want to continue [y/n]? ").lower()
        if not cont in {"y", "yes"}:
            print("Have a good day/night")
            break


if __name__ == "__main__":
    main()
