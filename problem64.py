#!/usr/bin/env python3

import math

def get_sq(n):
    ret = [math.isqrt(n)]
    real_sq = math.sqrt(n)
    drob = (1, ret[0])
    while ret[-1] != 2 * ret[0]:
        den = (n - drob[1]**2)//drob[0]
        ret.append(int((real_sq + drob[1])//den))
        drob = (den , (ret[-1]*den - drob[1]))
    return ret 


print(get_sq(23))
print(get_sq(12))
ret = 0 
for i in range(2,10000 + 1):                                                                                                                                 
    if math.isqrt(i)**2 != i and len(get_sq(i))%2 != 1:
        ret += 1

print(ret)
