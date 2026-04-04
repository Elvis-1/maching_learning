def main():
    print([x for x in range(0,3)])
    
    # exercise
    # can you combine the both expression and do the expressionns work  with a generator
    print([x for x in range(0,3) if x > 0])
    print(['*' if x%2 == 0  else x for x in range(0,20)])

    # 1
    print()
    print(['x' if x%2 == 0 else x for x in range(0,20) if x >0]) 

    # 2
    print()
    print((x for x in range(0,20) if x%2==0))
    g = (x for x in range(0,20) if x%2==0)

    for i in g:
        print(i)
    
    print(('x' if x%2 == 0 else x for x in range(0,20) if x >0)) 


if __name__ == '__main__':
    main()