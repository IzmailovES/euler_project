#!/usr/bin/env python3

import sympy
import math

def is_palindrome(s):
    l = len(s)
    for i in range(l//2):
        if s[i] != s[l-i-1]:
            return False
    return True

def test(num):
    #num2 = num**2
    num2 = int(str(num**2)[::-1])
    #print(num2)
    a,b = math.modf(math.sqrt(num2))
    #print(a,b)
    b = int(b)
    if not a:
        if sympy.ntheory.isprime(b):
            if num != b:
                #print('!!!')
                return True
    return False
    

acc = 0
n = 0
num = sympy.nextprime(1)
print(test(13))
#exit()
while n < 50:
    if test(num):
        acc += num**2
        n += 1
        print('->>>', n,num)
    num = sympy.nextprime(num)
print(acc)



