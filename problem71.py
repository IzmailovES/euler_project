#!/usr/bin/env python3

import math

ds = set()
for i in range(1,10**6+1):
  #  print(i)
    j = i*3//7
    g = math.gcd(i,j)
    while g != 1:
            i //= g
            j //= g
            g = math.gcd(i,j)
    ds.add((j,i))
ls = sorted(ds,key=lambda x: x[0]/x[1])
print(ls[-1])
print(ls[-2])


