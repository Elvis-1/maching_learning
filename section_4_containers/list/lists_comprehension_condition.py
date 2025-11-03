def main():
    numbers = [x for x in range(20)]
    print(numbers)

    numbers1 = [x for x in numbers if x > 2]
    print(numbers1)

    print(25%4 == 0)

    numbers2 = [x for x in numbers if x % 2 == 1]
    print(numbers2)



main()