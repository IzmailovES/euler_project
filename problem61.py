#!/usr/bin/env python3

def formula3(n):
    return n*(n+1)//2

def formula4(n):
    return n**2

def formula5(n):
    return n*(3*n-1)//2

def formula6(n):
    return n*(2*n-1)

def formula7(n):
    return n*(5*n-3)//2

def formula8(n):
    return n*(3*n-2)

f3 = formula3
f4 = formula4
f5 = formula5
f6 = formula6
f7 = formula7
f8 = formula8
formuls = f3,f4,f5,f6,f7,f8
def is_4digit(num):
    return 999 < num < 10000

def get_first_4digit(formula):
    n = 1
    ret = formula(n)
    while not is_4digit(ret):
        n += 1
        ret = formula(n)
    return n,ret

def get_4digits(formula):
    n,num = get_first_4digit(formula)
    ret = []
    while is_4digit(num):
        ret.append(num)
        n += 1
        num = formula(n)
    return ret

def filter_start(num1, num2):
    return num1%100 == num2//100

def delete_some(dn):
    startnumbers = set()
    endnumbers = set()
    for d in dn.values():
        for n in d:
            startnumbers.add(n//100)
            endnumbers.add(n%100)
    #print(startnumbers, len(startnumbers))
    #print(endnumbers, len(endnumbers))
    to_delete = startnumbers ^ endnumbers
    #print(to_delete)

    for l in range(3,9):
        for k in dn[l][:]:
            if k//100 in to_delete or k%100 in to_delete:
                dn[l].remove(k)
              #  print(k)
    return to_delete


def delete_nofollowers(dn):
    deleted = 0
    for f in range(3,9):
        for num1 in dn[f][:]:
            #print(num1, ':')
            fails1 = 0
            fails2 = 0
            for i in (x for x in range(3,9) if x != f):
                ret = list(filter(lambda x: filter_start(num1,x), dict_numbers[i]))
                ret2 = list(filter(lambda x: filter_start(x,num1), dict_numbers[i]))
                if not ret:
                    fails1 += 1
                if not ret2:
                    fails2 += 1
            if fails1 == 5 or fails2 == 5:
                dn[f].remove(num1)
                deleted += 1
    return deleted

## generate
dict_numbers = dict()
for i,f in enumerate(formuls, start = 3):
    #print(get_first_4digit(f), end = ' ')
    dict_numbers[i] = get_4digits(f)
    dict_numbers[i] = list(filter(lambda x: (x//10)%10, dict_numbers[i]))
    #print(dict_numbers[i], len(dict_numbers[i]))
    #print()
while delete_nofollowers(dict_numbers):
    pass
for i in dict_numbers:
    print(i, dict_numbers[i], len(dict_numbers[i]))


