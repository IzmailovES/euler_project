#!/usr/bin/env python3

import math

filename="0098_words.txt"

def sort_word(w):
    return ''.join(sorted(w))

def check_sq(w1, w2, sq):
    wsq = str(sq)
    if len(w1) == len(w2) == len(wsq):
        mw = {}
        md = {}
        n = len(wsq)
        for i in range(n):
            if w1[i] not in mw:
                mw[w1[i]] = wsq[i]
            else:
                if mw[w1[i]] != wsq[i]:
                    return False
            if wsq[i] not in md:
                md[wsq[i]] = w1[i]
            else:
                if md[wsq[i]] != w1[i]:
                    return False
        new_sq = [None]*n
        for i in range(n):
            new_sq[i] = mw[w2[i]]
        new_sq = int(''.join(new_sq))
        if len(str(new_sq)) != n:
            return False
        return math.isqrt(new_sq)**2 == new_sq
    else:
        return False

with open(filename, 'r') as f:
    words = [x.strip('"') for x in f.readlines()[0].split(',') ]

words = [x for x in words if len(x) > 2]
words_by_length = dict()

for w in words:
    n = len(w)
    if n not in words_by_length:
        words_by_length[n] = set()
    words_by_length[len(w)].add(w)

words_anagrams = dict()

for ws in words_by_length:
    for w in words_by_length[ws]:
        sw = sort_word(w)
        if sw not in words_anagrams:
            words_anagrams[sw] = {w}
        else:
            words_anagrams[sw].add(w)

words_anagrams = {x:y for x,y in words_anagrams.items() if len(y) > 1}

words_anagrams_by_length = dict()

for anagram in words_anagrams:
    n = len(anagram)
    if n not in words_anagrams_by_length:
        words_anagrams_by_length[n] = []
    words_anagrams_by_length[n].append(words_anagrams[anagram])

print(list(map(len, words_anagrams)))

print(len(words), max(map(lambda x: len(x) , words)))

print(check_sq('race', 'care', 1296))
#print(words_by_length)
#print(words_anagrams)

print(words_anagrams_by_length)


for i in range(10,10**7):
    sq = i ** 2
    n = len(str(sq))
    if n in words_anagrams_by_length:
        for anagrams in words_anagrams_by_length[n]:
            a = list(anagrams)
            for i in range(len(a) - 1):
                for j in range(i+1, len(a)):
                    if check_sq(a[i], a[j], sq):
                        print(sq, a[i], a[j])
                    if check_sq(a[j], a[i], sq):
                        print(sq, a[j], a[i])
