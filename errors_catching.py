def greeting():
    print('Hello')
    print(1/0)


def do_greeting():
    print('Hello')
    d = dict()
    g = d['hello']
    greeting()

def main():
    try:
        do_greeting()
    except KeyError:
        print('The key does not exist')
    except ZeroDivisionError:
        print('Trying to divide by zero')
    except:
        print('Something went wrong')
    
main()