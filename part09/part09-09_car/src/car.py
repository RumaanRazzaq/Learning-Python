# WRITE YOUR SOLUTION HERE:
class Car:
    def __init__(self) -> None:
        self.__petrol = 0
        self.__reading = 0
    
    def fill_up(self):
        self.__petrol = 60

    def drive(self, km:int):
        if km <= self.__petrol:
            self.__reading += km
            self.__petrol -= km
        else:
            self.__reading += self.__petrol
            self.__petrol -= self.__petrol
    
    def __str__(self) -> str:
        return f"Car: odometer reading {self.__reading} km, petrol remaining {self.__petrol} litres"