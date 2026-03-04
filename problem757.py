#!/usr/bin/env python3

import sympy

def how_many(x, lim):
    a = lim / (x*(x+1))
    sqa = a**0.5
    ret = int(sqa)
    while ret*(ret+1) > a:
        ret -= 1
    return ret - x + 1 

ret = 0 
a = 1 
x = 1 
cache = set()
while(a > 0): 
    a = how_many(x, 10**14)
    if a <= 0:
        break
    ret += a
    for i in range(x,x+a):
        k = x*(x+1)*i*(i+1)
        if k in cache:
            ret -= 1                                                                                                                                         
        cache.add(k)
    print(x,x+a-1, a)
    x += 1
print(ret)
