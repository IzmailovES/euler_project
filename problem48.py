#!/usr/bin/env python3

import time

n = 1000
t = time.process_time()
acc = 0
for i in range(1, n+1):
    acc += pow(i,i,10**18)

print(acc%(10**10), time.process_time() - t)
