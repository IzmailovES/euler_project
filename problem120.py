#!/usr/bin/env python3

import math

def get_sum_c(n):
    nf = math.factorial(n)
    ret = 0
    for k in range(0, n, 2):
        ret += nf // (math.factorial(k) * math.factorial(n-k))
    return ret

print(get_sum_c(3)*2)

ret = 0
for i in range(3,1001):
    ret += ( i*(i-1) if i&1 else i*(i-2))

print(ret)
