
def showMenu(menu):
        print()
        for item in range(0,len(menu)):
            print(str(item+1) + '.', menu[item])
        print()
def displayDB(db):
    for index, item in enumerate(db):
        print(str(index) + ':', item)

def addItem(db):
    newItem = input('Enter a new item to add the database ')
    db.append(newItem)
def deleteItem(db):
    newItem = input('Enter number in the list to be deleted ')
    db.pop(int(newItem))
def updateItem(db):
    itemIndex = input('Enter number in the list to be changed ')
    newText = input('Enter the text to update to ')
    db[int(itemIndex)] = newText

def myDBSolution():
    menu = ('Display database','Add an item','Delete an item','Change an item','Quit')
    db = ['orange','banana','blackberry']
    

    

    doLoop = True
    while doLoop:

        showMenu(menu)
        selectMenu = input('Select a menu: ')
        
        if selectMenu == '1':
            displayDB(db)
            
        elif selectMenu == '2':
            addItem(db)
           

        elif selectMenu == '3':
            deleteItem(db)

                
        elif selectMenu == '4':
            updateItem(db)
            
        elif selectMenu == '5':
            doLoop = False
        else:
            print('Unexpected response')

    

    



def main():
     myDBSolution()






main()