#!/usr/bin/env python3

def is_palindrome(num):
    s = str(num)
    for i in range(len(s)//2):
        if s[i] != s[ -1 - i]:
            return False
    return True

def lish(num):
    n = 0
    while n < 50:
        n += 1
        num = num + int(str(num)[::-1])
        if is_palindrome(num):
            return False
    return True

print(lish(47))
cnt = 0
for i in range(1,10**4):
    if lish(i):
        cnt += 1
        print(i)
print()
print(cnt)
