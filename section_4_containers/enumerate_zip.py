fruits = ['Mango','Orange','Apple']
animals = ['Lizard','Monkey','Parrot']

for i, item in enumerate(fruits):
    print(i,item)

for fruit, animal in zip(fruits,animals):
    print(fruit, animal)