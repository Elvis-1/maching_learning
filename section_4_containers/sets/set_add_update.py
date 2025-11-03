def main():
    numbers1 = {1,2,3,4}
    numbers2 = {5,6,7,8}
    numbers1.add(5)
    print(numbers1)

    numbers1.update(numbers2) # you can add any iterable with the update method
    numbers1.update(['car','house'])

    print(numbers1)

main()



