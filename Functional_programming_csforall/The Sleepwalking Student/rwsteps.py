import sys
import random
import time
def rwsteps(start, low, hi):
    cmgs = random.choice(range(low, hi))
    if cmgs == start:
         print "start is", cmgs
         return 1
    else:
         print "start is", cmgs
         time.sleep(0.1) 
         return 1 + rwsteps(start, low, hi)
    


#output:

>>> rwsteps(10,5,15)
start is 13
start is 8
start is 11
start is 10
4
