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


    for x in dir(Machine): # dir is used to access properties of methods of a class
        print(x)

    print(Machine.mro())

    print()

    for x in dir(object):
        print(x)
    print(object.mro())

    
    
    

main()