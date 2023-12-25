#!/usr/bin/env python3

import random

def get_py():
    return random.randint(1,4)
def get_cu():
    return random.randint(1,6)
def game():
    return sum((get_py() for _ in range(9))) > sum((get_cu() for _ in range(6)))

def get_all_variants(dice_dim, dice_number):
    return dice_dim**dice_number

def dice_6_variatnts():
    ret = dict()
    n = 6 + 1
    for a in range(1,n):
        for b in range(1,n):
            for c in range(1,n):
                for d in range(1,n):
                    for e in range(1,n):
                        for f in range(1,n):
                            num = a+b+c+d+e+f
                            ret[num] = ret.get(num,0) + 1
    return ret
def dice_4_variatnts():
    ret = dict()
    n = 4 + 1
    for a in range(1,n):
        for b in range(1,n):
            for c in range(1,n):
                for d in range(1,n):
                    for e in range(1,n):
                        for f in range(1,n):
                            for g in range(1,n):
                                for h in range(1,n):
                                    for i in range(1,n):
                                        num = a+b+c+d+e+f+g+h+i
                                        ret[num] = ret.get(num,0) + 1
    return ret

d6 = dice_6_variatnts()
d4 = dice_4_variatnts()
d6vars = get_all_variants(6,6)
d4vars = get_all_variants(4,9)
d6c = {x:(d6[x]/d6vars) for x in d6}
d4c = {x:(d4[x]/d4vars) for x in d4}

def chances_to_win():
    ret = {x:0 for x  in d4}
    for z in d4:
        for x,y in { i:d6[i] for i in d6 if i < z}.items():
            ret[z] = ret.get(z,0) + y
    return ret
csw = chances_to_win()
cswc = {x:(csw[x]/d6vars) for x in csw}
ret = 0
for x,y in d4c.items():
    ret += y*cswc[x]

print(ret)


exit()

peter_wins = 0
colin_wins = 0
total_games = 0
while True:
    for _ in range(100000):
        peter_wins += game()
        total_games += 1
    print(peter_wins/total_games)


