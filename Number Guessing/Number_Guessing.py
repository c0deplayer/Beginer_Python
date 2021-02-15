# Author: CodePlayer
# Date: 04.02.2021
import random


class Game:

    def __init__(self, target, nick):
        self.target = random.randint(0, target)
        self.highest_number = target
        self.nick = nick
        self.guess = None
        self.guess_taken = 0

    def guessing(self):
        try:
            self.guess = int(input("\nYour guess: "))
        except ValueError:
            print(f"{self.nick}, enter the number")
            return False
        return True

    def play(self):
        target = self.target
        print(f"The number was drawn from the interval <0, {self.highest_number}>")
        while self.guess_taken < 5:
            if not self.guessing():
                continue

            self.guess_taken += 1

            if self.guess == target:
                break

            if self.guess < target:
                print("Your number is less than the generated one")
            else:
                print("Your number is grater than the generated one")
        if self.guess == target:
            print(f"Congratulations, {self.nick}! You guessed the number in {self.guess_taken} guesses")
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

        if choice == '1':
            game_easy = Game(25, nick)
            game_easy.play()
        elif choice == '2':
            game_medium = Game(50, nick)
            game_medium.play()
        elif choice == '3':
            game_hard = Game(100, nick)
            game_hard.play()
        else:
            print("Please, try again")


if __name__ == '__main__':
    main()
