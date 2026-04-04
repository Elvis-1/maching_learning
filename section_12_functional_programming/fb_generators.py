def main():
    l = [chr(x) for x in range(65,69)]
    print(l)

    g = (chr(x) for x in range(65,69))
    print(g)

    for i in g:
        print(i)
    
    print(list(chr(x) for x in range(65,69)))
    print(set(chr(x) for x in range(65,69)))
    print(tuple(chr(x) for x in range(65,69)))
    

if __name__ == '__main__':
    main()