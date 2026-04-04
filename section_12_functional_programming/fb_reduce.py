from functools import reduce
from operator import add


def main():
    numbers = [1,2,3,4,5,6]

    print(reduce(lambda x,y:y+x, numbers))
    print(reduce(add,numbers))

if __name__ == '__main__':
    main()