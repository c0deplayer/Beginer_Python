# Author: CodePlayer
# Date: 23.02.2021
import random
import time

rps_table = [["?", 1, 0], [1, "?", 2], [0, 2, "?"]]
game_rule = {0: 'rock', 1: 'paper', 2: 'scissors'}
CLEAR = "\033[H\033[J"


def player_input():
    while True:
        try:
            player = int(input("> "))
            if player in game_rule.keys():
                return int(player)

            print("Invalid input!")
        except ValueError:
            print("This is not a valid input!")


def play():
    rounds = 0
    print('''
    +====================================+
       Type:
        > 0 -> Rock
        > 1 -> Paper 
        > 2 -> Scissors
        Result: Player vs. Computer
    +====================================+ 
    ''')
    while rounds != 5:
        move_player = player_input()
        move_comp = random.randint(0, 2)
        print(
            f"{game_rule[move_player].upper()} vs. {game_rule[move_comp].upper()}")

        winner = rps_table[move_player][move_comp]
        if winner != "?":
            print(f"The {'player' if winner == move_player else 'computer'}"
                  " has won this round!")
        else:
            print("Tie!")
        rounds += 1


def menu():
    while True:
        print('''
            ===============================================
                   Rock, Paper, Scissors (mini-game)       
            ===============================================
            ''')
        time.sleep(2)
        print(CLEAR, end="")
        play()
        leave = input("\nDo you want to quit the mini-game [y/n]?\n> ").lower()
        if leave in {'y', 'yes', 'quit'}:
            print("Have a good day/night ^w^")
            break


if __name__ == '__main__':
    menu()
