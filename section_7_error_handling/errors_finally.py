def main():
    try:
        pass
        raise ZeroDivisionError('You can\'t divide by zero')
        #raise KeyError('Fake key error!')
    except (ZeroDivisionError, KeyError) as err:
        print(err)
    else:
        print('No exception occcured')
    finally:
        print('Finally is always executed, whether their is an exception or not!')

main()