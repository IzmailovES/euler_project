#!/usr/bin/env python3

import primes
import math
import time
import sys
import functools
import sympy

def dict_summ(d1,d2, ret = dict()):
  #  for x in ret:
  #      del x
  #  for x in d1:
  #      ret[x] = d1[x]
  #  for x in d2:
  #      ret[x] = ret.get(x,0) + d2[x]
  #  return ret
  #  for x in d2:
  #      d1[x] = d1.get(x,0) + d2[x]
  #  return d1
    ret = {**d1, **d2}
    for x in d1:
        if x in d2:
            ret[x] += d1[x]
    return ret

def factor_exam(num,d):
    ret = 1
    for x,y in d.items():
        ret *= x**y
    if ret != num:
        return False
    return True

def factorize_rec(max_cachesize = 500**2):
    cache = dict()
    def update_cache(num, delimers):
        if num < max_cachesize:
            cache[num] = delimers
    time_summ = 0
    def inner(num, pp = 0):
        if num == 1 or not num:
            return dict()
        s_num = num
        # если число простое - возвращаем
        if sympy.ntheory.isprime(num): #num <= primes.Primes.known[-1] and num in primes.Primes.get_set():
            return {num:1}
        # если находим в кеше - возвращаем
        if num <= max_cachesize and num in cache:
            return dict(cache[num])
        # пытаемся поделить на простые числа по  очереди до корня из себя:
        acc = dict()
        lim = int(math.sqrt(num)) + 1
        while num != 1:
            prime = sympy.nextprime(pp)
            if prime > lim and s_num == num:
                return {s_num:1}
            if not (num % prime):
                acc[prime] = acc.get(prime,0) + 1
                num //= prime
            elif acc:
                acc = dict_summ(acc, inner(num, prime ))
                update_cache(s_num, acc)
                return acc
            else:
                pp  = sympy.nextprime(pp)
        update_cache(s_num, acc)
        return acc
    return inner
f = factorize_rec()
print(f(1000))
def f_sy():
    fsycache = dict()
    def update_cache(num,ret):
        #if len(ret) == 1:
        #    return
        fsycache[num] = ret

    def get_fromcache(num):
        ret = fsycache[num]
        return ret

    def inner(num):
        if num in fsycache:
            ret = get_fromcache(num)
            return ret
        else:
            ret = sympy.factorint(num)
            update_cache(num,ret)
            return ret
    return inner
f = f_sy()

print(f(3))
print(f(27))
print(f(9))
print(f(3))
            #  удалось поделить - делим на делитель сколько можем - возвращаем дикт сумм делителя + вызов себя от остатка c указанием следующего простого числа


