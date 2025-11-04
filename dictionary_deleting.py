def main():
    fruits = {
        'apple':'green',
        'orange':'orange',
        'banana':'yellow'
    }

    del fruits['banana']

    print(fruits)

    color = fruits.pop('orange')

    print(color)
    print(fruits)

    



main()