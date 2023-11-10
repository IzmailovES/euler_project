#!/usr/bin/env python3
import math
def get_splits(s):
    ls = len(s)
    if ls == 1:
        return [[s]]
    if ls == 2:
        return [[s], [s[0], s[1]]]
    ret = []
    for i in range(1,ls):
        ret +=  [[s[:i]] + x for x in get_splits(s[i: (len(s))])] + [[s[:i], s[i:]]]
    return ret

def get_split_pattern(c):
    #s = ''
    #for i in range(c):
    #    s += str(1)
    #s = ''.join(['1' for _ in range(c)])
    s = '1'*c
    ret =  list(filter( lambda x: (math.ceil(c/2) - 1) <= max([len(y) for y in x] ) <= math.ceil(c/2) ,get_splits(s)))
    #return ([ [len(y) for y in x] for x in ret ] + [ [c//2,  c-c//2], [c-c//2, c//2]]) if c > 3 else 
    return ([ [len(y) for y in x] for x in ret ] )

def is_s_num(num,num2, patterns):
    s_num = str(num2)
    for l in patterns[len(s_num)]:
        acc = 0
        p = 0
        for pt in l:
            ss = s_num[p:p+pt]
            try:
                acc += int(ss)
            except ValueError:
                print(l,num)
                exit(1)
            p += pt
        else:
            if acc == num:
                print(num, num2, 'pattern:', l, len(l))
                return num2
    return 0


n = 10**6
d_patterns = dict()
for i in range(1,len(str(n**2))+ 1):
    d_patterns[i] = get_split_pattern(i)

for d in d_patterns:
    print(d, d_patterns[d])

acc = 0
i = 2
while i <= n:
    ii = i**2
    acc += is_s_num(i,ii,d_patterns)
    i += 1

print(acc)

