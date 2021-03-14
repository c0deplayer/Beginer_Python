# Author: CodePlayer
# Date: 12.02.2021
import ujson
import os

contacts = {}


def load_file():   # Loads the file if available otherwise creates an empty json file
    global contacts
    if os.path.isfile('contacts.json') and os.access('contacts.json', os.R_OK):
        with open('contacts.json', 'r') as file:
            contacts = ujson.load(file)
        print("File 'contacts.json' exists and is readable\nLoading...")
    else:
        print("Either file 'contacts.json' is missing or is not readable\nCreating file...")
        with open('contacts.json', 'w') as file:
            ujson.dump({}, file)


def save_file():   # Saves changes to the file
    with open('contacts.json', 'w') as file:
        ujson.dump(contacts, file, sort_keys=True)


def contact_list():   # Shows contact list if dictionary is not empty
    if contacts:
        print('''
        +================+
           Contact List
        +================+
        ''')
        for k, v in sorted(contacts.items()):
            print(f"\t{k} -> {v}")
    else:
        print("\nContact list is empty")


def contact_book(choice):
    if choice == '2':
        name = input("Please enter the name: ")
        if name not in contacts:
            number = input("Please enter the number: ")
            contacts[name] = number
            print("Contact saved successfully!")
        else:
            print("\nThe contact is already on the list")
    elif choice == '3':
        name = input("Please enter the name you wish to delete: ")
        if name in contacts:
            confirm = input("Are you sure you want to delete this contact? [y/n] ")
            if confirm.lower() in ['y', 'yes', 't']:
                contacts.pop(name, None)
                print("The contacts list has been updated")
        else:
            print("\nThe contact doesn't exist! Returning to main menu")
    elif choice == '4':
        name = input("What contact do you want to check? ")
        if name in contacts:
            print(f"\nName: {name}, Number: {contacts[name]}")
        else:
            print("\nThe contact doesn't exist! Returning to main menu")
            
    if choice in ['1', '2', '3']:
        save_file()
        contact_list()


def welcome():   # Main menu
    load_file()
    while True:
        print('''
        =================================
             Welcome to Contact Book
        =================================
           1. Show saved contacts
           2. Save new contact
           3. Delete contact
           4. Check contact
           5. Exit
        ''')
        choice = input("Enter one of the available option: ")
        if choice in ['1', '2', '3', '4']:
            contact_book(choice)
        elif choice == '5':
            print("Have a good day/night")
            break
        else:
            print("Please, try again")


if __name__ == '__main__':
    welcome()
