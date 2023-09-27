#!/usr/bin/env python3

import primes

def factorize(num):
    if not num:
        return {1:1}
    acc = dict()
    p = primes.Primes()
    pp = 0
    while num != 1:
        prime = p[pp]
        if not (num % prime):
            acc[prime] = acc.get(prime, 0) + 1
            num //= prime
        else:
            pp += 1

    return acc


def d_old(num): ## sum of all divisors
    ret = 0
    for i in range(1,(num+1)>>1):
        if not ( num%i):
            ret += i
    return ret

def d(num):
    delimers = factorize(num)


def s(n):
    cache = dict()
    ret = 0
    for i in range(1,n+1):
        for j in range(1, n+1):
            #ret += cache.setdefault(i*j, d(i*j))
            ret += d(i*j)
    return ret



for i in range(10**5):
    print(i,factorize(i))
print(primes.Primes()[0])
#print(s(200))

