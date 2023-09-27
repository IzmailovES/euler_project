#!/usr/bin/env python3

import primes
import math

def factorize():
    cache = dict()
    def inner(num):
        if not num:
            return {1:1}
        acc = dict()
        p = primes.Primes()
        pp = 0
        s_num = num
        lim_num = int(math.sqrt(num)) + 1
        while num != 1:
            if num in cache:
                ret = dict_summ(cache[num], acc)
                cache[s_num] = ret
                return ret
            prime = p[pp]
            if not (num % prime):
                acc[prime] = acc.get(prime, 0) + 1
                num //= prime
            elif num == s_num and prime > lim_num:
                acc = { s_num : 1 }
                cache[s_num] = acc
                return acc
            else:
                pp += 1
        cache[s_num] = acc
        return acc
    return inner

def dict_summ(d1,d2):
    ret = d1.copy()
    for x,y in d2.items():
        ret[x] = d1.get(x,0) + y
    return ret


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

#print (dict_summ({1:2, 3:4}, {0:5, 1:3, 7:8}))
#exit(0)
f = factorize()
#for i in range(10**10 - 1000000, 10**10):
for i in range(10**7):
    #print(i, f(i))
    f(i)
print('done')
print(primes.Primes()[0])
#print(s(200))

