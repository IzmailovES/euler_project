#!/usr/bin/env python3

## special Pythagorean triplet

import math

for i in range(2,1000):
    for j in range(i,1000):
        o,k = math.modf(math.sqrt(i**2 + j**2))
        if not o and (i+j+k) == 1000:
            print('find triplet:', i, j, k, i*j*k) 

#print(math.modf(math.sqrt(3**2 + 4**2)))
