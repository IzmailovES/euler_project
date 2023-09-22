#!/usr/bin/env python3
import math
def nod(a,b):
    if a < b:
        a,b = b,a
    ret = b
    while True:
        d = a%b
        if not d:
            return b
        a,b = b,d


def e_function_dummy(num):
    if num == 1:
        return 1
    count = 0
    for i in range(1,num):
        if nod(num,i) == 1:
            count += 1
    return count

class Primes:
    known_primes = [2,3,5,7,11]
    def __init__(self):
        self.pivot = 0
    @classmethod
    def find_next_prime(cls):
        candidate = cls.known_primes[-1] + 2
        while True:
            for i in range(cls.known_primes[0], int(math.sqrt(candidate) + 1)):
                if not (candidate%i):
                    candidate += 2
                    break
            else:
                cls.known_primes.append(candidate)
                return

    def get_next_prime(self):
        if self.pivot >= len(Primes.known_primes):
            Primes.find_next_prime()
        self.pivot += 1
        return self.known_primes[self.pivot - 1]

    def get_count_primes(self,num):
        i = 0
        while num:
            yield self.get_next_prime()
            num-=1

def factorize(num):
    if num == 1:
        return [1]
    ret = []
    p = Primes()
    d = p.get_next_prime()
    while num != 1:
        if not num%d:
            ret.append(d)
            num /= d
        else:
            d = p.get_next_prime()
    return ret

def separate_dubles(l):
    ret = [1 for _ in range(len(l))]
    p = 0
    el = l[p]
    for i in l:
        if i == el:
            ret[p] *= el
        else:
            el = i
            p += 1
            ret[p] *= el
    return [x for x in ret if x != 1]

def e_function_clever(num):
    ret = 1
    l = separate_dubles(factorize(num))
    for x in l:
        if x in Primes.known_primes:
            ret *= x-1
        else:
            ret *= e_function_dummy(x)
    return ret

m = 0
for x in range(1,1000000):
    print(x)
    e = x/e_function_clever(x)
    if e > m:
        m = e
print(m)
exit(0)
