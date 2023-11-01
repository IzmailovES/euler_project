#!/usr/bin/env python3

from math import gcd
def is_curious(n,m):
    if not n%10 or not m%10:
        return False
    sn = str(n)
    sm = str(m)
    com = []
    for i in sn:
        if i in sm:
            com.append(i)
    if not com:
        return False

    for i in com:
        if int((sn.replace(i,'')) or i)/int((sm.replace(i,'') or i)) == n/m:
            return True
    return False

print(is_curious(49,97))
acc = []
for m in range(11,100):
    for n in range(11,m):
        if is_curious(n,m):
            acc.append((n,m))

print(acc)
acc1 = [1,1]
for i in acc:
    acc1[0] *= i[0]
    acc1[1] *= i[1]
print(acc1)
g = gcd(*acc1)
while g != 1:
    acc1[0] //= g
    acc1[1] //= g
    g = gcd(*acc1)
print(acc1)
