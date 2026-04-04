def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def print_numbers(n):
    if n == 0:
        return
    print(n)
    print_numbers(n - 1)


def main():
    print(factorial(5))
    print_numbers(10)


if __name__ == '__main__':
    main()