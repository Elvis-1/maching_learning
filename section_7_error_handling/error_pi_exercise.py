import math

"""
Docstring for error_pi_exercise

Write a function that calculates pi

You can calculate PI by addinng up a large number of terms of the following series:

pi = 4 x (1/1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ...)

You can check your value against the actual value of pi. Import the math module and then use math.pi
"""

def calculate_pi():
    sum = 0.0
    sign = 1
    for i in range(1,10000,2):
        sum += sign * 1/i
        sign *=-1
      
    return 4 * sum




def main():
   approximated_pi = calculate_pi()

   print('Approximated pi: ', approximated_pi)
   print(math.pi)

main()