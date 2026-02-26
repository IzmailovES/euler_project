#!/usr/bin/env python3

import math
import sympy

def s_dummy(p):
    return (math.factorial(p-1) +  math.factorial(p-2) +  math.factorial(p-3) +  math.factorial(p-4) +  math.factorial(p-5)) % p 

def s_dummy1(p):
    return (((p-1)*(p-2)*(p-3)*(p-4) + (p-2)*(p-3)*(p-4) + (p-3)*(p-4) + (p-4) + 1) * math.factorial(p-5)) % p 

def s_dummy2(p):
    return (( 9  * math.factorial(p-5)) % p) if sympy.isprime(p) else 0

def s_dummy3(p):
    return  ((9 % p)   * (math.factorial(p-5) % p)) % p 

def s_dummy4(p):
    return  (9 * factormod(p-5,p)) % p 

def s_fast(p):
    return ( 9 * factorminus5(p)) % p 

def s_fmod(p):
    ret = 0                                                                                                                                                  
    for i in range(1,6):
        ret += (math.factorial(p-i) % p)
    return int(math.fmod(ret,p))

def factormod(n, m): 
    ret = 1 
    for i in range(1,n+1):
        print(ret, end=" ")
        ret = (ret * i) % m 
    return ret 

def factorminus5(n):
    return ((n % 24) * n - 1) // 24


s = s_fast

ret = 0 
for p in sympy.primerange(5,10**8):
    n = s(p)
    ret += n
print(ret)
