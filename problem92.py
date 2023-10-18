#!/usr/bin/env python3

def process(num):
    acc = 0
    while num:
        acc += (num%10)**2
        num //=10
    return acc

def calculate(num):
    while num != 1 and num != 89:
        num = process(num)
    return num

calculate(44)
calculate(85)
ret = 0
for i in range(1,10**7):
    if calculate(i) == 89:
        ret += 1
print(ret)
