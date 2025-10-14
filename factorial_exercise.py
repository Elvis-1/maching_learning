"""
Write a function that calculates the factorial of a given number.

The factorial of a number is defined like this:

n! = n * (n - 1) * (n - 2) * ... * 1

e.g.
3! = 3 * 2 * 1 = 6
5! = 5 * 4 * 3 * 2 * 1 = 120

The factorial of zero, 0! is defined to be 1.

calculate the factorial of 7, i.e 7!

Hint:
Use a loop
Create a variable before the loop, and have the loop repeatedly alter the number that the variable refers to.
"""

def calculateFactorial(value):
    result = 1
    for i in range(1,value + 1):
        result = result * i
    return result


def main():
 factorial = calculateFactorial(5)
 print(factorial)

main()