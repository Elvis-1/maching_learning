"""
Print all the cubic numbers up to and including 729
Print all the square numbers up to and including 729

Which cubic numbers are also square numbers?
Which cubic numbers are not square numbers?

"""

def cubicNumbers():
    cubic_set = { x*x*x for x in range(10)}
    square_set = { x**2 for x in range(28)}
    print('cubic')
    print(cubic_set)
    print('square')
    print(square_set)

    # cubic numbers that are also square numbers

    print('cubic numbers that are also square numbers')
    print(cubic_set.intersection(square_set))

    # # cubic numbers that are not square numbers
    print('cubic numbers that are not square numbers')
    print(cubic_set.difference(square_set))


def main():
    cubicNumbers()

main()