#!/usr/bin/env python3

def d(num): ## sum of all divisors
    ret = 0
    for i in range(1,(num+1)>>1):
        if not ( num%i):
            ret += i
    return ret

def s(n):
    cache = dict()
    ret = 0
    for i in range(1,n+1):
        for j in range(1, n+1):
            #ret += cache.setdefault(i*j, d(i*j))
            ret += d(i*j)
    return ret

print(s(200))

