# The Fridge Exercise

'''
Get the user to enter a temperation in celsius.

< 0: Print "Fridge is too cold"
0 - 4: Print "Fridge is OK"
4 - 6: Print "Fridge is warm"
> 6: Print "Fridge broken"
'''

temp = float(input('Enter the fridge temperature in celsius: '))

STATUS_BROKEN = 'Fridge broken'
STATUS_COLD = 'Fridge is too cold'
STATUS_OK = 'Fridge is OK'
STATUS_WARM = 'Fridge is warm'

status = STATUS_BROKEN
if temp < 0:
    
    status = STATUS_COLD
elif  0 <= temp <= 4:
  
    status = STATUS_OK
elif 4 <= temp <= 6:
  
    status = STATUS_WARM

else:
    status = STATUS_BROKEN

print(f'Status: {status}')



