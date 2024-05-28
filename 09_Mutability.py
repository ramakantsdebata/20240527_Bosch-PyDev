i = int()
j = i
print(id(i), id(j))


# class Test
# {
#     //char x;
# };

# int arr[10];

# cout << arr[4];

# *(arr + 0)

# t1 = Test()
# Test t2[10]

i = 23423532356243353
j = 23423532356243353
print("\n\n")
print(id(i), id(j), sep='\n')
j += 1
print(i, j, sep='\n')
print(id(i), id(j), sep='\n')


j += 1
print("\n", j, id(j), sep='\n')


print("\n\n")
str1 = "Test"
print(str1, id(str1))
str1 = "TesY"
print(str1, id(str1))
