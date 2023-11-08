#!/usr/bin/env python3

d = {x:[set(),set()] for x in range(10)}
def analyze(tup, d):
    d[tup[0]][1].add(tup[1])
    d[tup[0]][1].add(tup[2])

    d[tup[1]][0].add(tup[0])
    d[tup[1]][1].add(tup[2])

    d[tup[2]][0].add(tup[0])
    d[tup[2]][0].add(tup[1])

nums = '''319
680
180
690
129
620
762
689
762
318
368
710
720
710
629
168
160
689
716
731
736
729
316
729
729
710
769
290
719
680
318
389
162
289
162
718
729
319
790
680
890
362
319
760
316
729
380
319
728
716'''

nums = [tuple((int(y) for y in x)) for x in nums.split('\n')]

for n in nums:
    analyze(n,d)

l = [ x for x in d if d[x][0] or d[x][1] ]
l.sort(key = lambda x: len(d[x][0]))
print(*l, sep = '')
