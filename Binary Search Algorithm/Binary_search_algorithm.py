# Author: CodePlayer
# Date: 15.02.2021
import random


def random_list():
    return random.sample(range(0, 101), 50)


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
    return -1


def main():
    while True:
        array = random_list()
        print(array)
        number = int(input("Enter a number between <0, 100>\n"))
        print(f"Index of {number}: {searching(number, sorted(array))}")
        again = input("Do you want to continue? [y/n] ")
        if again not in ['y', 'yes', 'ok']:
            print("Goodbye!")
            break


if __name__ == '__main__':
    main()
