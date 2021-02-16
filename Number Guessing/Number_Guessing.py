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
            self.guess = int(input("Your guess: "))
        except ValueError:
            print(f"{self.nick}, enter the number")
            return False
        return True

    def play(self):
        target = self.target
        print(f"\nThe number was drawn from the interval <0, {self.highest_number}>")
        while self.guess_taken < 8:
            if not self.guessing():
                continue

            self.guess_taken += 1

            if self.guess == target:
                break

            if self.guess < target:
                print(f"{self.guess} < {'#' * len(str(target))}")
            else:
                print(f"{self.guess} > {'#' * len(str(target))}")
        if self.guess == target:
            print(f'''
            ============================
                 CONGRATULATIONS!!!
            ============================
              > Nick: {self.nick}
              > Number of guessess: {self.guess_taken}
            ''')
        else:
            print(f'''
            ========================
                  GAME OVER!!!
            ========================
              > Nick: {self.nick}
              > Number: {target}
            ''')
        input("Enter anything to continue")


def main():
    nick = input("Hewwo! Please, enter your nickname ^w^\n")
    print()
    while True:
        print('''
        =======================================
              Number Guessing (mini-game)       
        =======================================

            1. Easy
            2. Medium
            3. Hard
        ''')
        choice = input("Enter a number to choose difficulty or 'q' to leave the mini-game\n")
        if choice.lower() in ['q', 'quit', 'exit']:
            print(f"Goodbye, {nick}")
            break

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
