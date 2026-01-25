class Cat:
    
    def __init__(self,name,weight):
        self._name = name
        self._weight = weight

    def introduce(self):
        print(f'Hi, my name is {self._name}, I weigh {self._weight} kg')

    def __str__(self):
        return f'Name: {self._name}\nWeight: {self._weight}'

def main():
    cat1 = Cat('Ruffies',1.2)
    cat2 = Cat('Madea',1.3)

    cat1.introduce()
    cat2.introduce()
    
    
    cat_string1 = str(cat1)

    print(cat_string1)
    print(cat1)

main()