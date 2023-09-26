#!/usr/bin/env python3

import math
def get_pentagonal_number(n):
    return (3*n*n -n) >> 1


def is_pentagonal_number(num):
    num <<= 1
    for n in range(1,int((math.sqrt(num)))):
        if (3*n*n -n) == num:
            return True
    return False


def get_pentagonal_numbers(n1):
    for i in range(1,n1 + 1):
        yield get_pentagonal_number(i)

def find_diff_p(num):
    lp = []
    diff = 0
    lp.append(get_pentagonal_number(1))
    lp.append(get_pentagonal_number(2))
    diff = lp[1] - lp[2]
    current = 1
    while True:
        pass

def is_our_pair(n1, n2, c):
    #if is_pentagonal_number(n2-n1) and is_pentagonal_number(n2+n1):
    if (n2-n1) in c and (n2+n1) in c:
        return n2-n1

#l = [get_pentagonal_number(1), get_pentagonal_number(2)]

l = list(get_pentagonal_numbers(1000000))
s = set(l)
for k,i in enumerate(l[1:]):
    print(f'\r {k}:  {i}', end = ' ')
    for j in l[0:k]: # ( x for x in l if x < i):
        if is_our_pair(j,i, s):
            print(i,j)

print(is_pentagonal_number(22))





print(list(get_pentagonal_numbers(10)))
