#!/usr/bin/env python3

import sympy
import itertools

def test(s_num):
    # sirst part - probuct
    for p in [4]:
        pp = int(s_num[:p])
        others = s_num[p:]
        for i in [1,2]:
            if int(others[:i]) * int(others[i:]) == pp:
                yield frozenset((pp, int(others[:i]), int(others[i:])))


l = []
s_num1 = '123456789'
nums = (int(''.join(x)) for x in itertools.permutations(s_num1))
for n in nums:
    l.append(list(test(str(n))))
print(l)
exit(0)



