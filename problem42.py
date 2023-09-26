#!/usr/bin/env python3

import math

def is_triangle_num(num):
    num = num<<1
    a = int(math.sqrt(num))
    if num == a*(a+1):
        return True
    return False

def is_triangle_word(word):
    num = 0
    for l in word:
        num += ord(l) - 64
    return is_triangle_num(num)


with open('words.txt', 'r') as f:
    words = [ x.strip('"') for x in f.read().split(',')]


s = 0
for w in words:
    s += is_triangle_word(w)

print(s)
