#!/usr/bin/env python3

import primes
import math
def is_prime(num):
    if not (num & 1) or num < 0:
        return False
    for i in range(3, int(math.sqrt(num))+ 1, 2):
        if not (num%i):
            return False
    return True

def prime_generator_counter(a,b):
    n = 0
    while is_prime(n**2 + a*n + b):
        n += 1
    return n

m = 0
ii = 0
jj = 0
for i in range(-1000, 1000):
    for j in range(1000):
        k = prime_generator_counter(i,j)
        if k > m:
            m = k
            ii = i
            jj = j

print(ii * jj, m)
