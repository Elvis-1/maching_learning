def main():
    days = ['Sun','Mon','Tues','Wed','Thurs','Fri','Sat']

    days[0:2] = []
    print(days)

    days.remove('Sat')
    print(days)
    days.pop()

    print(days)

    item =  days.pop(0)

    print(item)
    print(days)

    del days[1]

    print(days)

    days.clear()
    print(days)

    
    return

main()