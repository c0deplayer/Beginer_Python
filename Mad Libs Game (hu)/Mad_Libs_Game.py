# Author: CodePlayer
# Date: 03.02.21

template_form = ''' 
The Titanic was a {} ship that could
{} hold {} people. The ship was so
{} that it took {} years to build.
The ship had {} {} smoke stacks and
was as long as {} football fields and
could hold over 2 000 {}. The Titanic
{} in April 1912 from {}, headed for
New York. {}, the ship {} a {}
iceberg and {} in the {} Ocean,
though some people escaped in {}
boats. Explorers {} the wreckage of
the Titanic on the ocean {} {}
years later.
'''

blanks = [
    "adjective",
    "adverb",
    "number",
    "adjective",
    "number",
    "number",
    "adjective",
    "number",
    "plural noun",
    "verb",
    "proper noun place",
    "adverb",
    "verb",
    "adjective",
    "verb",
    "adjective",
    "adjective",
    "verb",
    "noun",
    "number",
]


def get_user_input():  # Takes user input and adds answers to the list
    answers = []
    for blank in blanks:
        ans = ""
        while not ans:
            ans = input(blank.capitalize() + " >> ")
            if not ans:
                print("Please, don't leave blank spaces. It kills the experience!")
        answers.append(ans)
    end(answers)


def end(answers):  # Shows completed template and waits for the feedback
    print(template_form.format(*answers))  # '*' -> more than one value
    feedback = input("Was it interesting enough? [y/n] ")
    if feedback.lower() == 'y':
        print("Thank you <3\n")
    else:
        print("I will try to be better next time\n")


def menu():  # Main menu
    while True:
        print('''
        ----------------------------
        |         Mad Libs         |
        ----------------------------
        ''')
        print(template_form)
        get_user_input()
        play_again = input("Do you want to play again? [y/n] ")
        if play_again.lower() not in ['y', 'yes', 'ok']:
            print("Have a good day/night")
            break


if __name__ == '__main__':
    menu()
