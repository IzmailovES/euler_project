#!/usr/bin/env python3
def digsum(n):
    acc = 0
    for i in str(n):
        acc += int(i)
    return acc

m = 0
for i in range(100):
    for j in range(100):
        m = max(m, digsum(i**j))

print(m)


