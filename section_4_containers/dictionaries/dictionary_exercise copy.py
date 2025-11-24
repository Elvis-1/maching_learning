"""
Put this data in a suitable data structure.

Science Fiction: Journey to the Center of the Earth, Day of the Triffids.
Drama: A Tale of Two Cities, Moby Dick

Assume:
1. Categories are unique (cannot have two different categories with the same name)
2. Book titles are unique
3. We want to be able to easily determine which books are in a given category
4. The order of book titles doesn't matter
5. We want to be able to quickly determine if a given book is present in a given category
6. We want to able to easily add books to a category



Now programmatically add this book:

Science Fiction:The War of the Worlds

Do not assume that the category already exists in the data structure. Write a code that will add the book whether the category already exists or not

Print all the categories and the book in them

Write a function that can determine whether a particular book is present in the data structure without knowing the category.

"""


#set1 = {1,2,3,4,5,6,[7,8]} # it throw an error because list is unhashable
tuple1 =(1,2,3,4,5,6)
list1 = [1,2,3,4,5,6]

#set1.add(7) # mutable
# set[2] # not ordered - not subscriptable

# tuple. # not mutable
tuple1[2] # ordered - subscriptable

list1.append(7) # mutable and ordered
# print(hash(set1))




def mySolution(bookStore):
    # libraryLoop(bookStore)
    #checkIfBookExist(bookStore,'Madman of Gadara')
    showLibrary(bookStore)

# my solution
def addBook(bookStore,bookCategory,book):
    check = bookStore.get(bookCategory)
    if check is None:
        bookStore[bookCategory] = {book}
    else:
        bookStore[bookCategory].add(book)

    print(bookStore)

def checkIfBookExist(bookStore,book):
    for keys,values in bookStore.items():

        if book in values:
            print(book + ' exists')
            return
    print('Book does not exist')

def libraryLoop(bookStore):
    doLoop = True 

    while doLoop:
       category = input('Add book category or "quit" > ')
       bookTitle = input('Add book title or "quit" > ')
       
       if category != 'quit'  and bookTitle != 'quit':
           
            addBook(bookStore, category,bookTitle)
       else:
           doLoop = False
           break

def showLibrary(library):
   for category, books, in library.items():
       print(category + ' '+ str(books))

# tutor's solution

def add_book(library,category,book):
    if not category in library:
        library[category] = set()
    library[category].add(book)
    show_library(library)

def find_book(library,book):
    for books in library.values():
        if book in books:
            return True
    return False

def show_library(library):
    for category in library:
        book = library[category]
        print(category+ ': ', end='')
        print(', '.join(book))



def main():

    bookStore = {
      'Science Fiction':{
           'Journey to the Center of the Earth','Day of the Triffids'
        },
      'Drama':{
           'A Tale of Two Cities','Moby Dick'
        }

    }

    add_book(bookStore,'Science Fiction','Day of the Fights')
    print(find_book(bookStore,'Day of the Fights'))


    

    
    
main()