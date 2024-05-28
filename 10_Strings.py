str1 = 'Test'
str2 = "Test2"
speech = "Abhijeet's book is with me"
reply = 'He said, "Thanks"'
raw_string = r"This here (\t) is an escape character"

print(raw_string)

path = r"c:\test\newdata"
print(path)

# Comment - Single line

'''
Multi
line
comment
'''

"""
Multi
line
comment
"""

def SomeFunction(x, y, z):
    '''
    IN
    x: int - x coord
    y: int - y coord
    OUT
    z: float - length from (0,0)
    '''
    print("Executing ...")
    if isinstance(x, int) == False:
        print(__doc__)


print(SomeFunction.__doc__)


str3 = "Test""string"           # Adjacent strings are concatenated


# Doc - https://docs.python.org/3.12/reference/lexical_analysis.html


name = "Ramakant"
string1 = "Hello %s"
final = string1.format(name)
print(final)

print(f"Hello {name}")

s1 = "This is a %s training for %d days"
final = s1.format('Python', 5)
print(final)

s1 = "This is a %s training for %d days"
final = s1%('Python', 5)
print(final)


# Slicing
string = "This is a random string"
print(string[0])
print(string[-1])
print(string[5:])
print(string[:8])
print(string[2:7])          # Inclusive - Exclusive idiom

# [start : stop : step]

print(string[2:10:2])
print(string[::-1])
print(string[::2]) # at even indices
print(string[1::2]) # at odd indices
