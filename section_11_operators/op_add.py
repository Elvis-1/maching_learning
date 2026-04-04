class Clock:
    def __init__(self,value):
        self._value = value

    def __str__(self):
        display_value = self._value % 12
        if display_value == 0:
            display_value = 12
        
        return f"{display_value} {'am' if (self._value % 24) < 12 else 'pm'}"
    def __add__(self, other):
        return Clock(self._value + other._value)
    def __neg__(self):
        return Clock(self._value + 12)


def main():
    c1 = Clock(7) # 7am

    c2 = Clock(19) # 7pm

    c3 = Clock(0) # 12am

    c4 = Clock(12) # 12pm
    # print(c1)
    # print(c2)
    # print(c3)
 


if __name__ == '__main__':
    main()
   