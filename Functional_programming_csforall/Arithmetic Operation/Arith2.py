def erdosIter(n, i):
    for x in range(i):
        if n%2 == 0:
           n = (n/2)
           
        else:
            n = (3*n + 1)
    return n


#output:

>>> erdosIter(84,1)
42
>>> erdosIter(42,0)
42
>>> erdosIter(3,7)
1
          
   
