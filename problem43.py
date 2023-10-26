#!/usr/bin/env python3

import itertools
d = [2,3,5,7,11,13,17]
dl = len(d)
def validate(num):
    for i in range(dl):
        #print((num[1+i:4+i]%d[i])
        if (int(num[1+i:4+i])%d[i]):
            return False
    return True

print(validate('1406357289'))
#exit(0)
a = '0123456789'
acc = 0
for i in itertools.permutations(a,len(a)):
    n = ''.join(i)
    if validate(n):
        acc += int(n)
        print(n, acc)


print(acc)
