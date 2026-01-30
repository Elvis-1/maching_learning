class Person:
    def __init__(self,age):
        self._age = age

    def get_age(self):
        return self._age
    def set_age(self,age):
        print('Setting age')
        if age < 0 or age > 150:
            raise ValueError(f'Age {age} is out of range')
        self._age = age
    age = property(fget=get_age,fset=set_age)

def main():
    person = Person(200)
    

    person.age = 120
    print(person.get_age())

main()


