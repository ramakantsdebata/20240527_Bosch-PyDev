from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def Speak(self):
        print("Let's chat")

    def Eat(self):
        print("Where's the food?")

class Cat(Animal):
    def Speak(self):
        print("Meow")

class Dog(Animal):
    def Speak(self):
        print("Woof")

class Owl(Animal):
    def Speak(self):
        print("Hoot")
    
    def Eat(self):
        print("Had food")



def Communicate(entity: Animal):
    entity.Speak()


def RunCode():
    c = Cat()
    d = Dog()
    o = Owl()
    Communicate(c)
    Communicate(d)
    # Communicate(o)
    o.Eat()

    a1 = Animal()

    d2: Animal = Dog()
    

RunCode()
