#!/usr/bin/env python3

import math

def expanding(num):
    d = (1,2)
    for _ in range(num-1):
        d = drob_reverse(drob_summ((2,1),d))
    return drob_summ((1,1),d)
    

def drob_summ(d1,d2):
    d3 = [d1[0]*d2[1] + d2[0]*d1[1], d1[1]*d2[1]]
    while True:
        g = math.gcd(d3[0], d3[1])
        if g != 1:
            d3[0] //= g
            d3[1] //= g
        else:
            break
    return d3[0],d3[1]

def drob_reverse(d1):
    return d1[1], d1[0]


#print(drob_reverse(drob_summ((1,1), (7,19))))

#print(expanding(2))

acc = 0
for i in range(1,1001):
    d = expanding(i)
    if len(str(d[0])) > len(str(d[1])):
        acc += 1
print(acc)
