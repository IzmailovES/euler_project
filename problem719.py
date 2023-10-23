#!/usr/bin/env python3

def get_splits(s):
    if len(s) == 1:
        return [[s]]
    if len(s) == 2:
        return [[s], [s[0], s[1]]]
    ret = []
    for i in range(1,len(s)):
        ret +=  [[s[:i]] + x for x in get_splits(s[i: (len(s))])]
    return ret

def get_split_pattern(c):
    s = ''
    for i in range(c):
        s += str(1)
    return get_splits(s)

def is_s_num(num, patterns):
    s_num = str(num**2)
    for l in patterns[len(s_num)]:
        acc = 0
        p = 0
        for pt in l:
            acc += int(s_num[p:p+len(pt)])
            p += len(pt)
        if acc == num:
            return True
    return False


d_patterns = dict()
for i in range(1,13):
    d_patterns[i] = get_split_pattern(i)

print(is_s_num(99, d_patterns))

#for i in range(2,1000):
#    if is_s_num(i):
#        print(i, i**2)

n = 10**2 + 1
acc = 0
i = 2
while i < n:
    if not i&1000:
        print(i, acc)
    if is_s_num(i,d_patterns):
        acc += i**2
    i += 1


print(acc)

