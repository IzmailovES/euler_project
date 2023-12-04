#!/usr/bin/env python3

import math

fs = {x:math.factorial(x) for x in range(10)}
def eval(num):
    return sum([fs[int(x)] for x in str(num)])

ch = dict()
def chain_len(num):
    c_num = num
    s = set()
    ret = 0
    while not num in s:
        if num in ch:
            ch[c_num] = ret+ch[num]
            return ch[c_num]
        s.add(num)
        num = eval(num)
        ret += 1
    ch[c_num] = ret
    return ret

ret = 0
for i in range(10**6):
    if chain_len(i) == 60:
        ret += 1
print(ret)
