


def positional_arguments(one,two,three):
    print(one)
    print(two)
    print(three)

def default_arguments(one,two = 2, three = 3):
    print(one)
    print(two)
    print(three)


def variable_arguments(*args):
    for arg in args:
        print(arg)

def variable_keyword_arguments(**kwargs):
    for key in kwargs:
        print(key,': ', kwargs[key])


def main():
    # positional arguments
    positional_arguments(1,2,3)

    print()

    #  default arguments   
    default_arguments(5)

    print()

    # keyword arguments
    positional_arguments(one='one', two='two',three='three')

    print()

    # variable arguments
    variable_arguments('one','two','three','hello','there')


    print()

    # variable keyword
    variable_keyword_arguments(height = 'height', width ='width', length ='length', one =1, two =2, four =4)


main()