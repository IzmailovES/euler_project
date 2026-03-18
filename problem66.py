#!/usr/bin/env python3

import sympy
import math

def get_d(x):
    factors = [x for x,y in sympy.factorint(x**2 - 1).items() if y%2]
    ret = 1
    for x in factors:
        ret *= x
    return ret

def get_x(d):
    print(d)
    px = d
    dx = 2
    not_found = True
    while not_found:
        x1 = px - 1
        x2 = px + 1
        for x in (dx,):
            xp2d = (x**2 - 1) // d
            if xp2d % 4 in (2,3):
                continue
            if math.isqrt(xp2d)**2 == xp2d:
                return x
        px += d
        dx += 1
        
def get_x2(d):
    x = math.isqrt(d)
    while True:
        if ((x%d) ** 2) % d == 1:
            y = (x ** 2 - 1) // d
            if (y % 4) < 2:
                if math.isqrt(y) ** 2 == y:
                    return x,y
        x += 1

def get_sq(n):
    ret = [math.isqrt(n)]
    real_sq = math.sqrt(n)
    drob = (1, ret[0])
    while ret[-1] != 2 * ret[0]:
        den = (n - drob[1]**2)//drob[0]
        ret.append(int((real_sq + drob[1])//den))
        drob = (den , (ret[-1]*den - drob[1]))
    return ret

def get_drob_num(drob, n):
	if n == 0:
		return drob[n]
	else:
		n = (n-1) % (len(drob) - 1) + 1
		return drob[n]


def get_pqs(n):
	drob = get_sq(n)
	p = [drob[0], drob[0]*drob[1] + 1]
	q = [ 1, drob[1]]
	k = 2
	i = 0
	while True:
		ak = get_drob_num(drob, k)
		p.append(ak*p[-1] + p[-2])
		q.append(ak*q[-1] + q[-2])
		k += 1
		yield p[i], q[i]
		i += 1

def get_x3(d):
	for p,q in get_pqs(d):
		if (p**2 - d * q ** 2) == 1:
			return p,q


get_x = get_x3

mx = 0
for d in 2,3,5,6,7:
    print(get_x(d), d)

print()

for d in range(1000 + 1):
    if math.isqrt(d)**2 != d:
        x,y = get_x(d)
        if x > mx:
            print(x, d, y)
            mx = x
print(mx)
exit()


m = (1,1)
ds = set()
for i in range(1,10000000):
    d = get_d(i)
    if d <= 1000:
        if d not in ds:
            print(d, len(ds), i)
            ds.add(d)
            
