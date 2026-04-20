from functools import reduce
from operator import add


def word_guesses():

    gueses = set('aeiou')
    word = 'fascinate'

    result = reduce(add,map(lambda x: ' - ' if x  not in gueses else x , word))
    result = ' '.join(map(lambda x: ' - ' if x  not in gueses else x , word))

    print(result)





    
def main():
    word_guesses()

if __name__ == '__main__':
    main()