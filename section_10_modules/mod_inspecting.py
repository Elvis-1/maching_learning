import sys
from games import game_of_life as gol

def main():
    value = 7
    # print(locals())
    # print(dir()) # returns a list of attributes defined in the file if no argument is passed in

    # for attr in dir(sys):
    #  print(attr)
    
    for attr in dir(gol):
       print(attr)


if __name__ == '__main__':
    main()