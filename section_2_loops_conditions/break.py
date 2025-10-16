for i in range(5):
    print('Starting loop number ' + str(i))
    
    stop = input('Stop the loop (y/n)? ')

    if stop.lower() == 'y':
        break


    print ('Ending loop number ' + str(1))

print('Program finished')
