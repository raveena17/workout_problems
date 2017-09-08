import time         
from random import *  
import sys            
sys.setrecursionlimit(10000)
def mutate(i, oldL):
    new_ith_element = 2**oldL[i]
    return new_ith_element


def evolve(oldL, curgen = 0):
    print oldL,                 
    print "  (gen: " + str(curgen) + ")"  
    time.sleep(0.25)
    
    if curgen == 5: 
        return       
    else:
        newL = [ mutate(i, oldL) for i in range(len(oldL)) ]
        return evolve(newL, curgen + 1)



#OUTPUT:
    
>>> evolve([1,2,3])
[1, 2, 3]   (gen: 0)
[2, 4, 6]   (gen: 1)
[4, 8, 12]   (gen: 2)
[8, 16, 24]   (gen: 3)
[16, 32, 48]   (gen: 4)
[32, 64, 96]   (gen: 5)
