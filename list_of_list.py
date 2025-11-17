def main():
    numbers = [[1,2,3],[4,5,6],[7,8,9]] # this is a two dimensional array because it takes two numbers to get an arbitrary point
    sublist = numbers[1]
    print(sublist)

    print(numbers[2][1]) # two numbers


    #loop

    for i in numbers:
        for j in i:
            print(j,end='')
        print()
    print()
    for i in range(0,len(numbers)):
        for j in range(0,len(numbers[i])):
            print(numbers[i][j], end='')
        print()
main()