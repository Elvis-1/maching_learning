"""
Exercise: define a single that accepts:
    one or more positional arguments
    zero or more variable arguments
    zero or more variable keyword arguments

    Make the function print out all the arguments it receives
"""

def various_args(name,age,*args,**kwargs):
    print(name)
    print(age)
    for arg in args:
        print(arg)
    
    print('variable keyword')
    for kwarg in kwargs:
        print(kwarg, ': ', kwargs[kwarg])


def main():
    various_args('Kessy','45',1,3,4,5,6, height = 10, width = 20, id = 'Randy', sex = 'male')

main()



