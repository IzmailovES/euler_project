#!/usr/bin/env python3

import sympy
import itertools
import functools
def test(s_num):
    # sirst part - probuct
    for p in [4]:
        pp = int(s_num[:p])
        others = s_num[p:]
        for i in [1,2]:
            if int(others[:i]) * int(others[i:]) == pp:
                #yield (pp, int(others[:i]), int(others[i:]))
                return pp
    return None


l = set()
s_num1 = '123456789'
nums = (int(''.join(x)) for x in itertools.permutations(s_num1))
for n in nums:
    k = test(str(n))
    if k:
        l.add(k)
print(l)
print(functools.reduce(lambda x,y: x+y , l),)
exit(0)



