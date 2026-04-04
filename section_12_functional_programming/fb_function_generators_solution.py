def powers_of_two(n):
    power = 1
    for _ in range(0,n):
        yield power
        power *=2
        

def main():
    for x in powers_of_two(5):
        print(x)

if __name__ == '__main__':
    main()
