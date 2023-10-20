#!/usr/bin/env python3

def check(num):
    s_num = str(num)
    l= len(s_num)
    for i in range(2,7):
        ss = str(num*i)
        if len(ss) != l:
            return False
        for x in s_num:
            if not x in ss:
                return False
        for x in ss:
            if not x in s_num:
                return False
    return True

print(check(125874))

n = 1
while True:
    if check(n):
        break
    n += 1
print(n)
