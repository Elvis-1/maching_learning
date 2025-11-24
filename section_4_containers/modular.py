"""
for mod 12, 12 is removed from the result and the reminder is taken.
clock
2 + 12 = 2
5 + 12 = 17 = 17 - 12 = 5 (mod 12)
7 + 13 = 8 (mod 12)
"""

def main():
    print((1+12)%12)

    for i in range(0,30):
        print(i%12, end=',')
    animals = ['pig','cow','cat']
    for i in range(0,20):
        print(animals[i % len(animals)],end=' ')
    for i in range(0,10):
        for j in range(len(animals)):
            print(animals[j],end=',')
main()