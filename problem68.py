#!/usr/bin/env python3

magics = []
totals = []
                                                                                                                                                             
for a1 in range(1,11):
    for a2 in range(1,10):
        if a2 in (a1,):
            continue
        for a3 in range(1,10):
            if a3 in (a1, a2):
                continue
            total = a1 + a2 + a3
            for a4 in range(1,11):
                if a4 in (a1, a2, a3):
                    continue
                for a5 in range(1,10):
                    if a5 in (a1, a2, a3, a4):
                        continue
                    if a4 + a3 + a5 != total:
                        continue
                    for a6 in range(1,11):
                        if a6 in (a1, a2, a3, a4, a5):
                            continue
                        for a7 in range(1,10):
                            if a7 in (a1, a2, a3, a4, a5, a6):
                                continue
                            if a6 + a5 + a7 != total:
                                continue
                            for a8 in range(1,11):
                                if a8 in (a1, a2, a3, a4, a5, a6, a7):
                                    continue
                                for a9 in range(1,10):
                                    if a9 in (a1, a2, a3, a4, a5, a6, a7, a8):
                                        continue
                                    if a8 + a7 + a9 != total:
                                        continue
                                    for a10 in range(1,11):
                                        if a10 in (a1, a2, a3, a4, a5, a6, a7, a8, a9):
                                            continue
                                        if a10 + a9 + a2 != total:
                                            continue
                                        tup = (a1,a2,a3,a4,a3,a5,a6,a5,a7,a8,a7,a9,a10,a9,a2)
                                        tup_str = ''.join(map(str, tup))
                                        flag = True
                                        for s in magics:
                                            if tup_str in s + s:
                                                flag = False
                                        if flag:
                                            magics.append(tup_str)
                                            totals.append(total)


print(*magics, sep = "\n")
    
