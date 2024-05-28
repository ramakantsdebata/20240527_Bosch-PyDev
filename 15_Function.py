# def fun(a: int, b: int)->int:
#     return a + b


# print(fun(1, 2))
# print(fun("One", "Two"))

#################################################################################

# Forward declaration - Define Higher  <-- NOT required in Python
# Python operates on 'Define Earlier' principle

# def Foo():
#     '''
#     Multiline
#     comment
#     '''
#     print("Foo")
#     Bar()

# def Bar():
#     print("Bar")

# def Main():
#     print("Main")
#     Foo()

# Main()


#############################################################################

# def func(a, b, c):
#     if False:
#         return
#     else:
#         print("C: ", c)
#         c = a + b
#     print(c)

# res = 100 
# func(10, 20, res)
# print(res)
###########################################################################


# def add(a, b, c=0):     # Default arg
#     return a + b + c

# # res = add(1, 2, 3)
# res = add(1, 2)             # Positional arg


# res = add(b=2, c=3, a=1)    # Named arg

# print(res)

##########################################################################

## Variable Args & Keyworded VarArgs

## Scope

## Higher Order fucntions

## Lambda

## __builtin__

## Preventing Variable Modifications

