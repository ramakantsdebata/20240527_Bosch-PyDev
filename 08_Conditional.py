cond1 = True
cond2 = True

if cond1:
    pass
elif cond2:
    pass
else:
    pass

## LOOPS #############################################

# For
l1 = [1, 2, 3, 4, 5]
for x  in l1:
    print(x)

for _ in range(10):
    print("Hi")


for x in range(10):
    if x == 5:
        continue
    print("Hello")

for x in range(10):
    if x == 5:
        break
    print("World")

for x in range(10):
    if x == 5:
        break
    print("String1")
else:
    print("Else block")

# while(cond1):
#     print("String2")
# else:
#     print("While-else")


idx = 5
cond3 = (idx != 0)
# while(cond3):         # <-- Avoid implicit
while(cond3 == True):
    print(idx)
    idx -= 1
    cond3 = (idx != 0)

opt = 5
match opt:
    case 1:
        pass
    case 2:
        pass
    case _:
        pass
