#!/usr/bin/env python3

import math

fs = {x:math.factorial(x) for x in range(10)}
def eval(num):
    return sum([fs[int(x)] for x in str(num)])


def chain_len(num):
    s = set()
    ret = 0
    while not num in s:
        s.add(num)
        num = eval(num)
        ret += 1
    return ret

ret = 0
for i in range(10**6):
    if chain_len(i) == 60:
        ret += 1
print(ret)
