"""
Write a program that asks the user to enter a name.

If the user enters a name in the list below, respond with the age of the person entered. Otherwise print "Unknown person"

Make the program keep askinng for the names like this until the user enters 'quit'. Then the program exits.

Start by putting the names and ages in a dictionary


"""

# my solution
def checkDataBase(ages,peoples):
    # dataBase = {people[i]:ages[i] for i in range(len(people))}

    dataBase = {people:age for people, age in zip(peoples,ages)}
    print(dataBase)
    doLoop = True

    while doLoop:
        name = input('Enter your name or quit ')
        checkList = name in peoples
        if checkList:
            print('This is your aga: ' + str(dataBase[name]))
        elif name == 'quit':
            doLoop = False
            print('Bye for now')
        else:
            print("Unknown person")

# tutor solution
def userLoop(lookUp):
    doLoop = True
    while doLoop:
        userInput = input('Enter your name or "quit" > ')
        check = userInput in  lookUp

        if userInput == 'quit':
            break
        elif not check:
            print('Unknown Person')
            continue
        else:
            print(userInput + ' is age '+ str(lookUp[userInput]))

def lookUp(people,ages):
    db = dict()

    for i in range(0,len(people)):
        name = people[i]
        age = ages[i]
        db[name] = age
    return db


def main():
    people = ["Amelia","Arthur","Isla","Ava","Leo","Mia","Oscar",'Mat']
    ages = [20, 30, 25, 65, 21, 70, 32, 45]
    
    checkDataBase(ages,people)
    # look_up = lookUp(people,ages)

    # userLoop(look_up)
   

    dictT = {}


    

main()