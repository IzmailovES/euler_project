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
tail = 9**2 - sum(range(9))
def S(num):
    ret = 0
    k = num//9
    ost = num%9
    for i in range(k):
        #add =  (9*(ost + 9*(k-i-1) + 5)) * 10**i
        add =  (num - 9*i -4 ) * 10**i
        ret += add
      #  print(add)
    ret *=9
    print('>>',num, k, ost, sum(range(ost+1)), ret, end = ' ')
    return ret + sum(range(ost+1))*10**(k)

def S1(num, mod = None):
    k = num//9
    o = num%9
    ret =  pow((o + 6 + sum(range(o+1)))*  pow(10,k, mod), 1, mod) - pow((num+6), 1, mod)
    if ret < 0:
        ret += mod
    return ret

def d_sum(num):
    ret = 0
    while num:
        ret += num%10
        num //=10
    return ret
#for i in range(100):
#    r = S(i)
#    print( r, len(str(r)))
#print()
#exit()
#print(S(13), S(21), S(34))
#print(S(34) - S(33))
j = 1
acc = 0
print(len(fib(90,0,1)))
for i in fib(90,0,1)[1:]:
    j += 1
    f = S1(i,10**9+7)
    acc += f
    print(j, i, "\n", f)
print(acc%(10**9+7))
print(S1(20))
