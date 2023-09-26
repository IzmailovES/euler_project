#!/usr/bin/env python3

import primes

p = primes.Primes()

number = 600851475143
pp = 0
while number != 1:
    if not(number % p[pp]):
        number //= p[pp]
    else:
        pp+=1

print(p[pp])
