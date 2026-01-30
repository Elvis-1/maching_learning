class Alarm:
    def arm(self):
        # print(self)
        print("Alarm on!")
    
    def disarm(self):
        print("Alarm off!")

class Vehicle:
    def __init__(self,people):
        self._people = people
    
    def __str__(self):
        return f"Carries {self._people} people"



class Car(Vehicle,Alarm):
    def start(self):
        print('Car starting')

def main():
    car = Car(4)
    car.arm()

main()