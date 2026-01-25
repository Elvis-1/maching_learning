class Machine:
    def __init__(self,id,name):
        self._name = name
        self._id = id


class Car(Machine):
    def __init__(self, id, name,type):
        #Machine.__init__(self,id,name)
        super().__init__(id,name)
        self._type = type
    
    def __str__(self):
        return f'This is the name {self._name} and id {self._id}'

def main():
    car1 = Car(12343,'THX3434','RX223')
    print(car1)


main()