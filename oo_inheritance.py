import re

class IDException(Exception):
    pass


class Machine:
    def __init__(self,name,id):
        self._name = name
        self._id = id

        if re.search(r"\d",self._id) is None:
            raise IDException('ID must contain a digit')

    def __str__(self):
        return f'This is the name of the machine {self._name} ID {self._id}'
    
    def get_name(self):
        return self._name
    
    def set_id(self,id):
        self.id = id
        
class Car(Machine):
    pass 




def main():
    car1 = Car("THX4543",'78767')

    print(car1)

    print(car1.get_name())



main()