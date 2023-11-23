#!/usr/bin/env python3

import sympy
import math
#n = 800800**800800
n = 800**800
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
    #mif = gp(pp,mi) < lim
    #maf = gp(pp,ma) < lim
    if mif and maf:
        return 'less'
    if not (mif or maf):
        return 'more'
    return 'here'

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
        elif k < 0:
            low = p
        else:
            print('break exit')
            break
        #print(high,low,p)
    return sympy.prevprime(p+1)
## найти p, при котором q - предыдуюее - ассиметричные пары
# из последовательнсти p и меньше все пары будут меньше большого числа
# ищем ассиметричные пары:
k = sympy.nextprime(1)
acc = dict()
f = 3
while k < f:
    f = fs_log(k,n)
    print(k,f)
    if k != f:
        acc[f] = k
    k = sympy.nextprime(k)
print(f)
print(acc)
lacc = sorted([x for x in acc.items()], reverse = True)
print(lacc)
ret = 0
for i in range(len(lacc)-1):
    ret += (sympy.primepi(lacc[i][0]) - sympy.primepi(lacc[i+1][0]))*sympy.primepi(lacc[i][1])
print(ret)
z = sympy.primepi(f)
print(z)
b = math.factorial(z)//(math.factorial(z-2)*2)
print(b)
print(ret + b)
exit(0)
k = sympy.nextprime(1)
np = nodeprimes[0]
ii = 1
while True:
    if k > np:
        break
    if k in acc:
        countprimes.append((k,ii))
        print(k,ii)
    k = sympy.nextprime(k)
    ii += 1
ret = 0
for i in range(len(countprimes)-1):
    ret += (countprimes[-1 - i][1] - countprimes[-2 - i][1]) * acc[countprimes[-1 -i][0]][1]
print(ret)
ret += math.factorial(85)//(math.factorial(85-2) * 2)
print(ret)
print('done')

exit(0)



def find_secondprime(n):
    ## search for st2 minimum
    st2 = 0
    k = n
    mil2 = (2<<1000000)-1
    th2 = (2<<1000)-1
    while True:
        if not k&mil2:
            k>>=1000000
            st2 += 1000000
        elif not k&th2:
            k >>=1000
            st2+=1000
        elif not k&((2<<10) -1):
            k >>= 10
            st2+=10
        elif not k&1:
            k >>= 1
            st2 += 1
        else:
            break
    print('first st2 = ', st2)
    st2 = sympy.nextprime(st2)
    minst2 = st2
    maxst2 = st2
    while gp(2,maxst2) < n:
        maxst2 <<= 1
    minst2 = maxst2 >> 1
    print('maxst2 = ',maxst2, 'minst2 = ', minst2)
    while True:
        p = (maxst2 + minst2)>>1
        t = test(2,n, p)
        if t == 'less':
            minst2  = p
        elif t == 'more':
            maxst2 = p
        else:
            print(p)
            break
    if not sympy.ntheory.isprime(p):
        st2 = sympy.prevprime(p)
    else:
        st2 = p
    return st2

def fs(low,high,pp, n):
    while True:
        p = (low+high)>>1
        t = test(pp ,n,p)
        if t == 'less':
            low = p
        elif t == 'more':
            high = p
        else:
            break
        print(p)
    if not sympy.ntheory.isprime(p):
        st2 = sympy.prevprime(p)
    else:
        st2 = p
    return st2
fp = sympy.nextprime(1)
sp = find_secondprime(n)
acc= [(2,sp)]
while True:
    fp = sympy.nextprime(fp)
    sp = (fs(sp>>1,sp, fp , n))
    acc.append((fp,sp))
    print(acc)
exit()

sp = find_secondprime(n)
fp = 2
print(sp,fp)
acc = 0
addacc = 1
while sp > fp:
    print(sp,fp, acc, addacc)
    if gp(fp,sp) <= n:
        acc += addacc
        sp = sympy.prevprime(sp)
        fp = sympy.nextprime(fp)
        addacc += 1
    else:
        acc += (addacc -1)
        sp = sympy.prevprime(sp)
print(acc)
exit()

firstprime = 2
secondprime = 15704473

#print(gp(firstprime, secondprime) < n) 
#print(gp(3, sympy.prevprime(secondprime)) < n)

while secondprime != 2:
    print(secondprime)
    secondprime = sympy.prevprime(secondprime)




