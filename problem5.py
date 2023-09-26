#!/usr/bin/env python3
n = 100
print(sum([x**2 for x in range(1,n+1)]) - sum([x for x in range(1, n+1)])**2)

