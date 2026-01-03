def greeting():
    print('Hello')
    print(1/0)


def do_greeting():
    print('Hello')
    # d = dict()
    # g = d['hello']
    greeting()

def main():
    try:
        do_greeting()
    except KeyError as ke:
        print(f"key Error: {ke}")
    except ZeroDivisionError as z:
        print(f'Error: {z}')
    except:
        print('Something went wrong')
    
main()