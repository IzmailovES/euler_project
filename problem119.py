#!/usr/bin/env python3

import sympy

def get_sum(num):
    ret = 0
    while num:
        ret += num%10
        num //= 10
    return ret
a = 0
i = 10
maxint = 2**64
bank = []
for i in range(2,1000):
    s = i**2
    while s < maxint:
        if get_sum(s) == i:
            bank.append(s)
        s *= i
bank.sort()
print(bank)
print(bank[29])
exit()

