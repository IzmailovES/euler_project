#!/usr/bin/env python3

def rect_fit(dims, grid):
    if dims[0] > grid[0] or dims[1] > grid[1]:
        return 0
    return (grid[0] - dims[0] +1)* (grid[1] - dims[1] +1)


def rects_summ(grid):
    acc = 0
    for i in range(1,grid[0]+1):
        for j in range(1,grid[1]+1):
            acc += rect_fit((i,j),grid)
    return acc

area = 1,1
target = 2*10**6
da = target

for i in range(1,100):
    for j in range(1,100):
        diff = abs(rects_summ((i,j)) - target)
        if diff < da:
            area = i,j
            da = diff
            #pirint(area,da)
print(area, area[1]*area[0])
