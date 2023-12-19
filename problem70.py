#!/usr/bin/env python3

import sympy

def pprimes_count(num_d):
    ret = 1
    for i,j in num_d.items():
        #ret *= i**j - i**(j-1)
        ret *= (i**(j-1 )) * (i -1)
    return ret

def check(num):
    num_d = sympy.factorint(num)
    if len(num_d) != 2:
        return None
    rp = pprimes_count(num_d)
    s_num = str(num)
    s_rp = str(rp)
    if num //rp > 1:
        return None
    if len(s_num) != len(s_rp):
        return None
    if sorted(str(rp)) == sorted(str(num)):
        return num/rp
    return None


acc = 100
n = 0
for i in range(3,10**7+1,2):
    c = check(i)
    if c and c < acc:
        acc = c
        n = i
        print(c, i, sympy.factorint(i))

print(acc, n)

