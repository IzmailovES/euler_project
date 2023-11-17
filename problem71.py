#!/usr/bin/env python3

import math

ds = set()
for i in range(1,10**6+1):
  #  print(i)
    j = i//7*3
    g = math.gcd(i,j)
    while g != 1:
            i //= g
            j //= g
            g = math.gcd(i,j)
    ds.add((j,i))
print(len(ds))
ls = sorted(ds,key=lambda x: x[0]/x[1])
print(ls[-1])
print(ls[-2])
print(ls[-3])
print(ls[0])


