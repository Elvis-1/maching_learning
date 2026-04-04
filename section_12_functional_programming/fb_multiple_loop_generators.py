def main():
    print(list((x,y) if x%2 == 0 else '=' for x in range(0,4) if x !=1 for y in range(0,4) if y !=2))

    #
    print()
    result = []

    for x in range(0,4):
        if x == 1:
            continue
        for y in range(0,4):
            if y == 2:
                continue
            if x%2 == 0:
                result.append((x,y))
            else:
                result.append(('='))
    print(result)




 

if __name__ == '__main__':
    main()
