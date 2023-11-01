#!/usr/bin/env python3

import primes
d_noprime = {0,1,4,6,8,9}
def is_truncatable(num, s):
    ns = str(num)
    if ns[0] in d_noprime or ns[-1] in d_noprime:
        return False
    for i in range(len(ns)):
        if not(int(ns[:i+1]) in s):
            return False
        if not(int(ns[i:]) in s):
            return False
    return True

acc = 0
cnt = 0
p = 0
prme = primes.Primes()
while cnt < 11:
    p += 1
    pr = prme[p]
    if pr < 10:
        continue
    if is_truncatable(pr,prme.known_set):

        acc += pr
        cnt += 1
        print(f'\n -- {cnt}!!! {pr} !!! {acc}')
    else:
        print(p, pr, end = '\r')

print(acc)


