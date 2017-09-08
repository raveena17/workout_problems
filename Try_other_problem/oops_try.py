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
