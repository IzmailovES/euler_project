#!/usr/bin/env python3

import sympy
import math

lim = 10**6
ip = sympy.ntheory.isprime
primes = list(sympy.primerange(lim))
s_primes = set(primes)
ad = {x:1 for x in primes}

for i_st in range(len(primes)-1):
    acc = 0
    counter = 0
    i = i_st
    p = primes[i]
    while acc < lim:
        try:
            acc += primes[i]
        except:
            print(i,i_st,len(primes))
            exit(1)
        counter += 1
        if acc in s_primes:
            ad[acc] = max(counter, ad[acc])
        i += 1

print(max(ad, key=lambda x: ad[x]))



