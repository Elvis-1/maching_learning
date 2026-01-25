class Animal():
    def speak(self):
        print('I am an animal')

class Cat(Animal):
    def speak(self):
        print('I am a cat')


def main():
    cat1 = Cat()
    cat1.speak()

main()