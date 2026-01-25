import re
"""
Write a function that converts feet to miles.

(miles = feet x 1.89E-4)

Using this function, write a program that asks the user to enter a distance in feet and converts it to miles.

If the user enters a valid input, print the distance in miles to three decimal places and quit.
If the user enters invalid input, print "Invalid input" as ask them again.

If the user enters 'quit', quit the program

Mount Everrest is 29,028 feet high. How high is it in miles?




"""
def convertFeetToMiles():
#  isLoop = True
#  while(isLoop):
    try:
        user_input = input('Enter a distance in feet: ')
        user = re.sub(r',','',user_input)
        
        # print(user)
        # return
        if user == 'quit':
           return
        # convert
        feet = int(user)
        miles = int(feet) * 1.89E-4
        print(f'{miles:.3f} miles')
        isLoop = False
        return
    except Exception as e:
        print('invalid input')
        print('This is the eror',e)

    


def main():
    convertFeetToMiles()

    

    
    

    

main()
