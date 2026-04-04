def main():
    # print(ord('A'))
    # print(chr(65))
    value = 65
    for i in range(4):
        print(chr(value))
        value +=1
    # tutor's method

    letters = [chr(x) for x in range(ord('A'),ord('E'))]
    print(letters)

if __name__ == '__main__':
    main()