

def main():
    animals = ['dog','Lion','cat','Monkey']

    def lower(str):
        return str.lower()

    animal = map(lower,animals)
    print(animal)

    animal_list = list(map(lower,animals)) # cast to a list
    print(animal_list)

if __name__ == '__main__':
    main()
