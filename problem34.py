#!/usr/bin/env python3

import math
d = {str(i): math.factorial(i) for i in range(10)}
def df(num):
    return sum((d[i] for i in str(num)))

acc = 0
for i in range(3,10000000):
    if i == df(i):
        acc += i
        print(acc)
