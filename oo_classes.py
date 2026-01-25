"""
Procedural programminng (PP) - functions calling functions
Object-oriented programminng (OOP) - classes and objects
Functional programming (FP) -- passing functions to functions

"""

class Person:
    def __init__(self,name):
        print(f'{name} created')
    def eat(self):
        print('I can eat, thank God!')
    def talk(self):
        print('Hello!')


def main():
    person1 = Person('Zoe')
    person2 = Person('Divine')

    person1.eat()
    person2.talk()

main()



