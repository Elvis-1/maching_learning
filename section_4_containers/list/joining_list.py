animals1 = ('dog','cat')
animals2 = ('tiger', 'lion')

fruits1 = ['orange','strawberry']
fruits2 = ['banana','apple']

value = 3
# value = value + 5
value += 5
print(value)
print(id(animals1))

animals1 += animals2
print(id(animals1))
print(animals1)
print()
print(id(fruits1))
fruits1 +=fruits2
print(id(fruits1))
print(fruits1)

