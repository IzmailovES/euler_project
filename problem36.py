#!/usr/bin/env python3

def is_palingrome(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True
acc = 0
for i in range(10**6):
    if is_palingrome(str(i)) and is_palingrome(bin(i)[2:]):
        acc += i
print(acc)
