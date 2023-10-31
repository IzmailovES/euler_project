#!/usr/bin/env python3

import math

def is_triangle(num):
    n = num <<1
    for i in range(1,num):
        if i*(i+1) == n:
            return True
    return False

def is_pentagonal(num):
    n = num *2
    for i in range(1,int(math.sqrt(num)) + 1):
        if i*(3*i-1) == n:
            return True
    return False

def is_hexagonal(num):
    for i in range(1,int(math.sqrt(num)) +1):
        if i*((i*2)-1) == num:
            return True
    return False


def get_tringle(n):
    return (n*(n+1))//2



#print(get_tringle(285))
#print(is_pentagonal(40755))
#exit(0)
i = 286
while True:
    n = get_tringle(i)
    if is_pentagonal(n) and is_hexagonal(n):
        print(i,n)
        break
    i+=1
    #print(n,i)
