# Author: CodePlayer
# Date: 04.02.2021
import random


class Game:

    def __init__(self, choice):
        self.target = random.randint(0, 20 ** int(choice))
        self.guess = None
        self.hints = 0

    def play(self, nick):
        target = self.target
        while self.hints < 10:
            try:
                self.guess = int(input("\nYour guess: "))
                self.hints += 1

                if self.guess == target:
                    break

                if self.guess < target:
                    print("Your number is less than the generated one")
                else:
                    print("Your number is grater than the generated one")
            except ValueError:
                print("Please, enter the number")
        if self.guess == target:
            print(f"Congratulations {nick}! You guessed the number in {self.hints} guesses")
        else:
            print(f"Sorry, the number I generated is {target}")


def main():
    nick = input("Hewwo! Please, enter your nickname ^w^\n")
    while True:
        print('''
        -------------------------------------------
        |       Number Guessing (mini-game)       |
        -------------------------------------------

            1. Easy
            2. Medium
            3. Hard
        ''')
        choice = input("Type the number to choose difficulty ('q' to leave the game): ")
        if choice.lower() in ['q', 'quit', 'exit']:
            print(f"Goodbye, {nick}")

        if choice in ['1', '2', '3']:
            game = Game(choice)
            game.play(nick)
        else:
            print("Please, try again")


if __name__ == '__main__':
    main()
