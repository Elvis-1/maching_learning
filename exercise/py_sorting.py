
"""
Sorting in Python revolves around two primary mechanisms:

list.sort() → in-place sorting
sorted() → returns a new sorted object
Understanding the difference is critical.
"""

# 1️⃣ Sorting a List (In-Place)
numbers = [1,4,2,7,5]
numbers.sort()
print(numbers)

"""
Key Properties
Modifies original list
Returns None
Faster for large lists (no copy created)
"""

# 2️⃣ Using sorted() (Creates New List)
sorted_number = sorted(numbers)
print(sorted_number)

"""
Use this when:
You must preserve original data
You’re sorting non-list iterables (tuple, set, dict keys, etc.)
"""

# 3️⃣ Sorting in Descending Order

numbers.sort(reverse=True)
sorted_rev = sorted(numbers, reverse=True)

print(numbers)
print(sorted_rev)

# 4️⃣ Sorting Strings

names = ['Mike', 'Ada','John']

names.sort() # case sensitive
names.sort(key=str.lower) # case insensitive

sorted(names,key=str.lower) # case insensitive



# 5️⃣ Sorting by a Custom Key (Very Important)

# Example: Sort by length
names.sort(key=len, reverse=True)
print(names)

# 6️⃣ Sorting Dictionaries by Value
data = {"a": 3, "b": 1, "c": 2}

# in place sorting
sorted_data = sorted(data.items(), key=lambda items:items[1])
print(sorted_data)


# 7️⃣ Sorting Objects (Interview Favorite)

people = [
    {"name": "Elvis", "age": 30},
    {"name": "Ada", "age": 25},
    {"name": "Mike", "age": 35}
]

people.sort(key=lambda p:p['age'], reverse=True)
print(people)
sorted_people = sorted(people,key=lambda p:p['age'])
print(sorted_people)

# 8️⃣ Multi-Level Sorting

# Sort by age, then by name:
people.sort(key=lambda person: (person["age"], person["name"]))


"""
| Scenario                | Use            |
| ----------------------- | -------------- |
| Modify original list    | `.sort()`      |
| Preserve original       | `sorted()`     |
| Sort complex structures | `key=`         |
| Descending              | `reverse=True` |

"""

"""
Interview Question You Might Get

“How would you sort a list of users by signup date descending?”
You should immediately think:
"""

# users.sort(key=lambda u: u["signup_date"], reverse=True)


