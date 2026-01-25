import math

def calculate_pi():
    sum = 0.0
    sign = 1
    for i in range(1,10000,2):
        sum += sign * 1/i
        sign *=-1
    pi = 4 * sum

    assert abs(pi - math.pi) < 0.0001,f'PI is out of range {pi}'
    return pi
   




def main():
   approximated_pi = calculate_pi()

   print('Approximated pi: ', approximated_pi)
   print(math.pi)

main()