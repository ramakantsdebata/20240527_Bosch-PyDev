# Int
# Float
# None
# Bool


# import math
# print(math.pow(2, 64))


print(type(5/2))
print(type(5//2))

val1 = bool()
print(val1)

print(bool(0))
print(bool(1))
print(bool("True"))
print(bool("False"))
print(bool(""))
print(bool([1, 2, 3]))
print(bool([]))
print(bool(False))


x = None
print(x)
# y = x + 10

print(x is None)


x = 10
print(x)
print(hex(x))
print(oct(x))
print(bin(x))

print("X -->", int('10000', 3))


##  Float


# 22.56   --> 2.256 x 10**1

p = 3.125
q = 3e8
r = 1.234e-12

print(p, q, r)

print(  type(  int(  p  )  )  )


p = float('1.5')
print(type(p), p)

print(float('nan'))
print(float("inf"))
print(float("-inf"))

print("#" * 20)

print(float(2**53))
print(float(2**53 + 1))
print(float(2**53 + 2))
print(float(2**53 + 3))
print(float(2**53 + 4))
print(float(2**53 + 5))
print(float(2**53 + 6))
