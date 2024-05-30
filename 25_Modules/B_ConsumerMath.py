## Imports for Test1() 
# from Math.BasicMath import *
# from Math.BasicMath import PowerOf

def Test1():
    try:
        print(add(2, 3))
    except NameError as e:
        print(f"Error (add): {e}")

    try:
        print(sub(2, 3))
    except NameError as e:
        print(f"Error (sub): {e}")

    try:
        print(mul(2, 3))
    except NameError as e:
        print(f"Error (mul): {e}")

    # Attempt to use pow (should raise a NameError)
    try:
        print(PowerOf(2, 3))
    except NameError as e:
        print(f"Error (PowerOf): {e}")

def Test2():
    from Math.BasicMath import add, sub

    try:
        print(add(2, 3))
    except NameError as e:
        print(f"Error (add): {e}")

    try:
        print(sub(2, 3))
    except NameError as e:
        print(f"Error (sub): {e}")

import Math
import Math.BasicMath

Math.BasicMath.add

Test2()
