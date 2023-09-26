#!/usr/bin/env python3
import math

class Primes:
    known = [2,3,5,7]
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
                break

    def __getitem__(self,i):
        if not(i < len(Primes.known)):
            while len(Primes.known) -1 != i:
                Primes._invent_prime()
        return Primes.known[i]

if __name__ == '__main__':
    p = Primes()
    print(p[10000])