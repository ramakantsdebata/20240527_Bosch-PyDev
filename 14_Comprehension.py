fruits = ['Apple', 'Banana', 'Chiku', 'DragonFruit', 'Mango']

lst = []

for fruit in fruits:
    if 'a' in fruit:
        lst.append(fruit)

print(lst)

c1 = [x                 for x in fruits        if 'a' in x]; print(type(c1), c1)
c2 = {x                 for x in fruits        if 'a' in x}; print(type(c2), c2)
c3 = {x:len(x)          for x in fruits        if 'a' in x}; print(type(c3), c3)
c4 = (x                 for x in fruits        if 'a' in x); print(type(c4), c4)
c5 = tuple(x            for x in fruits        if 'a' in x); print(type(c5), c5)

print("\n"*5)


members = [attr          for attr in dir(int)     if attr.startswith('_') == False]
print(members)

# __call__

# class Test:
#     def __call__(self, a: int, b: int):
#         return a + b

# t1 = Test()

# print(t1(1, 2))