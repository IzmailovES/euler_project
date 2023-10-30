#!/usr/bin/env python3

import itertools

st = '0123456789'
ne = itertools.permutations(st)
for _ in range(10**6):
    print(_, ''.join(next(ne)))
