from decimal import Decimal
import decimal

# # x = 0.8
# # y = 0.7
# # z = x - y

# # if z == 0.1:
# #     print("Great")
# # else:
# #     print("What happened?")

# # print(x, y, x-y)


# x = Decimal('0.8')
# y = Decimal('0.7')
# print(x, y, x-y)

# x = Decimal(0.8)
# print(x/2)
# decimal.getcontext().prec = 3
# print(x/2)


# Rounding strategies in Python
# Round Ceiling & Round Floor

def round_it(x, ndigit, strategy=decimal.ROUND_HALF_EVEN):
    dec_num = decimal.Decimal(str(x))
    decimal.getcontext().rounding = strategy
    rounded = dec_num.quantize(decimal.Decimal(f'1e-{ndigit}'))
    print(f'round({dec_num}, {ndigit}, {strategy})'.ljust(35), f" --> {rounded}")











round_it(-4.2, ndigit=0, strategy=decimal.ROUND_DOWN)
round_it(-4.2, ndigit=0, strategy=decimal.ROUND_UP)
round_it(-4.2, ndigit=0, strategy=decimal.ROUND_FLOOR)
round_it(-4.2, ndigit=0, strategy=decimal.ROUND_CEILING)
