import time
import random
import sys
sys.setrecursionlimit(10000)
def mutate(i,oldl):
    #oldl=[0,1]
    newelement=oldl=random.choice([0,1])
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
def allones(list1):
    for i in range(len(list1)):
        if list1[i]==1 or list1[i]==' ':
            print list1[i]
        else:
            print list1[i]
            return False
    return True            
