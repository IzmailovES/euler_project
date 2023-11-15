#!/usr/bin/env python3

def fib(n, f1,f2):
    ret = [f1,f2]
    n -= 2
    while n > 0:
        ret.append(ret[-1] + ret[-2])
        n -=1
    return ret
def s(num):
    nines = num//9
    first = num%9
    return int(str(first)+'9'*nines)
def Ss(num):
    acc = 0
    for n in range(1,num+1):
        acc+=s(n)
    return acc

def S(num):
    ret = 0
    k = num//9
    ost = num%9
    for i in range(k):
        add =  (num - 9*i -4 ) * 10**i
        ret += add
    ret *=9
    return ret + sum(range(ost+1))*10**(k)

def S1(num, mod = None):
    k = num//9
    o = num%9
    ret =  pow((o + 6 + sum(range(o+1)))*  pow(10,k, mod) - (num+6), 1, mod)
    return ret

def d_sum(num):
    ret = 0
    while num:
        ret += num%10
        num //=10
    return ret
j = 1
acc = 0
for i in fib(91,0,1)[2:]:
    j += 1
    f = S1(i,10**9+7)
    acc += f
    print(j, i,  f, acc)
print(acc%(10**9+7))
