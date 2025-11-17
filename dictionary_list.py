def main():
    people = {
        'AL':['Running', 'Programming'],
        'Mark':['Dancing','Designing']
    }

    al = people['AL']
    mark = people['Mark']

    for name,hobbies in people.items():
        print(name)

        for hobby in hobbies:
            print(hobby)
        print('-------------')
    

    animals = {
        'Monkey':{'Greeen', 'Blue'},
        'Dog':{'Red','White','Brown'}
    }
    print()
    
    for animal, colors in animals.items():
        print(animal)

        for color in colors:
            print(color)
        print('---- animals and colors --------')

    # print(animals['Dog'])



main()