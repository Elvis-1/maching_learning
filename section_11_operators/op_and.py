def printb(value):
    print(f"{value:08b}")

def main():
    number1 = 0b01110110
    number2 = 0b01010111
    printb(number1)
    printb(number2)
    printb(number1 & number2) # sets to zero where any of the position is zero


if __name__ == '__main__':
    main()