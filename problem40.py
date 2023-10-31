#!/usr/bin/env python3

def get_nth(n):
    ## reduce
    l = 1
    n -= 1
    while l*(9*10**(l-1)) <= n:
        n -= l*(9*10**(l-1))
        l += 1
    nn = n//l
    ni = n%l

    dig = str(10**(l-1) + nn)[ni]
    return int(dig)

def get_n_brute(n):
    s = '0'
    i = 1
    while len(s) <= n:
        s = s + str(i)
        i += 1
    #print(f'str: {s[:n]} {s[n]} {s[n+1:]}')
    return int(s[n])

#for i in range(100):
#    a = get_nth(i)
#    b = get_n_brute(i)
#    if a != b:
#        print('!!!!', i,a,b)
#exit(0)
acc = 1
for i in range(7):
    acc *= get_nth(10**i)

print(acc)
     
