# Author: CodePlayer
# Date: 09.02.2021
# ToDo: Improve, improve, improve...
import random

Hangman_pics = ['''
     +---+
         |
         |
         |
        ===''', '''
     +---+
     0   |
         |
         |
        ===''', '''
     +---+
     0   |
     |   |
         |
        ===''', '''
     +---+
     0   |
    /|   |
         |
        ===''', '''
     +---+
     0   |
    /|\  |
         |
        ===''', '''
     +---+
     0   |
    /|\  |
    /    |
        ===''', '''
     +---+
     0   |
    /|\  |
    / \  |
        ==='''
                ]
word = 'anxiety baboon badger bat bear beaver camel cat clam cobra cougar \
       coyote crow deer dog donkey duck eagle fixable fjord flapjack flopping \
       fluffiness flyby foxglove frazzled frizzled fuchsia furry gabby galaxy \
       galvanize gazebo gizmo hawk lion lizard llama mole monkey moose mouse \
       mule newt otter owl panda parrot pigeon python rabbit ram rat raven \
       rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad \
       trout turkey turtle weasel whale wolf wombat zebra'.split()


def board(correct_letters, wrong_letters, secret_word):
    print(Hangman_pics[len(wrong_letters)])
    print()

    blanks = "_" * len(secret_word)

    for i, item in enumerate(secret_word):
        if item in correct_letters:
            blanks = blanks[:i] + item + blanks[i + 1:]

    if len(wrong_letters) != len(Hangman_pics) - 1:
        for letter in blanks:
            print(letter, end=" ")
        print("\n")


def random_word():
    word_index = random.randint(0, len(word) - 1)
    return word[word_index]


def guessing(entered_letters):
    while True:
        guess = input("Enter your guess: ").lower()
        if len(guess) != 1:
            print("Please enter a single letter")
        elif guess in entered_letters:
            print("You have already guessed this letter. Please, try again ")
        elif guess not in 'abcdefghijklmnoprstuvwxyz':
            print("Please enter only letters")
        else:
            return guess


def play():
    secret_word = random_word()
    correct_letters = ''
    wrong_letters = ''
    while True:
        board(correct_letters, wrong_letters, secret_word)
        guess = guessing(correct_letters + wrong_letters)
        if guess in secret_word:
            correct_letters += guess
            print(correct_letters)
            win = 1
            for i, item in enumerate(secret_word):
                if secret_word[i] not in correct_letters:
                    win = 0
            if win:
                print(f'''
                ====================================
                         CONGRATULATIONS!!!
                 > Correct guesses: {len(correct_letters)}
                 > Wrong guesses: {len(wrong_letters)}
                ====================================\n
                ''')
                break
        else:
            wrong_letters += guess
            if len(wrong_letters) == len(Hangman_pics) - 1:
                board(correct_letters, wrong_letters, secret_word)
                print(f'''
                ====================================
                            GAME OVER!!!
                 > Correct guesses: {len(correct_letters)}
                 > Wrong guesses: {len(wrong_letters)}
                 > Secret word: {secret_word}
                ====================================\n
                ''')
                break


def menu():
    while True:
        print('''
        --------------
        |   Hangman  |
        --------------
        ''')
        play()
        play_again = input("Do you want to play again? [y/n] ")
        if play_again.lower() not in ['y', 'yes', 'ok']:
            print("Have a good day/night")
            break


if __name__ == '__main__':
    menu()
