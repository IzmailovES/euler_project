#!/usr/bin/env python3

import math

l = [ i for  i in range(1,10)]
l1 = l[:]
acc = 0
p = 1
while True:
    for x in l1:
        if len(str(x**p)) == p:
            acc += 1
        else:
            l.remove(x)
    if not l:
        print(acc)
        exit(0)
    l1 = l[:]
    p += 1

            
