#!/usr/bin/env python3

import sympy

def get_layer(n):
    return list(range((2*(n-1)-1)**2+1, (2*n-1)**2+1))

def prime_procent(ld):
    return len([x for x in ld if sympy.ntheory.isprime(x)])/len(ld)

def diagonal(nums):
    l = len(nums)//4
    return(nums[l-1], nums[l*2]-1, nums[l*3-1], nums[l*4-1])

nums = 1
p_nums = 0
k = 1
i = 2
while k > .1:
    nums += 4
    p_nums += len([ x for x in diagonal(get_layer(i)) if sympy.ntheory.isprime(x) ])
    k = p_nums/nums
    i += 1
print((i-1)*2-1)
