"""
Write a function that asks the user to enter their in kilos and thier height in metres, calculate their BMI

(weight divided by height times height)

The function should return all three values
"""

def calBMI():
    weight =float(input('Enter your weight '))
    height = float(input('Enter your height '))

    bmi = weight/(height * height)

    return weight,height,bmi

def main():
    weight, height, bmi =  calBMI()
    print('Weight :',weight, ', ', 'Height :',height, ', ', 'BMI :',bmi)
main()