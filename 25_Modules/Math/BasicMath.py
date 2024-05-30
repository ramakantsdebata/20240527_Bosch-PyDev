__all__ = ['add', 'sub', 'mul', 'div']

x = 10

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def PowerOf(num, exp):
    return num ** exp

if __name__ == '__main__':
# def Test():
    print(add(1, 2))
    print(sub(2, 1))
    print(mul(1, 2))
    print(div(2, 1))

# Test()




#########################################################
# print(f"__name__--> {__name__}")
# print("Executing the Global code")

# __name__ is the name of the scope in which the code is 
# executed
# "__main__" is the scope if the execution is happening 
# from the current or the main scope  in the file