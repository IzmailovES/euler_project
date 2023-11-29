#!/usr/bin/env python3

import sympy

num = 10**8
acc = 1
for i in range(2,num+1,4):
    if not (sympy.ntheory.isprime(i+1) and sympy.ntheory.isprime((i>>1)+2)):
        continue
    divs = sympy.divisors(i)
    for j in range(2,len(divs)>>1):
        if not sympy.ntheory.isprime(divs[j] + divs[-1 -j]):
            break
    else:
        acc += i
print(acc)
        
