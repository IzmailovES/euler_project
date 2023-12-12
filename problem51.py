#!/usr/bin/env python3

import  sympy
import collections

def get_mask(num):
    s_num = str(num)
    ret = dict()
    for i in ('0', '1', '2'):
        if i in s_num:
            i_ret = []
            for j in range(len(s_num)):
                if s_num[j] == i:
                    i_ret.append('1')
                else:
                    i_ret.append('0')
            ret[int(i)] = int(''.join(i_ret))
    return ret

def check_family(num, shift, misses, target):
    passed = 1
    fails = misses
    max_misses = 10 - target
    while fails !=  (max_misses +1) and passed != target:
        num += shift
        if sympy.ntheory.isprime(num):
            passed += 1
        else:
            fails += 1
    return passed == target


num = sympy.nextprime(10)
while True:
    for m,sh in get_mask(num).items():
        b = check_family(num, sh, m, 8)
        if b: 
            print(num)
            exit()
    num = sympy.nextprime(num)
exit()
