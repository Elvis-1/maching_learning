class Machine:
    _id = 0
    def __init__(self,name):
        Machine._id +=1
        self._name = name
        self._id = Machine._id
    
    def __str__(self):
        return f'The id of machine {self._name} is {self._id}'
    
    @classmethod
    def get_id(cls):
        return Machine._id
    
    @classmethod
    def create(cls): # factory method
        return cls('Unknown')





def main():
    machine1 = Machine('THX1232')
    machine2 = Machine('RBV1232')
    machine3 = Machine('MRT1232')
    machine4 = Machine('QRT1232')
    print(machine1)
    print(machine2)
    print(machine3)
    print(Machine.get_id())
    print(Machine.create())
    
    
    

main()