# Author: CodePlayer
# Date: 16.03.2021
import os


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


def main():
    while True:
        print('''
        +---------------------------+
              Files rename tool       
        +---------------------------+
        ''')
        path = input(
            "Enter the path of the files (e.g. C:\Screenshots\Test) \n> ") + "\\"
        lenght_dir = len(os.listdir(path))
        print(f"|  There are {lenght_dir} files in this location  |")
        name = input("Enter the new files name \n> ")
        ext = "." + input("Enter the files extension (e.g. 'txt') \n> ")
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
