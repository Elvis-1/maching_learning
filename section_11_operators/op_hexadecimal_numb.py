"""
Exercise 1
Print a table of numbers from 0 to 225.

Print each number in decimal, binary and hexadecimal format

Exercise 2

red     0x12
green   0x34
blue    0x56

combinedd color:  0x123456

Write a function that accepts three colors red, green and blue. The function returns a single integer that combines all three colors, as above.

Write another function that acceepts a single combined color and returns the red, green and blue components.


"""


def print_in_various_format():
    print('Hexadecimal','|', 'Binary','|' ,'Decimal') 
    for i in range(5):
        print( "{:08x}".format(i),'|',"{:08b}".format(i),'|',i)
        print()


def main():
    print_in_various_format()

if __name__ == "__main__":
    main()