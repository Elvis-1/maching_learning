def main():
    fruits = ['orange','banana','mangoe','apple']

    print(len(fruits))
    print(fruits[1])
    print()
    print(fruits[0:2])

    # convert tuple to list

    animals = ('fox','rabbit', 'dog')
    animals = list(animals)

    print(animals)

    print()
    for animal in animals:
        print(animal)

main()