def d(num):
    ret = 1
    delimers = f(num)
    for x,y in delimers.items():
        ret *= ((x**(y+1) -1)//(x - 1))
    return ret

def prime_d(x,y):
    return (x+1) if y == 1 else (( x**(y+1) -1) // (x-1))


def multi_d(dct, dct2 = dict()):
    # all items in dct are prime:power
    ret = 1
    for x,y in dct.items():
        ret *= prime_d(x,y) #)((x+1) if y == 1 else ((x**(y+1) -1)//(x - 1)))
    for x,y in dct2.items():
        if x in dct:
            ret *= prime_d(x,y+dct[x])
            ret //= prime_d(x,dct[x])
        else:
            ret *= prime_d(x,y)
    return ret

def multiple_delimers(d1,d2, pr = False):
    d3 = dict()
    ks = d1.keys()
    for i in ks:
        if i in d2:
            d3[i] = d2[i] + d1[i]
    return multi_d(d3) * multi_d({x:y for x,y in (d1|d2).items() if x not in d3})

def balance_d(d1,d2):
    ret1 = dict(d1)
    ret2 = dict()
    for x,y in d2.items():
        if x in d1:
            ret2[x] = d1[x] + y
            del ret1[x]
        else:
            ret2[x] = y
    return multi_d(ret1) * multi_d(ret2)
    #return ret1, ret2

def balance_d_(d1,d2):
    ret1 = dict(d1)
    it = d2.items()
    for x,y in it:
        if x in d1:
            d2[x] += d1[x]
            del ret1[x]
   # print(d2)
   # print(multi_d(d2))
    return multi_d(ret1) * multi_d(d2)

def balance_i(i,j):
    print(i,j)
    while True:
        nod = math.gcd(i,j)
        print(nod)
        if nod == 1:
            break
        i //= nod
        j *= nod
    return i,j


def mnozitel(d1,d2):
    ret = dict()
    for x in list(d2):
        if x in d1:
            ret[x] = d2.pop(x)
    # teper formiruem coefficient
    k = 1
    for x,y in ret.items():
        try:
            k *= (x**(y+1+d1[x]) - x**(d1[x]+1))//(x-1)
        except ZeroDivisionError:
            pass
    return k

def s_generator(n):
    ret = 0
    ret1 = 0  # on main diagonal
    ret2 = 0  # other
    ret3 = 0 # need to multiple by dd1
    for i in range(1,n+1):
        d1 = f(i)
        dd1 = multi_d(d1)
        ret1 += multi_d( {x:(y <<1) for x,y in d1.items()}) #(dict_summ(d1,d1))
        ret2 += sum( ( ((multi_d(f(j)) * dd1) if (math.gcd(i,j)==1) else (multi_d(dict_summ(d1, f(j))))) for j in range(1, i) ))
        #ret2 += sum( (multi_d(dict_summ(d1, f(j))) for j in range(1, i) ))
    return ret1 + (ret2 << 1)


def s(n):
    cache = dict()
    def get_f(num):
        return cache.setdefault(num, f(num))
    ret = 0
    ret1 = 1  # on main diagonal
    ret2 = 0  # other
    ret3 = 0 # need to multiple by dd1
    retP = 1
    for i in range(2,n+1):
        d1 = f(i)
        dd1 = multi_d(d1)
        ret1 += multi_d({x:y*2 for x,y in d1.items()})  ###dict_summ(d1,d1))
        ret3 = retP
        if not sympy.ntheory.isprime(i):
            ###
            dk = sorted(d1.keys())
            #print(dk,d1, i)
            ## first iterate:
            for j in range(dk[0], i, dk[0]):
                d2 = f(j)
                ret2 += multi_d(d1,d2) ###{x:(d1.get(x,0)+d2.get(x,0)) for x in (*d1,*d2)}) #dict_summ(d1,d2)))
                ret3 -= multi_d(d2)
            for k,div in enumerate(dk[1:]):  ## for all prime divisirs exclude 0
                srez = dk[:k+1]
                for e,x in enumerate(range(div,i,div)):  ## x iterate by step - divisor
                    for s in srez: ## check if already do this number
                        if not (e+1)%s:
                            break
                    else:
                        d2 = f(e+1).copy() #f(x)
                        #assert factor_exam(e+1, f(e+1)), (e,d2)
                        #assert factor_exam(e+1,d2), (e+1,d2)
                        
                        #print(d2, e+1)
                        d2[div] = d2.get(div,0) + 1
                        ret2 += multi_d(d1,d2) #  dict_summ(d1,d2))
                        ret3 -= multi_d(d2)
                        #if ret3 <0:
                        #    print(retP, ret3)
                        #    exit()

            ###
            #for j in range(1,i ) :
            #    if (math.gcd(i,j) != 1):
            #        d2 = f(j)
            #        ret2 += (multi_d(dict_summ(d1,d2)))
            #        ret3 -= multi_d(d2)
        ret2 += ret3*dd1
        retP += dd1
        #print(i)
    return ret1 + (ret2 << 1)



for i in range(1,1001):
    assert factor_exam(i, f(i)) , i
for i in range(1,1001):
    assert factor_exam(i, f(i)) , i

if __name__ == '__main__':
    num = int(sys.argv[1])
    prime_lim = int(math.sqrt(num)+1000) + 1
    print(f'inventing primes until {prime_lim}')
    n = 0
    while primes.Primes()[n] < prime_lim:
        n+=1
    print('go calculte!', time.process_time())
    #for i in range(num):
    #    print(i, f(i))
    strt = time.process_time()
    #print(s_generator(num), time.process_time() - strt)
    strt = time.process_time()
    print(s(num), time.process_time() - strt)
    exit(0)


