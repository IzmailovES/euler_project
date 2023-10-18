#!/usr/bin/env python3


def collatz_outer():
    cache = dict()

    def inner(num):
        if num in cache:
            return cache[num]
        counter = 0
        s_num = num
        while num != 1:
            if num in cache:
                counter += cache[num]
                break
            if num & 1:
                num = num * 3 + 1
            else:
                num >>= 1
            counter += 1

        cache[s_num] = counter
        counter += 1
        return counter
    return inner

collatz = collatz_outer()
m = 0
n = 1
for i in range(1,10**6):
    c = collatz(i)
    #print(i,c)
    if c > m:
        m = c
        n = i
        print(n,c)
print(n,m)