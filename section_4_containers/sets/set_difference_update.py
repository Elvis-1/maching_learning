def main():
    numbers1 = {1,2,3,5,7,8,9}
    numbers2 = {0,4,6,8}

    print(numbers1.difference_update(numbers2))

    print(numbers1.issuperset(numbers2))

    print({1,2,3,4}.issuperset({1,2,3}))

    

main()