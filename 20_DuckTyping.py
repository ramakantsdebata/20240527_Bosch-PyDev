def add(a: int, b: int)->int:
    print(f"Adding {a} and {b}")
    return a + b

class MyClass:
    def __init__(self, value) -> None:
        self.val = value

    def __str__(self):
        return str(self.val)
    
    def __add__(self, other):
        return self.val + other.val

def Main():
    print(add(1, 2))
    print(add(1.1, 2.2))
    print(add("First", "Second"))
    m1 = MyClass(10)
    m2 = MyClass(20)
    print(add(m1, m2))

# Main()

##############################################################



# class Animal:
#     def Speak(self):
#         pass

class Cat:
    def Speak(self):
        print("Meow")

class Dog:
    def Speak(self):
        print("Woof")

class Owl:
    pass


# def Communicate(entity: Animal):
def Communicate(entity):
    entity.Speak()


def RunCode():
    c = Cat()
    d = Dog()
    o = Owl()
    Communicate(c)
    Communicate(d)
    Communicate(o)

RunCode()



