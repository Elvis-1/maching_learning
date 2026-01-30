class Person:
    def __init__(self,name):
        self._name = name
        print(f'{self._name} created')
        print(id(self))
    def eat(self):
        print('I can eat, thank God!')
    def talk(self):
        print('Hello!')


def main():
    person1 = Person('Zoe')
    person2 = Person('Divine')

    person1.eat()
    person2.talk()

    print(id(person1))
    print(id(person2))

    person1.age = 50
    person2.age = 30

    print(person1.age)
    print(person2.age)

    print(person1._name)
    print(person2._name)



main()