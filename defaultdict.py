from collections import defaultdict

people = defaultdict(int)

people.update({
    'Bob':45,
    'Adria':30,
    }
    )

print(people['Matthew']) # prints default which is int
print(people['Bob'])
