#!/usr/bin/env python3

import math
tr = set()
d = dict()
for i in range(1,1000):
    for j in range(1,1000):
        a,b = math.modf(math.sqrt(i**2 + j**2))
        if not a:
            tr.add(frozenset((i,j,int(b))))
            p = sum((i,j,int(b)))
            if p < 1000:
                d[p] = d.get(p,0) + 1

print(max(d, key = lambda x: d[x]))
