# import builtins
# print(dir(builtins))

# # __builtin__
# # __builtins__
# # builtins

# def print():
#     pass

# builtins.print("Hello")


from __future__ import barry_as_FLUFL

x = 10
y = 20

print(x != y)
print(eval("x <> y"))
# print(eval("x != y")) # SyntaxError: with Barry as BDFL, use '<>' instead of '!='

