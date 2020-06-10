# 1.

import math


def check_fermat(a, b, c, n):
    if n > 2 and a ** n + b ** n == c ** n:
        print("Fermat is wrong!")
    else:
        print("Fermat is right on this!")


check_fermat(2, 3, 4, 2)
check_fermat(3, 4, 5, 2)


# 2.

def check_fermat_custom():
    a = int(input("Please in put a: "))
    b = int(input("Please in put b: "))
    c = int(input("Please in put c: "))
    n = int(input("Please input n: "))
    return check_fermat(a, b, c, n)


check_fermat_custom()
