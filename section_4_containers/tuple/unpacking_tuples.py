def main():
    elements = (True,3.7,6,'goat') # packing tuple
    (is_raining,volume,height,animal) = elements # unpacking

    print(is_raining)
    print(volume)
    print(height)
    print(animal)

    fruits = ('apple', 'mangoe','pawpaw','orange')

    (fruit1,fruit2,fruit3,fruit4) = fruits
    print()
    print(fruit1)
    print(fruit2)
    print(fruit3)
    print(fruit4)
    print()
    (fruit1,fruit2,fruit3, *more_fruits) = fruits
    print()
    print(fruit1)
    print(fruit2)
    print(more_fruits)





main()
