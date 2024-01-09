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


def delete_nofollowers(dn):
    deleted = 0
    for f in range(3,9):
        for num1 in dn[f][:]:
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

good_seqs = list()
def get_circle_inner(all_numbers, known_numbers, current_number, used_figures):
    if len(used_figures) == 6:
        good_seqs.append(known_numbers)
        return known_numbers
    aviaible_numbers = list(filter(lambda x: (x[1] not in used_figures) and (filter_start(current_number[0], x[0]) ), all_numbers))
    if not aviaible_numbers:
        return None
    ret = []
    for an in aviaible_numbers:
        ret.append(get_circle_inner(all_numbers, known_numbers + [an], an, used_figures + [an[1]]))
    return ret

def get_circle(numbers):
    nums8 = list(filter(lambda x: x[1] == 8, numbers))
    for num in nums8:
        ret = [num]
        ret =  get_circle_inner(all_numbers= numbers , known_numbers = ret,current_number = num , used_figures = [8])
    return ret


## generate
dict_numbers = dict()
for i,f in enumerate(formuls, start = 3):
    dict_numbers[i] = get_4digits(f)
    dict_numbers[i] = list(filter(lambda x: (x//10)%10, dict_numbers[i]))
while delete_nofollowers(dict_numbers):
    pass
#for i in dict_numbers:
#    print(i, dict_numbers[i], len(dict_numbers[i]))
numbers = []
for f in dict_numbers:
    for i in dict_numbers[f]:
        numbers.append((i,f))

#print(numbers, len(numbers))
get_circle(numbers)
good_seq = (list(filter(lambda x: filter_start(x[-1][0], x[0][0]), good_seqs)))[0]
print(sum(x[0] for x in good_seq))
