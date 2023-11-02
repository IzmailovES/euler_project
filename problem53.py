#!/usr/bin/env python3

import math

n_max = 100
f = math.factorial
def c(n,r):
    return f(n)//(f(r)*f(n-r))

acc = 0
for i in range(1, n_max+1):
    for j in range(1,i):
        if c(i,j) > (10**6):
            acc += 1
print(acc)

