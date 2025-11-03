def main():
    numbers = [x for x in range(20) if x/2 > 2]

    print(numbers)

    more_numbers = [x if x > 10 else 0 for x in numbers]

    print(more_numbers)


main()