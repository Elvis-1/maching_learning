def printb(value):
    print("{:08b}".format(value))

def main():
    number1 = 0b01110110
    number2 = 0b01010111
    printb(number1)
    printb(number2)
    printb(number1 | number2) # combining two binary numbers


if __name__ == '__main__':
    main()