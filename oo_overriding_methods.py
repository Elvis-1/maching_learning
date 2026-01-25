

class Animal():
    def speak(self):
        print('I am an animal')
    
    def eat(self):
        print('I am eating')


class Cat(Animal):
        def speak(self):
          print('I am a cat')

def main():
    cat1 = Cat()
    cat1.speak()
    cat1.eat()

main()
