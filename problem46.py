#!/usr/bin/env python3

import sympy
import math

def is_square(num):
    return num == int(math.sqrt(num))**2

def is_goldbach(num):
    ## try to reduce by prime
    for i in sympy.primerange(3,num):
        if is_square((num-i)>>1):
            return True
    return False

print(is_goldbach(127111))

f = 9
while True:
    if not sympy.ntheory.isprime(f):
        if not (is_goldbach(f)):
            print('\nfounnd!!: ',f)
            break
    print(f'\r {f}')
    f += 2


