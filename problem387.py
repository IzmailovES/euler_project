#!/usr/bin/env python3

import sympy
import math
import functools

def digsum(num):
    acc = 0
    while num:
        acc += num%10
        num //= 10
    return acc

def is_harshad(num):
    return not num%digsum(num)

def is_harshad_strong(num):
    d = digsum(num)
    if num%d:
        return False
    else:
        return sympy.ntheory.isprime(num//d)

def trunc_generator(maxlen):
    ret = {x:[] for x in range(1,maxlen+1)}
    ret[1] = list(range(1,10))
    for i in range(2,maxlen+1):
        toadd = []
        for n in ret[i-1]:
            for a in range(10):
                k = n*10+a
                if is_harshad(k):
                    toadd.append(k)
        ret[i] = toadd
    return ret

mynumbers = list(functools.reduce(lambda x,y : x+y,  trunc_generator(13).values()))
mynumbers = list(filter(lambda x: is_harshad_strong(x), mynumbers))
acc = 0
for i in mynumbers:
    for j in range(1,10,2):
        k = i*10+j
        if sympy.ntheory.isprime(k):
            acc += k
print(acc)




