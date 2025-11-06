def main():
    fruits = {
        'apple':'green',
        'orange':'orange',
        'banana':'yellow'
    }
   # color1 = fruits['mango'] 
   # print(color1) # it throws an error because the key is not found

    color =  fruits.get('mango') # the key is not in the dictionary yet no error
    print(color)

    color = fruits.get('mango','red') # add default if its not available
    print(color)

    color = fruits.get('apple') # pick what is there
    print(color)

    color = fruits.get('apple','red') # pick what is there
    print(color)


main()