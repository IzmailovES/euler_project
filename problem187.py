#!/usr/bin/env python3

import sympy
import math

num = 10**8

max_min_prime = sympy.prevprime(math.ceil(math.sqrt(num)) + 1)
print(max_min_prime)
ret = 0
for i,p in enumerate(sympy.primerange(2, max_min_prime+1)):
    ret += sympy.primepi(num//p) - i 

print(ret)
