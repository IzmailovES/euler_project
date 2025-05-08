#!/usr/bin/env python3

rootval=10**17
target =9**17

ret = target

while target != rootval:
    d = rootval - target
    target += 2**(d.bit_length()-1)
    print(bin(target))
    ret += target

print(ret)

