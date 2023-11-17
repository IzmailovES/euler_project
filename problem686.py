#!/usr/bin/env python3

def reduce(num, digs=None):
    if digs is None:
        return num
    while num > (10**digs)-1:
        num //=10
    return num

def f(n):
    li = 0
    dct = dict()
    i = 90
    ndigs = 3
    rd = ndigs **2*2 
    ai = reduce(2**i, rd)
    k = 1
    a = []
    for j in 196,289,485:
        a.append((reduce(2**j, rd),j))

    while k < n:
        for d,dd in a:
            if reduce(ai*d, ndigs) == 123:
                i += dd
                dct[dd] = dct.get(dd,0) + 1
                ai = reduce(ai*d,rd)
                k += 1
                print(i,dd,k,n)
                break
            #else:
            #    print('no', dd)
        else:
                print('!!!!', i,k,d,dd)
                exit(2)
    return i, dct

print(f(45))
print(f(678910))

    

