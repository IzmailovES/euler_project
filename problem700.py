#!/usr/bin/env python3

from math import pow as p

a = 1504170715041707
b = 4503599627370517
e = a%b
pos = [a]
while e != 1:
    e = a-b%a
    pos.append(e)
    b,a = a,e
    print(e)

print(sum(pos))
