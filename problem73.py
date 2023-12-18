#!/usr/bin/env python3

import math

class Fraction:
    def __init__(self,n,d):
        g = math.gcd(n,d)
        while g != 1:
            n//=g
            d//=g
            g = math.gcd(n,d)
        self.c = n//d
        self.n = n%d
        self.d = d
    
    def __hash__(self):
        return hash((self.c, self.n,self.d))

    def __eq__(self,other):
        return self.c == other.c and self.n == other.n and self.d == other.d

    def __lt__(self,other):
        if self.c != other.c:
            return self.c < other.c
        n1 = self.n*other.d
        n2 = other.n*self.d
        return n1 < n2
    def value(self):
        return (self.c,self.n,self.d)

    def decimal(self):
       return (self.c*self.d+self.n)/self.d

    def __str__(self):
        return str((self.c,self.n,self.d))
    def __repr__(self):
        return(self.__str__())
n = 12000
l = []
cnt = 0
for d in range(1,n+1):
    for num in range(d//3,(d>>1)+1):
        k = num/d
        if math.gcd(num,d) != 1:
            continue
        if k < 0.5 and k > (1/3):
            cnt += 1
print(cnt)
exit()

