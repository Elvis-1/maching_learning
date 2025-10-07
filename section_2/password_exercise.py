'''
Write a program that asks the user to enter
a password and compares it to a hard-coded password.


if the password is correct, the program prints "Greetings Professor Falcon" and exits.


if the password is incorrect, the program prints "Access denied" and asks for the password again.

The program will ask for the password three timees if necessary.

After that, it exits.
'''


PASSWORD = 'secret123'

for attempts in range(3):
    your_password = input('Enter the password: ')

    if your_password == PASSWORD:
        print('Greetings Professor Falcon')
        break
    else:
        print('Access denied')

else:
    print('Too many incorrect attempts. Exiting.')