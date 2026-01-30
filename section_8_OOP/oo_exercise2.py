import re

class Media:
    def __init__(self,title):
        self._title = title

    def search_str(self):
       fields = vars(self)
       return " ".join(fields.values())
    
class Book(Media):
    def __init__(self, title,author):
       super().__init__(title)
       self._author = author
    def __str__(self):
        return f'Title: {self._title}\nAuthor: {self._author}'

class Movie(Media):
    def __init__(self, title,director):
       super().__init__(title)
       self._director = director
    def __str__(self):
        return f'Title: {self._title}\nDirector: {self._director}'
    
class Podcast(Media):
    def __init__(self, title,podcast):
       super().__init__(title)
       self._podcast = podcast
    def __str__(self):
        return f'Title: {self._title}\nPodcase: {self._podcast}'


def main():
    media = [
        Book('A journey to the Center of the Earth', 'Jules Verne'),
        Book('Moby Dick', 'Herman Melville.'),
        Book('A Tale of Two Cities', 'Charles Dickens'),
        Movie('Limitless','Neil Burger'),
        Podcast('Cave of Programming Podcast','Episode 1: Why learn to Code?'),
        Podcast('Skeptiko','Is the Delai Lama an Atheist?')
    ]

    while True:
        text = input('search > ').strip()

        if text == 'quit':
            break
        if len(text) == 0:
            continue

        regex = re.escape(text)
        matches_found = False

        for m in media:
          if re.search(regex,m.search_str(), flags=re.I) is not None:
              matches_found = True
              print(m)
        if matches_found is False:
            print('No matches')

main()