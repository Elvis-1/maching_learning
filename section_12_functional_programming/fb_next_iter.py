class Sequence:
    def __init__(self):
        self._values = ['A','B','C','D']

    def __iter__(self):
        self.index = 0
        return self
    def __next__(self):
        self.index +=1

        if self.index > len(self._values):
            raise StopIteration
        
        return self._values[self.index - 1]


def main():
    s = Sequence()

    # for i in s:
    #     print(i)

    it = iter(s)
    print(it)

    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))

if __name__ == '__main__':
    main()