## Set - Mutable ###################

i = 10
s = "Test"
l = [1, 2, 3, 4]
t = (1, 2, 3)

hash(i)
hash(s)
# hash(l)
hash(t)

# Sets are collections of keys (hashable, essentially Immutable)

# s1 = set( [10, 20, 30, 40, 20, 30] )

lst_temp = [10, 20, 30, 40, 20, 30]
s1 = set( lst_temp )

print(type(s1), s1)

print(10 in s1)

s2 = set([40, 50, 60])

print(s1.intersection(s2))

t1 = (1, 2, 3)
a, b, c = t1    # Unpacking a sequence

def fun1(a, b, c):
    pass

fun1(*t1)

def fun2(*pkg):
    pass

fun2(a, b, c)


## FrozenSet - Immutable ############################
fs1 = frozenset(s1)
