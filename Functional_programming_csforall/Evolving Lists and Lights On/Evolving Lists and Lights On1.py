import time
from random import *
import sys
sys.setrecursionlimit(10000)
def mutate(i,oldl):
    newelement=oldl[i-1]
    return newelement
def evolve(oldl,curgen=0):
    print oldl,
    print"(gen:" +str(curgen)+ ")"
    time.sleep(0.25)
    if curgen==5:
        return
    else:
        newl=[mutate(i,oldl) for i in range(len(oldl))]
    return evolve(newl,curgen+1)



#OUTPUT:

>>> evolve( [1,2,3], 0 )
[1, 2, 3]  (g: 0)
[2, 3, 4]  (g: 1)
[3, 4, 5]  (g: 2)
[4, 5, 6]  (g: 3)
[5, 6, 7]  (g: 4)
[6, 7, 8]  (g: 5)
