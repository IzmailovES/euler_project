#!/usr/bin/env python3

import sympy
import math
n = 800800**800800
#n = 800**800
#n = 800
def gp(p1,p2):
    return p1**p2*p2**p1

def test(pp, lim, n):
    mi = sympy.prevprime(n)
    ma = sympy.nextprime(n)
    dm = ma-mi
    f = pp**mi
    mif = f*mi**pp < lim
    maf = f * pp**dm * ma**pp < lim
    if mif and maf:
        return 'less'
    if not (mif or maf):
        return 'more'
    return 'here'

def test1(x,y,n):
    return gp(x,y) <= n

def fs_log(fp,n):
    logn = math.log(n,fp)
    high = int(logn)
    low = 0
    d = low
    while(high - low) > 1:
        p = (high+low)>>1
        k = p + fp*math.log(p,fp) - logn
        if k > 0:
            high = p
            f = 1
        elif k < 0:
            low = p
            f = 0
        else:
            print('break exit')
            break
    if f :
        p -= 1
    ret = sympy.prevprime(p) if not sympy.ntheory.isprime(p) else p
    return ret
## найти p, при котором q - предыдуюее - ассиметричные пары
# из последовательнсти p и меньше все пары будут меньше большого числа
# ищем ассиметричные пары:
k = sympy.nextprime(1)
acc = dict()
f = 3
while k <= f:
    f = fs_log(k,n)
    if k != f:
        acc[f] = k
    k = sympy.nextprime(k)
acc[f] = 0
lacc = sorted([x for x in acc.items()], reverse = True)
ret = 0
for i in range(len(lacc)-1):
    ret += (sympy.primepi(lacc[i][0]) - sympy.primepi(lacc[i+1][0]))*sympy.primepi(lacc[i][1])
z = sympy.primepi(f)
b = math.factorial(z)//(math.factorial(z-2)*2)
print(ret + b)
exit(0)
