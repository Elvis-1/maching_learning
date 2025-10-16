PASSWORD = 'secret123'

def greeting():
    print('Welcome! No unauthorized access allowed.')
def login():
    password = input("Enter your password: ")
    if password == PASSWORD:
        print("Access granted.")
    else:
        print("Access denied.")

def main():
    greeting()
    login()


main()


