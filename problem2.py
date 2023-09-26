#!/usr/bin/env python3

a,b = 1,1
s = 0
while True:
    c = a+b
    if c >= 4000000:
        break
    if not (c&1):
        s += c
    a,b = b,c
print(s)
