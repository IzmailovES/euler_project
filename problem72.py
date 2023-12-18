#!/usr/bin/env python3

import sympy

def pprimes_count(num):
    ret = 1
    for i,j in sympy.factorint(num).items():
        ret *= i**j - i**(j-1)
    return ret
acc = 0
for i in range(2,10**6+1):
    acc  += pprimes_count(i)
    #print(i)

print(acc)

