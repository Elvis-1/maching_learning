WORKER1 = 'Elvis'
WORKER2 = 'John'
PROFESSOR = 'Albert'

name = input('Enter your name:')

if name == WORKER1:
    print('Welcome back Elvis!')
elif name == WORKER2:
    print('Welcome back John!')
elif name == PROFESSOR:
    print('Welcome back Professor Albert!')

else:
    print('Your name is not recognized!')

