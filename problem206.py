#!/usr/bin/env python3

def verify(num):
    s = str(num)
    if len(s) != 19:
        return False
    for i in range(10):
        if int(s[i*2]) != i+1:
            return False
        if s[-1] != '0':
            return False
    return True

for i in range(10**9,10**10):
    if verify(i):
        print(i)

