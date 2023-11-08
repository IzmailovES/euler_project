#!/usr/bin/env python3

def get_splits(s):
    if len(s) == 1:
        return [[s]]
    if len(s) == 2:
        return [[s], [s[0], s[1]]]
    ret = []
    for i in range(1,len(s)):
        ret +=  [[s[:i]] + x for x in get_splits(s[i: (len(s))])]
    return ret

def get_split_pattern(c):
    #s = ''
    #for i in range(c):
    #    s += str(1)
    #s = ''.join(['1' for _ in range(c)])
    s = '1'*c
    return list(filter( lambda x: max([len(y) for y in x] ) <= (c//2+1) ,get_splits(s)))

def is_s_num(num,num2, patterns):
    s_num = str(num2)
    for l in patterns[len(s_num)]:
        acc = 0
        p = 0
        for pt in l:
            ss = s_num[p:p+len(pt)]
            #if len(ss) > len(str(num)):
            #    break
            #if len(ss) > 1 and ss[0] == '0':
            #    break
            acc += int(ss)
            p += len(pt)
        else:
            if acc == num:
                print(num, num2, 'pattern:', l, len(l))
                return num2
    return 0


d_patterns = dict()
for i in range(1,14):
    d_patterns[i] = get_split_pattern(i)


#for d in d_patterns:
#    print()
#    print(f'{d}: {d_patterns[d]}')
#exit(0)

#print(is_s_num(99, d_patterns))

#for i in range(2,1000):
#    if is_s_num(i):
#        print(i, i**2)

n = 10**6 + 1
acc = 0
i = 2
while i < n:
    ii = i**2
    acc += is_s_num(i,ii,d_patterns)
    #if is_s_num(i,ii,d_patterns):
    #    acc += ii
    #    print(acc,i)
    i += 1


print(acc)

