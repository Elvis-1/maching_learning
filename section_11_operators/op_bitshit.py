def printb(value):
    print(f"{value & 0b11111111:08b}")

def main():
  pass

if __name__ == '__main__':
    num1 = 0b10001000

    printb(num1)

    printb(num1 >> 1)
    printb(num1 >> 4)
    num1 >>= 2

    printb(num1) 

    print(10 >> 1) # dividing in the power of 2
    print()
    num1 = 0b01001000
    printb(num1)
    printb(num1 << 3)


    print(10 << 3) # multiplying in the power of 2