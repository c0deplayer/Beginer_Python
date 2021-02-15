# Author: CodePlayer
# Date: 04.02.2021
import random


class Game:

    def __init__(self, choice, name):
        self.name = name
        self.score = generated_score(choice)
        self.target = random_number(choice)
        self.guess = None

    def lower_score(self):
        print("Wrong answer!\n")
        self.score -= 1

    def play(self):
        while self.score > 0:
            try:
                self.guess = int(input("\nYour guess: "))
                if self.guess == self.target:
                    break
                self.lower_score()
                self.hint()
            except ValueError:
                print(f"{self.name}, enter the number")
        self.win_or_lose()

    def win_or_lose(self):
        name, score = self.name, self.score
        if score > 0:
            print(f'''
            -----------------------------
            |        YOU WIN !!!        |
            -----------------------------
            >  Nick: {name}         
            >  Your score: {score}
            ''')
        else:
            print(f'''
            -----------------------------
            |       GAME OVER !!!       |
            -----------------------------
            >  Nick: {name}
            >  Secret number: {self.target}
            ''')

    def hint(self):
        print(f'''\t\tHints:
        The number given is too {'small' if self.guess < self.target else 'high'}''')


def welcome_message():
    print('''
       Howdy!
       Before starting the mini-game, could you enter your nickname :?
       (Also, this project is obviously poorly made >.<)
       ''')


def random_number(choice):
    return random.randint(0, 20 ** int(choice))


def generated_score(choice):
    return 10 * int(choice)


def menu():
    print('''
    -------------------------------------------
    |       Number Guessing (mini-game)       |
    -------------------------------------------

        1. A number between 0 to 20
        2. A number between 0 to 400
        3. A number between 0 to 8000
    ''')


def main():
    welcome_message()
    name = input("\t")
    print("\n" * 100)
    while True:
        menu()
        choice = input("Choose one of the available option: ")
        if choice in ['1', '2', '3']:
            game = Game(choice, name)
            game.play()
            play_again = input("Do you want to play again? [y/n] ")
            if play_again.lower() not in ['y', 'yes', 'ok']:
                print(f"Goodbye, {game.name}!")
                break
        else:
            print("Please, try again")


if __name__ == '__main__':
    main()
