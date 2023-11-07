#!/usr/bin/env python3
from math import ceil
coins = [1,2,5,10,20,50,100,200]
summ = 200


def ways(ncoin, summ):
    global coins
    print(ncoin, summ, end = ' -> ')
    if summ == 0:
        print('sum 0')
        return 1
    while coins[ncoin] > summ:
        ncoin -= 1
    print(ncoin)
    if ncoin == 0:
        print('coin 0')
        return 1
    ret = ways(ncoin-1, summ)
    while True:
        summ -= coins[ncoin]
        if summ >= 0:
            ret += ways(ncoin-1, summ)
        #if summ == 0:
        #    ret += 1
        else:
            break
    print('return', ret)
    return ret

print(ways(len(coins) -1,200))
        

