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
f = factorize()

def dict_summ(d1,d2):
    ret = d1.copy()
    for x,y in d2.items():
        ret[x] = d1.get(x,0) + y
    return ret

def factorize_rec(max_cachesize = 50**2):
    cache = dict()
    def update_cache(num, delimers):
        if num < max_cachesize:
            cache[num] = delimers
           # print(num,cache, sep = '\t')

    def inner(num, pp = 0):
        if not num:
            return dict()
        if num == 1:
            return {1:1}
        s_num = num
        # если число простое - возвращаем
        if num in primes.Primes.get_set():
            return {num:1}
      #  else:
       #     print(f'known set miss: {num} {primes.Primes.get_set()}')

        # если находим в кеше - возвращаем
        if num in cache:
            return cache[num]
        # пытаемся поделить на простые числа по  очереди до корня из себя:
        acc = dict()
        lim = int(math.sqrt(num)) + 1
        while num != 1:
            #print(num, acc)
            prime = primes.Primes()[pp]
            if prime > lim and s_num == num:
                #update_cache(s_num,{s_num:1})
                return {s_num:1}
            if not (num % prime):
                acc[prime] = acc.get(prime,0) + 1
                num //= prime
            elif acc:
                #print('call recursion', end = '')
                acc = dict_summ(acc, inner(num, pp + 1 ))
                update_cache(s_num, acc)
                #print()
                return acc
            else:
               # print(f'\r fail to divide by {prime}', end =  ' ')
                pp += 1
        update_cache(s_num, acc)
        return acc
    return inner
f = factorize_rec()

            #  удалось поделить - делим на делитель сколько можем - возвращаем дикт сумм делителя + вызов себя от остатка c указанием следующего простого числа


def d_old(num): ## sum of all divisors
    ret = 0
    for i in range(1,(num+1)>>1):
        if not ( num%i):
            ret += i
    return ret

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
            ret *= 1
    return ret


def s(n):
    cache = dict()
    ret = 0
    for i in range(1,n+1):
        d1 = f(i)
        ret += multi_d(dict_summ(f(i),f(i)))
    for i in range(1, n):
        for j in range(i+1, n+1):
            d1 = dict_summ(f(i), f(j))
            ret += multi_d(d1) << 1
    return ret
#
#        for j in range(1, n+1):
#            ret += multi_d(dict_summ(f(i),f(j)))
#            ret%=10**3
            #print(ret)
#    return ret

def factor_exam(num,d):
    ret = 1
    for x,y in d.items():
        ret *= x**y
    if ret != num:
        return False
    return True
#print(primes.Primes()[100])
#print(primes.Primes.get_set())
#n = 1
#while factor_exam(n,f(n)):
#    n+= 1
#    print(n, f(n))
#exit(0)
prime_lim = 10**3
print(f'inventing primes until {prime_lim}')
n = 0
while primes.Primes()[n] < prime_lim:
    n+=1
print('go calculte!')

print(s(2000))
exit(0)

#print (dict_summ({1:2, 3:4}, {0:5, 1:3, 7:8}))
#exit(0)
for i in range(3,10**6):
    #print(f'{i:,}, {f(i)}')
    f(i)
exit(0)
for i in range(10**11 -10000, 10**11):
    a = f(i)
    print(f'{i:,}: {a}')
    acc = 1
    for x,y in a.items():
        acc *= x**y
    if acc != i:
        raise Exception()



print('done')
print(primes.Primes()[0])
#print(s(200))

