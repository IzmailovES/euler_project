#!/usr/bin/env python3

import sympy

def is_permutation(a,b):
    return sorted(str(a)) == sorted(str(b))

lp = list(sympy.primerange(1000,10000))
#print(lp)
gr = dict()
#print(type(gr.get(10,list()).append(10)))
for i in lp:
    for j in range(len(lp)):
        if is_permutation(lp[j], i):
            gr[i] = gr.get(i, list()) + [lp[j]]
gr = (set(map(lambda x: frozenset(x[1]), gr.items())))
gr = list(filter(lambda x: len(x) > 2, gr))
gr = [ sorted(x) for x in gr]
print(gr)
for pp in gr:
    for i in range(len(pp)-2):
        for j in range(i+2, len(pp)):
            if (pp[i] + pp[j])>>1 in pp:
                print(pp[i], (pp[i]+pp[j])>>1,  pp[j], sep = '')


