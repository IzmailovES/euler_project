#!/usr/bin/env python3

import primes
import math
import time
import sys

def dict_summ(d1,d2):
    ret = d1.copy()
    for x,y in d2.items():
        ret[x] = d1.get(x,0) + y
    return ret

def factorize_rec(max_cachesize = 500**2):
    cache = dict()
  #  i = 0
    def update_cache(num, delimers):
        if num < max_cachesize:
            cache[num] = delimers
           # print(num,cache, sep = '\t')

    def inner(num, pp = 0):
        if not num:
            return dict()
        if num == 1:
            return dict()
        s_num = num
        # если число простое - возвращаем
        if num <= primes.Primes.known[-1] and num in primes.Primes.get_set():
            return {num:1}
        # если находим в кеше - возвращаем
        if num <= max_cachesize and num in cache:
            return cache[num]
        # пытаемся поделить на простые числа по  очереди до корня из себя:
        acc = dict()
        lim = int(math.sqrt(num)) + 1
        while num != 1:
            prime = primes.Primes()[pp]
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
f = factorize_rec()

            #  удалось поделить - делим на делитель сколько можем - возвращаем дикт сумм делителя + вызов себя от остатка c указанием следующего простого числа


def d(num):
    if num == 1:
        return 1
    ret = 1
    delimers = f(num)
    for x,y in delimers.items():
        ret *= ((x**(y+1) -1)//(x - 1))
    #print(num, ret, delimers)
    return ret

def multi_d(dct):
    # all items in dct is prime:power
    ret = 1
    for x,y in dct.items():
        try:
            ret *= (x**(y+1) -1)//(x - 1)
        except ZeroDivisionError:
            pass
    return ret

def multiple_delimers(d1,d2):
    #d1_new = dict(d1)
    #d2_new = dict(d2)
    d3 = dict()
    ks = d1.keys()
    for i in ks:
        if i in d2:
            d3[i] = d2[i] + d1[i]
    #return multi_d(d3) * multi_d({x:y for x,y in d1.items() if x not in d3}) * multi_d({x:y for x,y in d2.items() if x not in d3})
    return multi_d(d3) * multi_d({x:y for x,y in (d1|d2).items() if x not in d3})
    #return multi_d(d3) * multi_d( dict(filter(lambda x: x[0] not in d3, (d1|d2).items() ))) #  {x:y for x,y in (d1|d2).items() if x not in d3})


def s(n):
    cache = dict()
    def get_f(num):
        return cache.setdefault(num, f(num))
    ret = 0
    ret1 = 0  # on main diagonal
    ret2 = 0  # other
    ret3 = 0 # need to multiple by dd1
    for i in range(1,n+1):
        d1 = f(i)
        dd1 = multi_d(d1)
        ret1 += multi_d(dict_summ(d1,d1))
        ret3 = 0
        for j in range(1,i ):
            d2 = f(j)
            nod = primes.nod(i,j)
            if nod == 1:
                ret3 += multi_d(d2)#(dd1*multi_d(d2))
            else:
                #ret2 += multi_d(f(i//nod))*multi_d(f(j//nod))*multi_d(f(nod))
                ret2 += (multi_d(dict_summ(d1,d2))) #(0 if i == j else 1)
        ret2 += ret3*dd1
        #if not i%1000:
            #print(i,time.process_time(), ret1 + (ret2 << 1), ret1)
        #print(i,time.process_time(), ret1 + (ret2 << 1), ret1, ret2)
    #print(ret1,ret2)
    return ret1 + (ret2 << 1)

def s3(n):
    ret1 = 0
    ret2 = 0
    for i in range(1,n+1):
        d1 = f(i)
        dd1 = multi_d(d1)
        ret1 += multi_d(dict_summ(d1,d1))
        ret3 = 0
        for j in range(1,i):
            d2 = f(j)
            nod = primes.nod(i, j)
            if nod == 1:
                ret3 += multi_d(d2)
            else:
                ret2 += multiple_delimers(d1, d2)
        ret2 += ret3*dd1
    return ret1 + (ret2<<1)


def factor_exam(num,d):
    ret = 1
    for x,y in d.items():
        ret *= x**y
    if ret != num:
        return False
    return True

if __name__ == '__main__':
    num = int(sys.argv[1])
    prime_lim = int(math.sqrt(num)) + 1
    print(f'inventing primes until {prime_lim}')
    n = 0
    while primes.Primes()[n] < prime_lim:
        n+=1
    print('go calculte!', time.process_time())
    strt = time.process_time()
    print(s(num), time.process_time() - strt)
    strt = time.process_time()
    print(s3(num), time.process_time() - strt)
    exit(0)


