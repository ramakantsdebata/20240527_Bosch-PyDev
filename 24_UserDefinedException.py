# class MyClass:
#     def __init__(self, value) -> None:
#         self.val = value

# def Test():
#     obj1 = MyClass(1)
#     obj2 = MyClass(2)
#     print("Starting...")
#     # sum  = obj1 + obj2
#     raise Exception("Exceptiuon raised.")
#     print("End")

# def Foo():
#     Test()

# Foo()

#######################################################################


class CustomException(Exception):
    def __init__(self, message, code) -> None:
        self.message = message
        self.code = code
        super().__init__(self.message, self.code)

class InvalidAgeException(ValueError):
    def __init__(self, message, code) -> None:
        self.message = message
        self.code = code
        super().__init__(self.message, self.code)


## Validating code ########################################################

def checkAge(age):
    if age < 0:
        raise InvalidAgeException("Age cannot be negative", 1002)
    if age < 18:
        raise InvalidAgeException("Age must be 18 or above.", 1001)
    print("Age is valid")


## Client code ############################################################

def Main():
    try:
        checkAge(-5)
    except InvalidAgeException as ex:
        print(f"InvalidAgeException occured: {ex.message} (Error code: {ex.code})")
    except CustomException as ex:
        print(f"CustomException occured: {ex.message} (Error code: {ex.code})")

    try:
        checkAge(16)
    except InvalidAgeException as ex:
        print(f"InvalidAgeException occured: {ex.message} (Error code: {ex.code})")
    except CustomException as ex:
        print(f"CustomException occured: {ex.message} (Error code: {ex.code})")

    try:
        checkAge(24)
    except InvalidAgeException as ex:
        print(f"InvalidAgeException occured: {ex.message} (Error code: {ex.code})")
    except CustomException as ex:
        print(f"CustomException occured: {ex.message} (Error code: {ex.code})")


Main()


