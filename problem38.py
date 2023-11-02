#!/usr/bin/env python3

import sympy
import itertools
import functools
def test(n):
    i = 1
    acc = ''
    while True:
        prod = str(i*n)
        if len(acc) + len(prod) > 9:
            break
        acc = acc + prod
        i += 1
    if len(acc) == 9:
        return int(acc)
    return None

#print(test(9))
#exit(0)


l = list()
s_num1 = '123456789'
nums = {int(''.join(x)) for x in itertools.permutations(s_num1)}
for i in range(1, 10**5):
    k = test(i)
    if k and k in nums:
        l.append((i, k))
print(l)
print(max(l, key = lambda x: x[1]))
exit(0)



