#!/usr/bin/env python3
import math, itertools

def in_mask(num):
    q = 0
    p = 0
    while num:
        q += (num%10)*(10**p)
        num //=100
        p += 1
    return q == 123456789

i = 101010101
while True:
    if in_mask(i**2):
        print(i)
        break
    i += 2


