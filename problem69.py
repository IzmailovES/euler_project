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



Primes.find_next_prime()
print(Primes.known_primes)
print(e_function_dummy(2850))
exit(0)
p = Primes()
for i in range(20):
    print(p.get_next_prime())

for i in range(2,100):
    print(i, e_function_dummy(i))
