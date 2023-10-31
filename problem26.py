#!/usr/bin/env python3

def get_period(m):
    print(m, end = ' ')
    while not(m&1):
        m >>= 1
    while not(m%5):
        m //=5
    p = 1
    print(m, end = ' ')
    while True:
        r = (10**p)%m
        if r == 1:
            print(p)
            return p
        if not r:
            return 0
        p +=1
        #print((10**p)%m, end = ' ')
    return p

m = 0
p = 1
for i in range(1,1001):
    k = get_period(i)
    if k > m:
        m = k
        p = i
        #print(m,k)
print()
print(p)
