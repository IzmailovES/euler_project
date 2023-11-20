#!/usr/bin/env python3

import collections

class Card:
    cards = {'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8,'T':9,'J':10, 'Q':11, 'K':12, 'A':13}
    suits = ['H', 'C', 'S', 'D']

    def __init__(self,id):
        self.suit = id[-1]
        self.rank = id[:-1]
    
    def get_rank_value(self):
        return self.cards[self.rank]

    def __eq__(self,other):
        return self.rank == other.rank

    def __hash__(self):
        return self.rank.__hash__()

    def __lt__(self,other):
        return self.cards[self.rank] < other.cards[other.rank]

    def __gt__(self,other):
        return self.cards[self.rank] > other.cards[other.rank]

class Hand:
    sets = {'card':1, 'pair': 10**2, 'dpair':10**4, 'three':10**6, 'straight':10**8, 'flush':10**10, 'full_house':10**12, 'four':10**17, 'sf':10**18}

    def __init__(self, cards):
        self.in_hand = [Card(x) for x in cards.split()]
        self.in_hand.sort()#key = lambda x: x.get_rank_value())
    
    def _is_flash(self):
        f = self.in_hand[0].suit
        for i in self.in_hand:
            if i.suit != f:
                return False
        return True
    
    def _is_straight(self):
        k = self.in_hand[0].get_rank_value()
        for i in self.in_hand:
            #print(k, i.get_rank_value())
            if i.get_rank_value() != k:
                return False
            k += 1
        return True

    def score(self):
        if self._is_flash():
            if self._is_straight():
                return self.sets['sf']*self.in_hand[-1].get_rank_value()
            else:
                return self.sets['flush']*self.in_hand[-1].get_rank_value()
        else:
            if self._is_straight():
                return self.sets['straight']*self.in_hand[-1].get_rank_value()
            else:
                c = collections.Counter(self.in_hand)
                acc = []
                score = 0
                for crd,cnt in c.items():
                    if cnt == 4:
                        return self.sets['full_house']*crd.get_rank_value()
                    if cnt > 1:
                        acc.append((crd,cnt))
                if len(acc) == 2:
                    d = sum([y for x,y in acc])
                    if d == 5:
                        score += self.sets['full_house']
                    if d == 4:
                        score += self.sets['dpair']*max(acc, key = lambda x: x[0])[0].get_rank_value()
                        score += self.sets['pair']*min(acc, key = lambda x: x[0])[0].get_rank_value()
                        return score
                for crd,cnt in acc:
                    score += crd.get_rank_value() * (self.sets['pair'] if cnt == 2 else self.sets['three'])
                return score
def match(h1,h2):
    sc1 = h1.score()
    sc2 = h2.score()
    if sc1 == sc2:
        for i in range(4,-1,-1):
            if h1.in_hand[i] < h2.in_hand[i]:
                return 1
            if h1.in_hand[i] > h2.in_hand[i]:
                return 0
    if sc1 < sc2:
        return 1
    elif sc1 > sc2:
        return 0
    return None


### main ###
if __name__ ==  '__main__': 
    plays = []
    wins = {0:0, 1:0}
    with open('0054_poker.txt', 'r') as f:
        for l in f.readlines():
            s = l.split()
            plays.append([' '.join(s[:5]), ' '.join(s[5:])])
    for game in plays:
        a = Hand(game[0])
        b = Hand(game[1])
        winner = match(a,b)
        wins[winner] += 1
    print(wins)





