class PowersOfTwo:

    def __init__(self,max):
        self._max = max

    def __iter__(self):
        self.last_value = 1
        self._index = 0
        return self
    

    def __next__(self):
        result = self.last_value
        self._index +=1
        self.last_value *=2
        if self._index > self._max:
            raise StopIteration
        return result

pot = PowersOfTwo(5)

for i in pot:
    print(i)

for x, y in enumerate(pot):
    print(x,y)