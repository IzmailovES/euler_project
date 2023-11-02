#!/usr/bin/env python3

import sympy
import itertools

def is_pandig(num):
    s = str(num)
    l = set(s)
    if len(s) != len(l) or '0' in s:
        return False
    for i in range(1,len(s)+1):
        if not ( str(i) in l):
            return False
    return True

def ip(num):
    n = len(str(num))
    d = [0]
    while num:
        k = num%10
        if k > n or k in d:
            return False
        else:
            d.append(k)
            num //= 10
    return True

def prev_prime_zero_step(num):
    p = sympy.prevprime(num)
    s = str(p)
    k = s.find('0')
    if k != -1:
        return prev_prime_zero_step(int(s[:k] + '0'*(len(s)-k)))
    else:
        return p


print(ip(987654321))
print(ip(987643211))
print(ip(987643))
l = []
for n in range(9,0,-1):
    s_num1 = ''.join(( str(x) for x in range(1,n+1)))
    nums = (int(''.join(x)) for x in itertools.permutations(s_num1))
    for n in nums:
        if sympy.ntheory.isprime(n):
            l.append(n)
print(max(l))
exit(0)



