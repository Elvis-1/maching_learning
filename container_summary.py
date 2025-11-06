"""
type                brackets            ordered?        hashable?                   items must be hashable?
tuple               ()                   yes               yes, if element is hashable               no
list                []                   yes                no                                       no
set                 {}                   no                 no                                       yes
dictionary          {}                   yes                no                                       keys, yes; values, no
"""


fruits = ('Apple','Mangoe','Orange')

# fruits[2] = 'Guava' # immutable

fruits = ['Apple','Mangoe','Orange']

fruits[2] = 'Guava' # mutable
print(fruits)

animals = {'Monkey','Goat','Lion'}
# print(animals[1]) # non ordered

animals.add('Lizard')
print(animals)





