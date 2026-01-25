class Machine:
    def __init__(self,name,id):
        self._name = name
        self._id = id

    def __str__(self):
        return f'This is the name of the machine {self._name} ID {self._id}'
    
    def get_name(self):
        return self._name
    
    def set_id(self,id):
        self.id = id
        
    




def main():

    m = Machine('TH123X34',78987)

    print(m)

    name = m.get_name()
    print(name)

    m.set_id(123436)
    print(m.id)


main()