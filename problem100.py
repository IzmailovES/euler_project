#!/usr/bin/env python3

#1070379110497 756872327473

import sympy
import math

thrsh = 10**12
#thrsh = 100
if thrsh % 4:
    thrsh += 2

def get_nedd_devs(num):
    divs = sympy.divisors(num)
    n = len(divs)
    if n % 2:
        return None
    if divs[n//2] - divs[n//2-1] == 1:
        return divs[n//2]
    return None


def get_nedd_devs1(num):
    k = int(num ** (0.5))
    if k * (k+1) == num:
        return k + 1 
    return None

def get_nedd_devs2(num):
    k = math.isqrt(num)
    if k * (k+1) == num:
        return k + 1 
    return None


g = get_nedd_devs2
thrsh //= 2
startnum  = int(10**12 * 0.70715)
#startnum = 80

while True:
#    print(startnum)
    num = startnum * (startnum-1) * 2 
    print(num)
    k = math.isqrt(num)
    if k * (k+1) == num:
        print(k+1, startnum)                                                                                                                                 
        exit(0)
    startnum += 1


while True:
#    print(thrsh)
    b = g(thrsh * (thrsh-1) // 2)
    if b is not None:
        print(b)
        exit(0)
    thrsh += 4
    
