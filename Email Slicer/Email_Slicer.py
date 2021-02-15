# Author: CodePlayer
# Date: 15.02.2021

def main():   # Nothing interesting to see here
    email = input("Enter an email address: ").strip()
    username = email[:email.index('@')]
    domain = email[email.index('@') + 1:]
    print(f'''
    The program successfully get the username and domain name from an email address
      > Username: {username}
      > Domain: {domain}
    ''')


if __name__ == '__main__':
    main()
