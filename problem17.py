#!/usr/bin/env python3

# digits
f = {1:'one',
     2:'two',
     3:'three',
     4:'four',
     5:'five',
     6:'six',
     7:'seven',
     8:'eight',
     9:'nine',
     10:'ten',
     11:'eleven',
     12:'twelve',
     13:'thirteen',
     14:'fourteen',
     15:'fifteen',
     16:'sixteen',
     17:'seventeen',
     18:'eighteen',
     19:'nineteen',
     20:'twenty',
     30:'thirty',
     40:'forty',
     50:'fifty',
     60:'sixty',
     70:'seventy',
     80:'eighty',
     90:'ninety',
     0:''
     }

def letterize(num):
     ret = []
     n = num//100
     if n:
          ret.append(f'{f[n]}hundred')
     n = num%100
     if n and (n in f):
          ret.append(f[n])
     elif n%100:
          a,b = n//10, n%10
          ret.append(f'{f[a*10]}{f[b]}')
     ret = 'and'.join(ret)
     return ret

acc = 0
for i in range(1,1000):
     acc += len(letterize(i))
acc += len('onethousand')
print(acc)