#!/usr/bin/env python3

import primes
import itertools

def go_right(s):
    return (s[-1] + s[:-1])

def check(num):
    s = go_right(str(num))
    while int(s) != num:
        if not int(s) in primes.Primes.known_set:
            return False
        s = go_right(s)
    return True

p = primes.Primes()
n = 10**6
d = 0
for i in range(10000):
    d = p[i]
exit(0)

print(f'search primes below {n}')
i = 0
while True:
    if p[i] > n:
        break
    #print(p[i])
    i+=1

print('go calculate!')
i = 0
cnt = 0
while p[i] < n:
    if check(p[i]):
        cnt += 1
    i += 1
print(cnt)
