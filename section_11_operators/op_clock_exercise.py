class Clock:
    def __init__(self,value):
        self._value = value

    def __str__(self):
        display_value = self._value % 12
        if display_value == 0:
            display_value = 12
        
        return f"{display_value} {'am' if (self._value % 24) < 12 else 'pm'}"
        
    def convert_to_twelve_hour(self):
       
        if self._value%12 == self._value:
             if self._value == 0:
                print('12','am')
             else:
                 print(self._value,'am')
        else:
            if self._value%12 == 0:
                print('12','pm')
            else:
             print(self._value%12,'pm')



def main():
    c1 = Clock(7) # 7am

    c2 = Clock(19) # 7pm

    c3 = Clock(0) # 12am

    c4 = Clock(12) # 12pm
    print(c1)
    print(c2)
    print(c3)
    print(c4)


if __name__ == '__main__':
    main()
   