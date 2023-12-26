#!/usr/bin/env python3

import math

def mutate(num, rnum):
    return num + rnum

def verify(num, rnum):
    num = num + rnum
    s_num = num
    while num:
        if not num&1:
            return 0
        num //= 10
    #print(s_num)
    return 1


ret = 0
i = 12
n = 10**9
while i < n:
    ri = int(str(i)[::-1])
    if not ri&1:
        i += 10**int(math.log(i,10))
        #i += 2
        continue
    k = verify(i, ri)
    if k:
        ret += 1
        print(ret,i)
    if i%10 == 8:
        i += 4
    else:
        i += 2
print(ret << 1)
