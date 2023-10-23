#!/usr/bin/env python3

def f(num):
    acc = 0
    for i in str(num):
        acc += int(i)**5
    return acc

acc = 0
for i in range(2,100000000):
    if i == f(i):
        acc += i
        print(i,acc)
