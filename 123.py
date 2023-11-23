#!/usr/bin/env python3

import sympy

n = 800800**800800
k = 1013277
acc = 0
print('vvv')
primes = {x:sympy.prime(x) for x in range(1,k+1)}
print('^^^')
for i in range(1,k):
    print(i)
    ii = primes[i]
    for j in range(i+1,k+1):
        jj = primes[j]
        if ii**jj*jj**ii <= n:
            acc +=1
        else:
            print(i,ii,j,jj, primes[j-1], acc)
            break

print(acc)
