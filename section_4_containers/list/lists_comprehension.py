def main():
    animals = ['dog','goat','rat','lion']

    animals1 = animals
  #  del animals1[1]
    print(animals1) # still refers to thesame list
    print(animals) # still refers to thesame list
    
    # how to correct get a copy
    # animals2 = animals.copy()
    # del animals2[1]
    # print(animals2)
    # print(animals)


    # a better way if you want to manipulate the items

    animals3 = [animal.upper() for animal in animals]
    print(animals)
    print()
    print(animals3)

    lengths = [len(text) for text in animals]
    print(lengths)

    numbers = [1,2,3,4,5]
    print()
    numbers1 = [x*x for x in numbers]
    print(numbers1)

    print()

    hundred_numbers = [x+1 for x in range(100)]

    print(hundred_numbers)

main()

