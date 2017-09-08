myarray = [1, 2,5,6]
def threshold(myarray, thresh):
    for i in range(len(myarray)):
        if myarray[i] > thresh:
            myarray[i] = 0
        else:
             myarray[i]
    return myarray         


# output:

>>> threshold(myarray, 5)
[1, 2, 5, 0]
>>> threshold(myarray, 4)
[1, 2, 0, 0]



l = [1,2,3,4,5]
def myremove(l, elem):
    for i in range(len(l)):
        if l[i] == elem:
          l.remove(l[i])
        else:
             l[i]
    print l


#output:

>>> myremove(l, 5)
[1, 2, 3, 4]
>>> myremove(l, 8)
[1, 2, 4]
  
