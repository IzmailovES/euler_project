#!/usr/bin/env python3

roman_digs = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'N':0}
arab_digs = ((1000,'M'), (900,'CM'), (500,'D'), (400,'CD'), (100,'C'), (90,'XC'), (50,'L'), (40, 'XL'), (10, 'X'), (9,'IX'), (5, 'V'), (4,'IV'), (1,'I'))
def roman_read(r_num):
    acc = 0
    r_num += 'N'
    for i in range(len(r_num)-1):
        if roman_digs[r_num[i]] < roman_digs[r_num[i+1]]:
            acc -= roman_digs[r_num[i]]
        else:
            acc += roman_digs[r_num[i]]
    return acc

def roman_write(num):
    acc = []
    for x,y in arab_digs:
        while num >= x:
            acc.append(y)
            num -= x
    return ''.join(acc)

def saved_chars(r_num):
    ri = roman_write(roman_read(r_num))
    return len(r_num) - len(ri) 

            
with open('0089_roman.txt','r') as f:
    ro = [x.strip() for x in f.readlines()]
ret = 0
for r in ro:
    ret += saved_chars(r)
print(ret)
