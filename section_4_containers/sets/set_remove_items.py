def main():
    numbers = {x for x in range(15)}
    print(numbers)

    numbers.remove(6)

    print(numbers)

 #   numbers.remove(20) # this will throw an error since item is not the set

    numbers.discard(20) # a better approach

    # never rely on the order of the numbers or the items in set
    for x in numbers:
        print(x)



main()