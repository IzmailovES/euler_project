#!/usr/bin/env python3

import sympy

class Chain:
    checked = set()
    def __init__(self, initval):
        self.initval = initval
        self.success = False
        if self.initval in Chain.checked:
            self.success = False
            return
        self.chain = [self.initval]
        x = self.initval
        while True:
            x = get_sum_of_divisors(x)
            if x <= 1 or x > 1000000 or x in Chain.checked:
                Chain.checked.update(self.chain)
                return
            elif x in self.chain:
                self.success = True
                Chain.checked.update(self.chain)
                return
            else:
                self.chain.append(x)

def get_sum_of_divisors(n):
    return sum(sympy.divisors(n)[:-1])

for i in range(6,1000000):
    ch = Chain(i)
    if ch.success:
        print(ch.chain)
