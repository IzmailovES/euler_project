#!/usr/bin/env python3

n = 2**1000
summ = 0
while n:
    summ += n%10
    n = n//10
print(summ)