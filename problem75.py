#!/usr/bin/env python3

def get_troika(m,n,k):
    a = m**2 - n**2
    b = 2 * m * n 
    c = m**2 + n**2
    return a*k,b*k,c*k

n = 0 

thrsh = 1500000
#thrsh = 120                                                                                                                                                 
# l:set(tup)
lens = dict()

while True: # n 
    n += 1
    m = n 
    added_by_m = 0 
    while True: # m 
        m += 1
        k = 0 
        added_by_k = 0 
        while True: # k 
            k += 1
            a,b,c = tuple(sorted(get_troika(m,n,k)))
            l = a + b + c 
            if l <= thrsh:
                added_by_k += 1
                added_by_m += 1
                print(f"l: {l} =  {m}, {n}, {k}")
                if l in lens:
                    lens[l].add((a,b,c))
                else:
                    lens[l] = {(a,b,c)}
            else:
                break
        if not added_by_k:
            break
    if not added_by_m:
        break

print(lens)
ret = 0 
for l in lens:
    if len(lens[l]) == 1:
        ret += 1
print(ret)
