#!/usr/bin/env python3

def get_spiral_item(n):
    a,b,c,d = 1,1,1,1
    acc = 1
    for i in range(n>>1):
        a = d + 2*(i+1)
        b = a + 2*(i +1)
        c = b + 2*(i + 1)
        d = c + 2*(i + 1)
        acc += a+b+c+d
    return acc

print(get_spiral_item(1001))




