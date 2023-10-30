#!/usr/bin/env python3
import math

a = {0:1}

def is_ambudant(num):
    acc = 1
    for i in range(2,(num>>1) + 1):
        if not (num%i):
            acc += i 
    return acc > num


print('searching for ambudands:')
ams = set()
for i in range(12, 28123):
    if is_ambudant(i):
        ams.add(i)
print('search done')

def can(num, ams):
    for i in ams:
        if (num - i) in ams:
            return True
    return False

acc = 0
for i in range(28123):
    if not(can(i,ams)):
        acc += i
        print(i,acc)
print(acc)
exit(0)
