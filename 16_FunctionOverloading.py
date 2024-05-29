from multipledispatch import dispatch

@dispatch(int, int)
def add(a, b):
    print(a + b)

@dispatch(int, int, int)
def add(a, b, c):
    print(a + b + c)

add(1, 2)
add(1, 2, 3)