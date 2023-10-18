#!/usr/bin/env python3

acc = set()
for i in range(2,101):
    for j in range(2,101):
        acc.add(i**j)

print(len(acc))