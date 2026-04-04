def double(n):
    return n * 2

def apply(values,function):
    result = []
    for value in values:
        result.append(function(value))
    
    return result



def main():
    numbers = [1,2,3,4,5]

    result = apply(numbers,double)
    print(result)

if __name__ == '__main__':
    main()