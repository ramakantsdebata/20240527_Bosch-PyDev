def Square(num):
    return num**2

tools = [lambda num:num**0, lambda num:num**1, lambda num:num**2, lambda num:num**3]
tools.append(lambda x: x%2 == 0)


print(tools[0](10))
print(tools[1](10))
print(tools[2](10))
print(tools[3](10))
print(tools[4](10))
print(tools[4](11))


# def add(a, b):
#     return a + b

def sub(a, b):
    return a + b

def mul(a, b):
    return a + b

def Operation(x, y, operator):
    return operator(x, y)


# print(Operation(3, 1, add))
# print(Operation(3, 1, sub))
# print(Operation(3, 1, mul))


print(Operation(3, 1, lambda x, y: x + y))
print(Operation(3, 1, lambda x, y: x - y))
print(Operation(3, 1, lambda x, y: x * y))
