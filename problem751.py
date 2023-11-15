#!/usr/bin/env python3


def fib(n,start):
    b = [start]
    k = 1
    for i in range(1,n):
        b.append(int(b[-1])*(b[-1] - int(b[-1]) + 1))
    return [int(x) for x in b]

o = 2.223561019313554106173177
print(len(str(o)), str(o))

print(fib(24,o))

