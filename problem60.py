#!/usr/bin/env python3

import sympy

known = ['3','19']
primes = list(sympy.primerange(3,10**4))
def concat(p):
    l = len(p)
    for i in range(1,l):
        for j in range(i):
            p1 = int(p[i]+p[j])
            p2 = int(p[j] + p[i])
            if (not sympy.ntheory.isprime(p1)) or (not  sympy.ntheory.isprime(p2)):
                return False
    return True

setcache = dict()
def get_set(prime):
    global primes
    if prime in setcache:
        return setcache[prime]
    ret = set()
    s_prime = str(prime)
    for i in primes:
        if i <= prime:
            continue
        if concat((s_prime , str(i))):
            ret.add(i)
    setcache[prime] = ret
    return ret

sums = []
def func(num, sett, counter):
    l = len(counter)
    if l == 5:
        print(counter, sum(counter))
        sums.append(sum(counter))
        return counter
    if not sett:
        return counter
    for i in sorted(sett):
        ret = func(i,sett & get_set(i), counter + [i])

print('go calculate')
for i in primes:
    func(i,  get_set(i), [i])
print(min(sums))
