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

print(get_splits('1234'))

print([1,2,3][1:2])

