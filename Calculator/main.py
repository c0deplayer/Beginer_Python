# Author: CodePlayer
# Date: 06.03.2021
import operator


def is_digit(y):
    try:
        _ = float(y[0])   # ???
        _ = float(y[1])
        return True
    except ValueError:
        return False


def options():
    print('''
    =======================================
       "+" for addition
       "-" for subtraction
       "/" for division
       "*" for multiplication
       "%" for remainder of division
       "^" for the power and nth root
       "quadratic" for quadratic equation 
    ========================================
    ''')
    input("Enter anything to go back... ")


def help():
    print('''
    ===================================================================
       Hello :)
       > Provide the mathematical operation in the following format: 
          NUM1 NUM2 OPER or quadratic/??? for diffrent calculator
       > Write fractional numbers in decimal form e.g. 1/2 as 0.5
    ===================================================================
    ''')
    input("Enter anything to go back... ")


def quadratic_equation():
    a = float(input("Enter the a number: "))
    b = float(input("Enter the b number: "))
    c = float(input("Enter the c number: "))

    delta = b * b - (4 * a * c)
    s_delta = delta ** (1/2)

    if delta > 0:
        x1 = (-b - s_delta)/2*a
        x2 = (-b + s_delta)/2*a
        print("Delta is grater than one")
        print(f"x1 = {x1} | x2 = {x2}")
    elif delta == 0:
        x0 = -(b/2*a)
        print("Delta is equal to 0")
        print(f"x0 = {x0}")
    else:
        print("Delta is less than 0")


ops = {
    '+': operator.add,
    '-': operator.sub,
    '/': operator.truediv,
    '%': operator.mod,
    '*': operator.mul,
    '^': operator.pow,
    'quadratic': quadratic_equation}


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
        if calc[0] not in ops:
            print("Invalid option!")
        else:
            value = True
    return value


def menu():
    while True:
        print('''
        +====================================+
           Type:
           "h" for help
           "o" to show available operations
           "q" to quit
        +====================================+
        ''')
        choice = input("> ").lower()
        if choice in {'q', 'quit', 'leave'}:
            print("Goodbye!")
            break

        if choice == 'h':
            help()
        elif choice == 'o':
            options()
        else:
            calc = [x for x in choice.split(" ")]
            if sanitised_input(calc):
                if calc[0].isalpha():
                    ops[calc[0]]()
                else:
                    op_func = ops[calc[2]]
                    result = op_func(float(calc[0]), float(calc[1]))

                    print(f"{calc[0]} {calc[2]} {calc[1]} = {result}")


if __name__ == "__main__":
    menu()
