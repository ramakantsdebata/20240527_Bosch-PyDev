import random

class Integer(object):
    
    def __init__(self, value) -> None:
        self.val = value

    def add(self, a, b):
        self.processed_data = a + b
        return self.processed_data


###############################################

# def genSerial():
#     return random.randint(10000)

class Car:
    total_cars = 0

    def __init__(self, make, model, color, mileage) -> None:
        self.__make = make
        self.__model = model
        self.__color = color
        self.__mileage = mileage
        self.__speed = 0
        self.__serial = Car.genSerial()
        Car.total_cars += 1

    @classmethod
    def getCarTotal(cls):
        return cls.total_cars
    
    @staticmethod
    def about():
        return "This is a Car class"
    
    @staticmethod
    def genSerial():
        return random.randint(10000)
    
    def __str__(self) -> str:
        return f"{self.__make} car, model {self.__model} of color {self.__color}"
    
    def start(self):
        print(f"{self.__color} {self.__model} started.")
    
    def stop(self):
        print(f"{self.__color} {self.__model} stopped.")

    @property    
    def speed(self):
        return self.__speed
    
    # @speed.setter
    # def speed(self, value):
    #     self.__speed = value

    def run(self, kms):
        print(f"{self.__color} {self.__model} ran {kms} distance.")

    
def Main():
    print(f"Total cars created - {Car.getCarTotal()}")
    c1 = Car("Maruti", "Ciaz", "White", 20)
    print(c1)
    c2 = Car("Lamborgini", "Diablo", "Black", 20)

    c2.start()
    # c2.setSpeed(40)
    # print(c2.getSpeed())

    # c2.speed = 40
    print(c2.speed)

    c2.stop()

    print(f"Total cars created - {Car.getCarTotal()}")

    print(c1.__class__.__name__)

Main()




