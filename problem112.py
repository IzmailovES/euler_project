#!/usr/bin/env python3

def is_bouncy(num):
    ret = False
    first = num%10
    others = num//10
    second = others%10
    others //=10
    while others and first == second:
        second = others % 10
        others //= 10
    is_up = first < second
    while others:
        current = others%10
        others //=10
        if current < second and is_up:
            return True
        elif current > second and not is_up:
            return True
        second = current
    return False
def dummy_bouncy(num):
    s_num = list(str(num))
    return not (s_num == sorted(s_num) or s_num == sorted(s_num, reverse = True))
#is_bouncy = dummy_bouncy

print(is_bouncy(13355667))
print(is_bouncy(76542211))
print(is_bouncy(1111111))
print(is_bouncy(76542231))
print(is_bouncy(765422111))
print(is_bouncy(76540211))

b = 0
cn = 1

while b/cn < 0.99:
    cn += 1
    b += is_bouncy(cn)
    #print(b/cn)

print(cn)

