#!/usr/bin/env python3

import sympy

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
    #mif = gp(pp,mi) < lim
    #maf = gp(pp,ma) < lim
    if mif and maf:
        return 'less'
    if not (mif or maf):
        return 'more'
    return 'here'


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




