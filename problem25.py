#!/usr/bin/env python3


n = 2
a = 1
b = 1
while True:
    n += 1
    a,b = b, b+a
    if len(str(b)) == 1000:
        break

print(n, b, len(str(b)))
