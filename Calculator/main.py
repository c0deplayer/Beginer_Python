# Author: CodePlayer
# Date: 06.03.2021
import math
import operator


ops = {
    '+': operator.add,
    '-': operator.sub,
    '/': operator.truediv,
    '*': operator.mul,
    '^': operator.pow,
    'sqrt': math.sqrt}


def options():
    print('''
    =================================
      "+" for addition (2 num)
      "-" for subtraction (2 num)
      "/" for division (2 num)
      "*" for multiplication (2 num)
      "^" for the power (2 num)
      "sqrt" for the root (1 num)
    =================================
    ''')
    input("Enter anything to go back... ")


def sanitised_input(calc):
    value = False
    if len(calc) == 3:
        if not calc[0].isdigit() or not calc[1].isdigit():
            print("This is not the number!")
        elif calc[2] not in list(ops)[:5]:
            print("Invalid operator!")
        else:
            value = True
    elif len(calc) == 2:
        if not calc[0].isdigit():
            print("This is not the number!")
        elif calc[1] not in list(ops)[-1]:
            print("Invalid operator!")
        else:
            value = True
    else:
        print("Invalid option!")
    return value


def menu():
    while True:
        print('''
        +====================================+
           Type:
           "o" to show available operations
           "q" to quit
           "NUM1 (NUM2) OPERATOR"
        +====================================+
        ''')
        choice = input("> ")
        if choice.lower() in {'q', 'quit', 'leave'}:
            print("Goodbye!")
            break
        elif choice.lower() == 'o':
            options()
        else:
            calc = [x for x in choice.split(" ")]
            if sanitised_input(calc):
                if len(calc) == 3:
                    op_func = ops[calc[2]]
                    result = op_func(float(calc[0]), float(calc[1]))

                    print(f"{calc[0]} {calc[2]} {calc[1]} = {result}")
                else:
                    op_func = ops[calc[1]]
                    result = op_func(float(calc[0]))

                    print(f"{calc[1]}({calc[0]}) = {result}")


if __name__ == "__main__":
    menu()
