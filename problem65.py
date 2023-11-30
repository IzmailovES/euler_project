#!/usr/bin/env python3

import math

e_seq = [2]
i = 1
while len(e_seq) < 100:
    e_seq.extend([1,i<<1,1])
    i += 1
e_seq = e_seq[:100]

def drob_simplyfy(drob_src):
    drob = drob_src[:]
    g = math.gcd(drob[0],drob[1])
    while g != 1:
        drob[0] //=g
        drob[1] //=g
        g = math.gcd(drob[0],drob[1])
    return drob


def drob_summ(drob1, drob2):
    ret = [drob1[0]*drob2[1] + drob2[0]*drob1[1], drob1[1]*drob2[1]]
    return drob_simplyfy(ret)

def drob_reverse(drob):
    return drob[::-1]

def get_seq(src_seq):
    ret = (0,1)
    for i in range(len(src_seq) - 1, 0, -1):
        ret = drob_reverse(drob_summ(ret,[src_seq[i],1]))
    ret = drob_summ(ret, [src_seq[0],1])
    return ret
num = get_seq(e_seq)[0]
ret = 0
while num:
    ret += num%10
    num = num//10
print(ret)


