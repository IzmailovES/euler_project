#!/usr/bin/env python3
import primes

def multi_d(dct):
    # all items in dct is prime:power
    #return functools.reduce(lambda x,y: x*y, ( (x**(dct[x] + 1) -1)//(x-1) for x in dct ), 1)
    ret = 1
    for x in dct:
        ret *= (x**(dct[x]+1) -1)//(x - 1)
    return ret

def d_count(dct):
    ret = 1
    for i in dct.values():
        ret *= (i+1)
    return ret
n = 1
step = 1
while True:
    dc = d_count(primes.factor(n))
    if dc > 500:
        print(n)
        break
    step += 1
    n += step

