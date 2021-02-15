# Author: CodePlayer
# Date: 15.02.2021
import random


def random_list():
    return random.sample(range(0, 101, 2), 40)   # Returns a list of 40 randoms numbers


def searching(number, array):
    start = 0
    end = len(array)

    while start <= end:
        mid = (start + end) // 2

        if number == array[mid]:
            return mid

        if number < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return "Number not found"


def main():
    print('''
    =================================
         Binary Search Algorithm
    =================================
     ''')
    while True:
        array = random_list()
        number = input("Enter a number between <0, 100> ('q' to leave the program)\n")

        if number.lower() in ['q', 'quit', 'exit']:
            print("Goodbye!")
            break

        if int(number) not in range(0, 101):
            print("You entered a number outside the range!")
        else:
            print(f"Index of {number}: {searching(int(number), sorted(array))}")


if __name__ == '__main__':
    main()
