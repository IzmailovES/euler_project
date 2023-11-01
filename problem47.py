#!/usr/bin/env python3

import sympy
import math

def is_four_factor(num):
    if sympy.ntheory.isprime(num):
        return False
    p = 2
    #l = set()
    c = 0
    while num != 1 and c != 5:
        if not num%p:
            c += 1
            while not num%p:
                num //= p
        p = sympy.nextprime(p)
    return c == 4

l = []
c = 0
i = 1
while c != 4:
    if is_four_factor(i):
        #l.append(i)
        c += 1
        #print(i)
    else:
        #l = []
        c = 0
    i += 1
print(i - 4)

print(is_four_factor(645))
