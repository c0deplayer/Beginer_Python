# Author: CodePlayer
# Date: 16.03.2021
import os


def main():
    while True:
        print('''
        +---------------------------+
              Files rename tool       
        +---------------------------+
        ''')
        suc = 0
        path = input("Enter the path of the files (e.g. C:\Screenshots\Test) \n> ") + "\\"
        name = input("Enter the new files name \n> ")
        ext = "." + input("Enter the file extension (e.g. 'txt') \n> ")
        print("Renaming files...")

        for count, filename in enumerate(os.listdir(path)):
            new = path + (name + str(count + 1) + ext)
            old = path + filename
            os.rename(old, new)
            
        print("Done!")
        cont = input("Do you want to continue [y/n]?  ").lower()
        if not cont in {"y", "yes"}:
            print("Have a good day/night")
            break


if __name__ == "__main__":
    main()
