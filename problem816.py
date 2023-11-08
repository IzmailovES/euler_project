#!/usr/bin/env python3

import math
def get_next(num):
    return pow(num,2,50515093)

def generate(num):
    ret = []
    start = 290797
    while num:
        d = get_next(start)
        ret.append((start, d))
        start = get_next(d)
        num -= 1
    return ret

def distance(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

p_count = 2*10**6
points = sorted(generate(p_count))
print("generated")

m = 999999999999999999
for i in range(p_count -1):
    m = min(m, distance(points[i], points[i+1]))
print(m)



