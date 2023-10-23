#!/usr/bin/env python3

def get_pass():
    a = ord('a')
    z = ord('z')
    for i in range(a,z+1):
        for j in range(a,z+1):
            for k in range(a,z+1):
                yield (i,j,k)
    return

def decrypt(key,message):
    ret = ''
    for i,k in enumerate(message):
        ret += chr(k^key[i%3])
    return ret

with open('0059.txt', 'r') as f:
    msg = f.read()
msg = [int(x) for x in msg.split(',')]

for k in get_pass():
    dc = decrypt(k,msg)
    if dc.find('extract') >= 0:
        print(sum((ord(x) for x in dc )))
