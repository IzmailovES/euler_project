#!/usr/bin/env python3

import sympy

dn = sympy.ntheory.divisor_count

ret = 0 
pi = 1 
for i in range(2,10**7 + 2): 
    ni = dn(i)
    if ni == pi: 
        ret += 1
    pi = ni

print(ret)
