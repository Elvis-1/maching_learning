def greet(name):
    print(id(name))
    print('Hello ' + name)

def main():
    name = 'Kelvin'

    print(id(name))
    greet(name)
main()