#!/usr/bin/env python3
import math

class Primes:
    known = [2,3,5,7]
    known_set = {2,3,5,7}
    @classmethod
    def _invent_prime(cls):
        candidate = cls.known[-1] +2
        while True:
            a = math.sqrt(candidate)
            for i in Primes.known:
                if not (candidate%i) and i <= a:
                    candidate += 2
                    break
            else:
                cls.known.append(candidate)
                cls.known_set.add(candidate)
                break

    def __getitem__(self,i):
        if not(i < len(Primes.known)):
            while len(Primes.known) -1 != i:
                Primes._invent_prime()
        return Primes.known[i]

    @classmethod
    def get_set(cls):
        return cls.known_set

def nod(a,b):
    if a < b:
        a,b = b,a
    ret = b
    while True:
        d = a%b
        if not d:
            return b
        a,b = b,d


if __name__ == '__main__':
    p = Primes()
    print(p[10000])
