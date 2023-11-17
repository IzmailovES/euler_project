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
#print(list(map(lambda x: x%20, fib))[:])
#for i in range(3,100000):
#    if pi(i)[0] == 120:
#        print(i)

#print('!!!!')
#print(*map(lambda x : x%66, pi(66)[1]))
#exit()

acc = 0
while i < 10**9:
    if validate(i,fib):
        print(i)
        acc  += i
    i += 1
print(acc)
exit(0)
print(pi(70))
print(pi(140))
print(pi(280))
print(pi(308))
print()
#exit(0)
i = 3
n = 0
while n < 10**9:
    k = pi(i)
    if k == 120:
        n += 1
        print(i)
        #break
    i += 1
print(i)

