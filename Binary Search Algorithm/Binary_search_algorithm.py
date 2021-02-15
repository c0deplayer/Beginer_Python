# Author: CodePlayer
# Date: 15.02.2021
import random


def random_list():
    return random.sample(range(0, 101, 2), 40)   # Returns a list of 40 randoms numbers


def searching(number, array):   # Returns either index of the number or -1 for the number not found
    start = 0
    end = len(array)
    step = 1

    while start <= end:
        mid = (start + end) // 2
        print(f"Searching for {number}, step {step}: {array[start:end + 1]}")
        step += 1

        if number == array[mid]:
            return mid

        if number < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


def main():
    print('''
    +==================================================================+
                     Welcome to Binary Search Algorithm
    +==================================================================+
      > The position of the number in the list will be displayed
      > If the number is not in the list, the index number will be -1
      > REMEMBER: Index begins with 0
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
