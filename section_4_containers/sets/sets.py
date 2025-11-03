numbers = {1,2,3,2,3}

print(numbers)

numbers_list = [1,2,3,4,5,3,4,3,1]

print(set(numbers_list)) # converting numbers_list to set to get the unique items.

for number in numbers:
    print(number)

print(3 in numbers) # checking item exist in set
print(10 in numbers)

"""
list: ordered,"in" is slow, mutable
tuple: ordered, "in" is slow, immutable
set: unordered, "in" is fast, mutable
"""