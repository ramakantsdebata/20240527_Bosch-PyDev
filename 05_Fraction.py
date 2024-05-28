from decimal import Decimal

PI_old = Decimal('22')/Decimal('7')

print(PI_old*7)

from fractions import Fraction

PI = Fraction(22,7)
PI = Fraction('22/7')
# PI = Fraction(22/7)       # <-- Avoid 
one_tenth = Fraction('0.1')

print(PI, one_tenth)
print(PI * 7)