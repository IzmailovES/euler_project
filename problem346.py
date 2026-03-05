#!/usr/bin/env python3                                                                                                                                       

glim = 10**12
baselim= 10**6 
def get_repunits(base, lim):
    ret = [1]
    power = 0
    newnum = 1
    while True:
        power += 1
        newnum = ret[-1] + base**power
        if newnum > lim:
            break
        ret.append(newnum)
    return ret[1:]

sset  = {1}
ret = {1}
for i in range(2,baselim ):
    repunits = get_repunits(i, glim)
    added_reps = 0
    for rep in repunits:
        if rep in sset:
            ret.add(rep)
        else:
            sset.add(rep)
            added_reps += 1

for r in sset:
    if r > baselim:
        ret.add(r)
print(len(ret), sum(ret), len(sset))
