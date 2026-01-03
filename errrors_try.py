def greeting():
    print('Hello')
    print(1/0)


def main():
    try:
        greeting()
    except:
        print('Something went wrong')
    
main()