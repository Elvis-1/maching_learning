def main():
    animals = ['dog','rat','pig']

    animals.insert(1,'giraffe')

    print(animals)

    more_animals = ['elephant','cat']

    animals.extend(more_animals)

    print()
    print(animals)

    return

main()