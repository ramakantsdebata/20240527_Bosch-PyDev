# def fun(a: int, b: int)->int:
#     return a + b


# print(fun(1, 2))
# print(fun("One", "Two"))

#################################################################################

# Forward declaration - Define Higher  <-- NOT required in Python
# Python operates on 'Define Earlier' principle

# def foo():
#     '''
#     multiline
#     comment
#     '''
#     print("foo")
#     bar()

# def main():
#     print("main")
#     foo()

# def bar():
#     print("bar")

# main()



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

## Variable Args
# def add(a, b, *more):
#     sum = a + b
#     for data in more:
#         sum += data

#     return sum

# lst = []
# a, b, lst = [1, 2, 3, 4, 5, 6]

# # print(add())
# # print(add(1))
# print(add(1, 2))
# print(add(1, 2, 3))
# print(add(1,2, 3, 4))

##  Keyworded VarArgs

# def my_func(**kwargs):
#     print(type(kwargs))
#     for k in kwargs.keys():
#         print(k)
#     print("\n", "-"*10)

#     for v in kwargs.values():
#         print(v)
#     print("\n", "-"*10)

#     for k, v in kwargs.items():
#         print(k, v)
#     print("\n", "-"*10)


# my_func(first="This", second="is", third="Python")


# ## Special Arguments (Sequence of passing)
# def MyFunc(p1, p2, /, p3, p4, *, p5, p6):
#     pass
# # Positional - p1, p2
# # Pos OR Kw - p3, p4
# # KeyWorded - p5, p6
# MyFunc(1, 2, 3, 4, 5, 6)                    # ERROR
# MyFunc(1, 2, 3, 4, 5, p6=6)                 # ERROR
# MyFunc(1, 2, 3, 4, p5=5, p6=6)              # Valid
# MyFunc(1, 2, 3, p4=4, p5=5, p6=6)           # Valid
# MyFunc(1, 2, p3=3, p4=4, p5=5, p6=6)        # Valid
# MyFunc(p1=1, p2=2, p3=3, p4=4, p5=5, p6=6)  # ERROR: p1, p2 can NOT be keyworded

# def MyAdaptive(*varArgs, **kwVarArgs):
#     pass



## Scope

# L-E-G-B
# Local - External - Global - Builtins

s1 = "Global"

def Outer():
    # global s1
    s1 = "Outer"
    
    def Inner():
        # global s1
        # nonlocal s1
        s1 = "Inner"
        print(f"Inner --> {s1}")

        # End of scope for Inner() ####
    
    
    print(f"Outer --> {s1}")
    return Inner
    
    # End of scope for Outer() ####

Outer()()

print(f"Global --> {s1}")


#################################################

# s1 = "Global"

# def MyFunc():
#     # global s1
#     # print(type(globals()), globals())

#     g_s1 = globals()['s1']
#     print(" IDs -->",   id(g_s1),   id( globals()['s1'] ))

#     print("MyFunc -->", g_s1)
#     g_s1 = "Modified"
#     print(" IDs -->",   id(g_s1),   id( globals()['s1'] ))
#     s1 ="Local"
#     print(f"MyFunc --> {s1}")

# MyFunc()
# print(f"Global --> {s1}")


## Higher Order fucntions

## Lambda

## __builtin__

## Preventing Variable Modifications

