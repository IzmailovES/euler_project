#!/usr/bin/env python3
m = 5
def is_permut(n1,n2):
    s1 = sorted(str(n1))
    s2 = sorted(str(n2))
    return s1 == s2

def hs(num):
    return ''.join(sorted(str(num)))

cubs = dict()
i = 1
while True:
    try:
        num = hs(i**3)
        vl = cubs.get(num,[])
        if len(vl) == m-1:
            print(vl[0])
            exit()
        vl.append(i**3)
        cubs[num] = vl
        i += 1
    except TypeError:
        print(cubs)
        exit(1)

