def get_user_info():
    name = input('What is your name? ')
    age = input('What is your age? ')

    return name,age


def main():
    name, height =  get_user_info()
    temp = get_user_info()
    print(type(temp))
    print()
    print(name + ": "+ height)

main()