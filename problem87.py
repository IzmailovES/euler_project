#!/usr/bin/env python3
from sympy import primerange
import math
def get_num(a,b,c):
    return a**2 + b**3 + c**4

acc = 0
n = 5*10**7
s = set()
for i in primerange(2,n**(0.5)):
    for j in primerange(2,n**(1/3)):
        for k in primerange(2, n**(1/4)):
            num = get_num(i,j,k)
            if num > n:
                break
            s.add(num)

print(len(s))

