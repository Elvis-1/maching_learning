class Widgets:
    count = 0

    def __init__(self, name):
        self._name = name

        Widgets.count +=1
        print(f'Widget created counts: {Widgets.count}')

    def __str__(self):
        return self._name
    

def main():
    widget1 = Widgets('Terminal View')
    widget2 = Widgets('Widget View')

    print(widget1)
    print(widget2)

    print(Widgets.count)


main()
