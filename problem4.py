#!/usr/bin/python3

def is_palindrome(num):
    sn = str(num)
    h = len(sn)>>1
    for i in range(h):
        if sn[i] != sn[len(sn) - i - 1]:
            return False
    return True

a = 100
b = 1000
m = 0
for i in range(a,b):
    for j in range(a,b):
        k = i*j
        if is_palindrome(k):
            if k > m:
                m = k
print(m)
