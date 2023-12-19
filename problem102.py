#!/usr/bin/env python3

def sw_sign(a,b):
    return a*b <= 0


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return str((self.x,self.y))

class Otr:
    def __init__(self, p1,p2):
        self.p1 = p1
        self.p2 = p2
        self.a = None
        self.b = None
        if self.p1.x == self.p2.x:
            self.type = 'v'
        elif self.p1.y == self.p2.y:
            self.type = 'h'
        else:
            self.type = 'r'
            self.a = (p2.y-p1.y)/(p2.x-p1.x)
            self.b = (-1) * self.a * p1.x + p1.y

    def get_y(self,x):
        return self.a*x + self.b

    def get_x(self,y):
        return (y - self.b)/self.a

    def axes(self):
        if self.type == 'h': ## only y axe
            if sw_sign(self.p1.x, self.p1.x): ## if peresekaet
                return 1 << (self.p1.y > 0)
            else:
                return 0
        elif self.type == 'v': ## only x axe
            if sw_sign(self.p1.y, self.p1.y): ## if peresekaet
                return 1 << ((self.p1.x > 0) +2)
            else:
                return 0
        else:
            ret = 0
            if sw_sign(self.p1.x, self.p2.x): ## if peresekaet
                ret |= 1 << (self.get_y(0) > 0)
            if sw_sign(self.p1.y, self.p2.y): ## if peresekaet
                ret |= 1 << ((self.get_x(0) > 0) + 2)
        return ret

    def __repr__(self):
        return str((self.p1,self.p2,self.a,self.b))






#p0 = Point(1,1)
#p1 = Point(-1,-1)

#o0 = Otr(p0,p1)

#print(o0.get_x(2))
#print(o0.get_y(3))
#print(sw_sign(1,1))

acc = 0
with open('0102_triangles.txt', 'r') as f:
    l = f.readline()
    while l:
        numbers = [float(x) for x in l.split(',')]
        ps = []
        for i in range(0,len(numbers), 2):
            ps.append((Point(numbers[i],numbers[i+1])))
        tr = [Otr(ps[0], ps[1]), Otr(ps[0], ps[2]), Otr(ps[1], ps[2])]
        ret = 0
        for o in tr:
            ret |= o.axes()
        if ret == 0xf:
            acc += 1
        l = f.readline()
print(acc)


        
