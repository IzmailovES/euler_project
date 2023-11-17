#!/usr/bin/env python3

mod = 38
def get_f(n):
    ret = [0, 1]
    while len(ret) < n:
        ret.append(ret[-1]+ret[-2])
    return ret

def pi(mod):
    f = [0,1]
    h = 2# f[-1]%mod + f[-2]%mod
    while h !=1 :
        c = f[-1]+f[-2]
        f.append(c)
        h = f[-1]%mod + f[-2]%mod
    return len(f) -1,f 

def validate(n,fib):
    if fib[120]%n == 0 and fib[119]%n == 1 and fib[118]%n == n-1:
        for i in range(2,len(fib)-2):
            if fib[i]%n == 0 and fib[i+1]%n == 1:
                return False
            
        #d = list(map(lambda x: x%n, fib))
        #print(d)
        return True 
    return False
fib = get_f(121)
i = 3

acc = 0
while i < 10**9:
    if validate(i,fib):
        print(i)
        acc  += i
    i += 1
print(acc)
exit(0)

