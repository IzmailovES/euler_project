#!/usr/bin/env python3

def get_spiral_item(n):
    a,b,c,d = 1,1,1,1
    acc = 1
    for i in range(1, (n>>1) +1):
        k = i<<1
        a = d + k
        b = a + k
        c = b + k
        d = c + k
        acc += a+b+c+d
    return acc

print(get_spiral_item(1001))




