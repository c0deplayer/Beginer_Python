# Author: CodePlayer
# Date: 09.02.2021
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


def board(letters_correct, letters_wrong, secret_word):   # Displays board with guessed words
    print(Hangman_pics[len(letters_wrong)])
    print()

    blanks = "_" * len(secret_word)

    for i, letter in enumerate(secret_word):
        if letter in letters_correct:
            blanks = blanks[:i] + letter + blanks[i + 1:]

    if len(letters_wrong) != len(Hangman_pics) - 1:
        for letter in blanks:
            print(letter, end=" ")
        print("\n")


def random_index():   # Returns a random index for word[]
    return random.randint(0, len(word) - 1)


def guessing(letters_entered):   # It's guessing time
    while True:
        guess = input("Enter your guess: ").lower()
        if len(guess) != 1:
            print("Please enter a single letter")
        elif guess in letters_entered:
            print("You have already guessed this letter. Please, try again ")
        elif guess not in 'abcdefghijklmnoprstuvwxyz':
            print("Please enter only letters")
        else:
            return guess


def play():   # It's playing time
    secret_word = word[random_index()]
    letters_correct = ''
    letters_wrong = ''
    while True:
        board(letters_correct, letters_wrong, secret_word)
        guess = guessing(letters_correct + letters_wrong)
        if guess in secret_word:
            letters_correct += guess
            win = 1
            for _, letter in enumerate(secret_word):
                if letter not in letters_correct:
                    win = 0
            if win:
                print(f'''
                ====================================
                         CONGRATULATIONS!!!
                 > Correct guesses: {len(letters_correct)}
                 > Wrong guesses: {len(letters_wrong)}
                ====================================
                ''')
                break
        else:
            letters_wrong += guess
            if len(letters_wrong) == len(Hangman_pics) - 1:
                board(letters_correct, letters_wrong, secret_word)
                print(f'''
                ====================================
                            GAME OVER!!!
                 > Correct guesses: {len(letters_correct)}
                 > Wrong guesses: {len(letters_wrong)}
                 > Secret word: {secret_word}
                ====================================
                ''')
                break


def menu():  # Menu?
    print('''
    ===============
        Hangman  
    ===============
    ''')
    while True:
        play()
        play_again = input("Do you want to play again? [y/n] ").lower()
        if play_again not in ['y', 'yes', 'ok']:
            print("Have a good day/night")
            break


if __name__ == '__main__':
    menu()
