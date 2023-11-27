#!/usr/bin/env python3

def get(m,x,y):
    l = len(m)
    if (x < 0 or x > l) or (y < 0 or y > l):
        raise IndexError('out of range')
    return m[x][y]

def neibs(m,x,y):
    ret = []
    for f in (m,x-1,y), (m,x,y-1):
        try:
            ret.append(get(*f))
        except:
            pass
    return ret

def calculate(raw_matrix):
    l = len(raw_matrix)
    for i in range(1,len(raw_matrix)):
        for j in range(i+1):
            raw_matrix[j][i-j] += min(neibs(raw_matrix,j,i-j))
    for i in range(1,len(raw_matrix)):
        for j in range(l-i):
            raw_matrix[i+j][l-j-1] += min(neibs(raw_matrix,i+j,l-j-1))



## get_raw_matrix
filename = '0081_matrix.txt'
with open(filename, 'r') as f:
    raw_matrix = [[int(x) for x in y.split(',')] for y in f.readlines()]
calculate(raw_matrix)
l = len(raw_matrix)

print(raw_matrix[l-1][l-1])


    
