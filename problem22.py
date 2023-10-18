#!/usr/bin/env python3

def name_to_num(name):
    acc = 0
    for l in name:
        acc += ord(l) - 64
    return acc

print(name_to_num('COLIN'))

with open('names.txt', 'r') as f:
    names = f.read()
names = sorted([ x.strip('"') for x in names.split(',')])

total = 0
for i,n in enumerate(names):
    total += name_to_num(n)*(i+1)

print(total)