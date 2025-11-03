def main():
    numbers1 = {1,2,3,4,6,6,7}
    numbers2 = {0,8,4,5,8,9}

    print(numbers1.union(numbers2))
    print('Difference')
    print(numbers1.difference(numbers2))
    print(numbers1 - numbers2)
    print(numbers2.difference(numbers1))
    print(numbers1.symmetric_difference(numbers2))

main()