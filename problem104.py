#!/usr/bin/env python3
import math

s = {str(x) for x in range(1,10)}
miliard = 10**9

def is_pang_tail(num):
    return set(str(num%miliard)) == s

def is_pang_head(num):
    numlen = int(math.log(num,10)) + 1
    num //= 10**(numlen-9)
    st = set(str(num))
    return st == s

print(is_pang_tail(11234567891))
print(is_pang_head(10234567891))
print(is_pang_head(123456789100000000000000))
a = 1
b = 2
step = 3
while True:
    c = a + b
    a = b
    b = c
    step += 1
    #print(step)
    if is_pang_tail(c) and is_pang_head(c):
    #if False :#is_pang_head(c) and is_pang_tail(c):
        print('step found: ', step)
        break
