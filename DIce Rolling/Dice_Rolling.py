# Author: CodePlayer
# Date: 06.02.2021
import random

dice_image = ['''
[ - - - - - ]
[           ]
[     0     ]
[           ]
[ - - - - - ]''', '''
[ - - - - - ]
[   0       ]
[           ]
[       0   ]
[ - - - - - ]''', '''
[ - - - - - ]
[ 0         ]
[     0     ]
[         0 ]
[ - - - - - ]''', '''
[ - - - - - ]
[ 0       0 ]
[           ]
[ 0       0 ]
[ - - - - - ]''', '''
[ - - - - - ]
[ 0       0 ]
[     0     ]
[ 0       0 ]
[ - - - - - ]''', '''
[ - - - - - ]
[ 0       0 ]
[ 0       0 ]
[ 0       0 ]
[ - - - - - ]''']  # Stores the 'image' of the dice


def generating_dice():  # Returns dice value
    return random.randint(0, 5)


def menu():  # Shows the generated dice value in a nice form
    while True:
        print("Throwing a dice...")
        dice_throw = generating_dice()
        print(dice_image[dice_throw])
        again = input("\nDo you want to throw the dice again? [y/n] ")
        if again not in ['y', 'yes', 'ok']:
            break


if __name__ == '__main__':
    menu()
