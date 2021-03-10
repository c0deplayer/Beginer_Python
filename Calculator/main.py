# Author: CodePlayer
# Date: 06.03.2021
import operator


ops = {
    '+': operator.add,
    '-': operator.sub,
    '/': operator.truediv,
    '%': operator.mod,
    '*': operator.mul,
    '^': operator.pow}


def is_digit(y):
    try:
        _ = float(y[0])   # ???
        _ = float(y[1])
        return True
    except ValueError:
        return False


def options():
    print('''
    =========================================
      "+" for addition
      "-" for subtraction
      "/" for division
      "*" for multiplication
      "%" for remainder of division
      "^" for the power and nth root
    =========================================
    ''')
    input("Enter anything to go back... ")


def help():
    print('''
    ===================================================================
       Hello :)
       > Provide the mathematical operation in the following format: 
          NUM1 NUM2 OPER
       > Write fractional numbers in decimal form e.g. 1/2 as 0.5
    ===================================================================
    ''')
    input("Enter anything to go back... ")


def sanitised_input(calc):
    value = False
    if len(calc) == 3:
        if not is_digit(calc):
            print("You must enter the nubmers")
        elif calc[2] not in ops:
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
           "h" for help
        +====================================+
        ''')
        choice = input("> ")
        if choice.lower() in {'q', 'quit', 'leave'}:
            print("Goodbye!")
            break
        elif choice.lower() == 'o':
            options()
        elif choice.lower() == 'h':
            help()
        else:
            calc = [x for x in choice.split(" ")]
            if sanitised_input(calc):
                op_func = ops[calc[2]]
                result = op_func(float(calc[0]), float(calc[1]))

                print(f"{calc[0]} {calc[2]} {calc[1]} = {result}")


if __name__ == "__main__":
    menu()
