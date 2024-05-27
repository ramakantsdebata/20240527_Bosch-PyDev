from decimal import Decimal
import decimal

# x = 0.8
# y = 0.7
# z = x - y

# if z == 0.1:
#     print("Great")
# else:
#     print("What happened?")

# print(x, y, x-y)


x = Decimal('0.8')
y = Decimal('0.7')
print(x, y, x-y)

x = Decimal(0.8)
print(x/2)
decimal.getcontext().prec = 3
print(x/2)


# Rounding strategies in Python
# ROUND_HALF_EVEN
# ROUND_HALF_UP
# ROUND_CEILING
