#!/usr/bin/env python3

import os, sys

class CellException(Exception):
    pass

class Cell:
    def __init__(self, value = 0):
        self._value = value
        if value == 0:
            self._variants = [x for x in range(1,10)]
        else:
            self._variants = []
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, newvalue):
        if self._value == 0:
            self._value = newvalue
            self._variants = []
        else:
            raise CellException(f'try to change non-zero value: {self._value} to {newvalue}' )
    @property
    def variants(self):
        return tuple(self._variants)

    @variants.setter
    def variants(self, newvalue):
        self._variants = newvalue
    
    def remove_variant(self,variant):
        acc = 0
        try:
            self._variants.remove(variant)
            acc += 1
        except ValueError:
            pass
        return acc

    def remove_variants(self,vs):
        acc = 0
        for v in vs:
            acc += self.remove_variant(v)
        return acc
    
    def update(self):
        if len(self._variants) == 1:
            self.value = self._variants[0]
            return True
        return False
    
    def __repr__(self):
        return f'v:{self._value} {self._variants}'


GD = 9
class Grid:
    def __init__(self):
        self.grid = [[Cell() for _ in range(GD)] for _ in range(GD)]

    def fill(self,grid):
        for i in range(GD):
            for j in range(GD):
                self.grid[i][j] = Cell(grid[i][j])

    def check_zeros(self):
        counter = 0
        for l in self.grid:
            for c in l:
                if not c.value:
                    counter += 1
        return counter

    def print(self):
        for l in self.grid:
            for c in l:
                print(c.value, end = ' ')
            print()

    def get_col(self, ncol):
        ret = []
        for i in range(GD):
            ret.append(self.grid[i][ncol])
        return ret

    def get_row(self, nrow):
        ret = []
        for i in range(GD):
            ret.append(self.grid[nrow][i])
        return ret

    def get_square(self,sqcoord):
        n,m = sqcoord
        n *=3
        m *=3
        ret = []
        for i in range(n, n+3):
            for j in range(m,  m + 3):
                ret.append(self.grid[i][j])
        return ret

    def get_square_by_num(self, nsquare):
        return self.get_square((nsquare//3, nsquare%3))
    
    def what_square(self,n,m):
        return n//3,m//3
    
    def update_all(self):
        acc = 0
        for l in self.grid:
            for c in l:
                acc += c.update()
        return acc
    @staticmethod
    def extract_values(cells):
        return list(map(lambda x: x.value, cells))

    def check_solution(self):
        etalon = set(range(1,10))
        for func in self.get_row, self.get_col, self.get_square_by_num:
            for i in range(GD):
                pacient = set(self.extract_values(func(i)))
                if pacient != etalon:
                    return False
        return True

    def check_integrity(self):
        for func in self.get_row, self.get_col, self.get_square_by_num:
            for i in range(GD):
                vals = self.extract_values(func(i))
                cnt = dict()
                for i in range(len(vals)):
                    cnt[vals[i]] = cnt.get(vals[i], 0) + 1
                for x,y in cnt.items():
                    if x and y != 1:
                        return False
        return True



    def crop_variants(self):
        acc = 0
        for i in range(GD):
            for j in range(GD):
                to_delete = set()
                to_delete.update(self.extract_values(self.get_col(j)))
                to_delete.update(self.extract_values(self.get_row(i)))
                to_delete.update(self.extract_values(self.get_square(self.what_square(i,j))))
                for e in to_delete:
                    acc += self.grid[i][j].remove_variant(e)
        return acc

    def crop_by_equal_variants(self):
        ## for rows and cols and squares
        acc = 0
        for func in self.get_row, self.get_col, self.get_square_by_num:

            for i in range(GD):
                row = func(i)
                for icc in range(GD - 1):
                    if row[icc].value:
                        continue
                    for isc in range(icc+1, GD):
                        if row[isc].value:
                            continue
                        if row[icc]._variants == row[isc]._variants and len(row[icc]._variants) == 2:
                            to_delete = set(row[icc]._variants)
                            #print(f'will delete {to_delete}, {func}, {icc,isc}')
                            for c in [row[i] for i in range(GD) if (i != icc and i != isc)]:
                                acc += c.remove_variants(to_delete)
        return acc

    def check_unique(self):
        acc = 0
        for func in self.get_row, self.get_col, self.get_square_by_num:
            for i in range(GD):
                row = func(i)
                ddigs = {x:[] for x in range(1,10)}
                for d in range(1,10):
                    for c in row:
                        if c.value == 0:
                            if d in c.variants:
                                ddigs[d].append(c)

                #print(ddigs)
                for d,cs in ddigs.items():
                    if len(cs) == 1:
                        #print(cs[0]._variants, cs[0].value, d)
                        #self.print()
                        cs[0].variants = [d]
                        acc += 1
                        return acc
        return acc




    g = '''003020600
900305001
001806400
008102900
700000008
006708200
002609500
800203009
005010300'''
    g1 = '''020030090
000907000
900208005
004806500
607000208
003102900
800605007
000309000
030020050'''
    g2 = '''090300600
450070100
000189040
200000000
070030080
000000004
040298000
007050019
008006020'''
def main(args):
    grids = dict()
    with open('p096_sudoku.txt', 'r') as f:
        name = f.readline()
        while name:
            gr = []
            for _ in range(9):
                gr.append(f.readline().strip())
            grids[name]= gr
            name = f.readline().strip()
    #print(grids)
    solved = 0
    for name,g in grids.items():
        game = Grid()
        game.fill([[ int(x) for x in l] for l in g])
        print(name)
        #game.print()
        changes = 100
        start_zeros = game.check_zeros()
        loop = 0
        while changes:
            print(f'loop {loop}')
            loop += 1
            changes = 0
            while game.crop_variants():
                changes += game.update_all()
            while game.crop_by_equal_variants():
                changes += game.update_all()
                changes += game.crop_variants()
            while game.check_unique(): #### ne rabotaet
                changes += game.update_all()
                changes += game.crop_variants()
                #changes += game.update_all()
            #while game.crop_variants():
            #    changes += game.update_all()
        if game.check_solution():
            solved += 1
        else:
            print()
            print(name, start_zeros, game.check_zeros())
            game.print()
        try:
            assert game.check_integrity(), name
        except AssertionError:
            print('integriyt fail')
            game.print()
    print(solved)
        #print(game.check_zeros(), game.check_solution())
    exit()



if __name__ == '__main__':
    main(sys.argv)
