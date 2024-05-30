
x = 10

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def pow(num, exp):
    return num ** exp

if __name__ == '__main__':
    print(add(1, 2))
    print(sub(2, 1))
    print(mul(1, 2))
    print(div(2, 1))

print(f"__name__--> {__name__}")
print("Executing the Global code")
