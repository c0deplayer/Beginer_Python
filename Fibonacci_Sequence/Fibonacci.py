# Author: CodePlayer
# Date: 01.03.2021


def show(fib, n = None):
    if n is not None:
        if n < len(fib):
            print(f">>> {fib[: n + 1]} <<<")
        else:
            print("Out of bound!")
    else:
        print("Please specitfy a value")


def sequence(n):
    fibonacii_list = []

    if n:
        fibonacii_list.extend([0, 1])
        for i in range (2, n + 1):
            fibonacii_list.append(fibonacii_list[i - 1] + fibonacii_list[i - 2])
    elif n == 0:
        fibonacii_list.append(0)
    return fibonacii_list


def main():
    print("\n>>>>> The Fibonacii Sequence <<<<<\n")
    while True:
        try:
            n_max = int(input("Enter the upper limit for the fibonacci sequence\n> "))
            if not n_max < 0:
                fib = sequence(n_max)
                n = int(input("Enter different values to get the corresponding fibonacci sequence, " 
                              "enter any negative number to exit\n> "))
                if n < 0:
                    print("Goodbye")
                    break

                show(fib, n)
        except ValueError:
            print("Invalid input")


if __name__ == "__main__":
    main()