#!/usr/bin/env python3

import math
import sympy
def p(a,c):
    return 2*a+c

#def hp(a,b,c):
#    return p(a,c)/2
def is_fullsq(num):
    f = sympy.ntheory.primetest.is_square(num)
    if f:
        return int(math.sqrt(num))
    return 0
    a,b = math.modf(math.sqrt(num))
    if not a:
        return int(b)
    return 0

def check(a,c):
    p = (2*a+c)/2

i = 4
p = 0
acc = 0
maxp = 10**9
while True:
    if i*3 -1 > maxp:
        break
    q = is_fullsq(4 + 3* i**2)
    if q:
        ## try to +1
        if not (q+1)%3:
            a = (q+1)//3
            c = a + 1
            acc += 2*a+c
            print(f'a={a}, c={c}')
        elif not (q-1)%3:
            a = (q-1)//3 
            c = a - 1
            acc += 2*a +c
            print(f'a={a}, c={c}')
        print(i,q,acc)
    i += 1
print(acc)

#def sq(a,c):
#    q = (a+b+c) * (-a + b +c) * (a -b +c) * (a + b -c)
#    (2a+c)*c *c * ( 2a -c ) = (2a + a +- 1)(2a -a +-1) * c**2 = (3a +-1)(a -+ 1) *c**2
#    q = (2*a+c) * (2*a-c) = 4*a**2 - c**2
#    4*a**2 - (a-1)**2
#    4*a**2 - a**2 + 2*a -1
#    (3*a**2 + 2*a - 1)**0.5 * (a-1)
#
#
#    4*a**2 - (a+1)**2
#    (3*a**2 - 2*a - 1)**0.5 * (a+1), c = a +1
#    (3*a**2 + 2*a - 1)**0.5 * (a-1), c = a - 1
#    (3*a**2 +- 2*a -1) == fsq1
#    d = 4 + (4*3*(1+fsq)) = 4 + 12 + 12*fsq = 4(1 + 3 + 3*fsq1) = 4(4 + 3*fsq1)
#    a = (+-2 - 2 * sqrt(fsq2))/(2 *3) =  (+-sqrt(4+3*fsq1) +-1)/3 - отрицательный корень не устраивает
#   a = (sqrt(fsq2) +- 1)/3, +1 для a=c-1, -1 для a=c+1
#   4 + 3*fsq1 = fsq2
# среди пар fsq1, fsq2 нужно найти такие, что корень из fsq1 +-1 делится на 3
#   fsq1 = (fsq2-4)/3 # fsq(1)*c**2 - квадрат площади
 #   return sqrt(q) * c//4
