"""
Docstring for oo_exercise

Create a class called Media.
Create the following subclasses: Book, Movie, Podcast

Each subclasses should contain instance variables appropraite to the type of media, and should be convertible to a string which displays this information.

Create several instances of each class and add them to a container

Write a program that displays a prompt, like this:

search > 

When the user enters a word or phrase, the program searches all Media objects to find a match in their details. If any matches are found, it displays them.

If no matches are found, it prints "No match",

If the user types "quit", the program terminates. Otherwise it displays the prompt again.
"""

class Media:
    def __init__(self,title):
        self._name = title
    
    def get_name(self):
        return self._name
        
class Book(Media):
    def __init__(self, title,author):
       super().__init__(title)
       self._author = author
    def __str__(self):
        return f'Title: {self._title}n\Author: {self._author}'

class Movie(Media):

    def __init__(self, title,director):
       super().__init__(title)
       self._director = director
    def __str__(self):
        return f'Title: {self._title}n\Director: {self._director}'
    
class Podcast(Media):
    def __init__(self, title,podcast):
       super().__init__(title)
       self._podcast = podcast
    def __str__(self):
        return f'Title: {self._title}n\Podcase: {self._podcast}'

def add_istance_container(container,*media,):
   
   for med in media:
      
    if isinstance(med,Book):
        container[med.get_name()] = med
        # print(med)
    if isinstance(med, Podcast):
        container[med.get_name()] = med
    if isinstance(med,Movie):
        container[med.get_name()] = med



def main():
    container = {}
    book1 = Book('Abestoes')
    movie1 = Movie('Traveller')
    podcast1 = Podcast('Seer')

    add_istance_container(container,book1,movie1,podcast1)
    
    search_media = None

    while search_media != 'quit':
      search_media = input('Search> ')
      
      if search_media in container:
        print(container[search_media])
      else:
        print('No Match')
    
    for cont in container:
        print(cont)
    
    
    
    
main()

