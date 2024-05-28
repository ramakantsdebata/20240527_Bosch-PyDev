# Mutable
lst1 = []
lst2 = list()

def someFunc():
    print("Hi")

lst3 = [1, 2, 3, 4, 5, "String", lst1, lst2, someFunc]
lst3.append("Some more data")
print("Len ->", len(lst3))
print("Len ->", lst3.__len__())
print(lst3) # --> print(str(lst3)) --> print(lst3.__str__()) --> print(lst3.__repr__())
print(str(lst3))
print(lst3.__str__())
print(lst3.__repr__())

# class Test
# {
#     Test operator+(const Test& t);
# };

# Test t1, t2;
# t3 = t1 + t2; // t1.opertator+(t2)

lst3[8]()

lst4 = ["text" * 4]
print(lst4)

lst5 = ["text"] * 5
print(lst5)

print(lst3.reverse())




# # Strings - Shallow copy and modify
# str1 = "Text"
# str2 = str1

# str2[0] = 'N'

# print(str2)
# print(str1)


# Lists - Shallow copy and modify
print("\n")
lst1 = [1, 2, 3]
lst2 = lst1
lst2[1] = 20

print(lst1, lst2, sep='\n')


lst3 = lst1[:]
lst3[2] = 30
print("\n", lst1, lst2, lst3, sep='\n')


lst5 = list("Test")
print(lst5)
print('T' in lst5)

# lst6 = lst3
# lst6 = lst3[:]
lst6 = list(lst3)

## TUPLE - Immutable #####################################

t1 = tuple([1, 2, 3])
print(t1)
t2 = t1
print(t1[2])

t1 = (10, 20, 30)
print(type(t1), t1)

t3 = t1 + t2
print(t3)

t1[2] = 40