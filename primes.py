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
                #print(f'invite new prime {candidate}')
                break

    def __getitem__(self,i):
        if not(i < len(Primes.known)):
            while len(Primes.known) -1 != i:
                Primes._invent_prime()
        return Primes.known[i]

    @classmethod
    def get_set(cls):
        return cls.known_set


def dict_summ(d1,d2):
    ret = {**d1, **d2}
    #print(d1,d2,ret)
    for x in d1:
        if x in d2:
            ret[x] += d1[x]
    #print(ret)
    return ret

def factorize_rec(max_cachesize = 500**2):
    cache = dict()
  #  i = 0
    def update_cache(num, delimers):
        if num < max_cachesize:
            cache[num] = delimers
           # print(num,cache, sep = '\t')
    time_summ = 0
    def inner(num, pp = 0):
        if not num:
            return dict()
        if num == 1:
            return dict()
        s_num = num
        # если число простое - возвращаем
        if num <= Primes.known[-1] and num in Primes.get_set():
            return {num:1}
        # если находим в кеше - возвращаем
        if num <= max_cachesize and num in cache:
            return dict(cache[num])
        # пытаемся поделить на простые числа по  очереди до корня из себя:
        acc = dict()
        lim = int(math.sqrt(num)) + 1
        while num != 1:
            #prime = primes.Primes()[pp]
            prime = Primes()[pp]
            if prime > lim and s_num == num:
                return {s_num:1}
            if not (num % prime):
                acc[prime] = acc.get(prime,0) + 1
                num //= prime
            elif acc:
                acc = dict_summ(acc, inner(num, pp + 1 ))
                update_cache(s_num, acc)
                return acc
            else:
                pp += 1
        update_cache(s_num, acc)
        return acc
    return inner
factor = factorize_rec()

if __name__ == '__main__':
    p = Primes()
    
    print(p[10000])
    print(Primes.get_set())
