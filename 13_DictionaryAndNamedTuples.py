# dt1 = dict()
# dt = dict(A=10, B=20, C=30)

# print(dt1, dt)

# dt['A'] = 100

# dt2 = dict(C=300, D=400, E=500)
# print("Id[dt]:", id(dt))
# dt.update(dt2)
# print("Id[dt]:", id(dt))

# print(dt)

# dt.pop('A')

# print(dt)

# print(dt['G'])


## Named Tuples ########################################

from collections import namedtuple

Point = namedtuple('Point', 'x y')
# Point = namedtuple('Point', ['x', 'y'])

p1 = Point(10, 20)
p2 = Point(15, 25)

print(p1[0], "<-->", p1.x)


# Student = namedtuple('StudentClass', ['Name', 'DateofBirth', 'Standard'])
Student = namedtuple('Student', ['Name', 'DateofBirth', 'Standard'])
st1 = Student('Manish', '12/12/12', 5)
st2 = Student('Rakesh', '1/2/2/', 7)
print(st1[1])
# print(type(Student))

'''
List --> Tuple
Dict --> NamedTuple
Set --> FrozenSet
'''