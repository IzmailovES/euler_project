#!/usr/bin/env python3

import math

def less(a:tuple,b:tuple):
    a = a[1]*math.log(a[0])
    b =b[1]*math.log(b[0])
    return a < b

filename = '0099_base_exp.txt'

with open(filename, 'r') as f:
    l = [[int(y) for y in  x.split(',')] for x in f.readlines()]

mi = [1,1]
ii = 0
for i,e in enumerate(l):
    if less(mi,e):
        mi = e
        ii = i+1

print(ii)
