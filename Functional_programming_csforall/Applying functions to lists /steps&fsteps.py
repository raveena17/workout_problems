def steps(low, high, N):
    return [(low )+ ((high - low)/float (N))*x for x in range(N)]


def dbl(x):
    return 2**x

def fsteps(db1, low, high, N):
     z = ((low )+ ((high - low)/float (N))*x for x in range(N))
     return [dbl(x) for x in z]



 #output:
>>> steps(0,10,4)
[0.0, 2.5, 5.0, 7.5]

>>> steps(41,43,8)
[41.0, 41.25, 41.5, 41.75, 42.0, 42.25, 42.5, 42.75]

>>> steps(41,43,10)
[41.0, 41.2, 41.4, 41.6, 41.8, 42.0, 42.2, 42.4, 42.6, 42.8]

>>> fsteps(dbl,0,1,4)
[1.0, 1.189207115002721, 1.4142135623730951, 1.681792830507429]

>>> import math
>>> fsteps(math.sin,0,math.pi,6)
[1.0, 1.4375366874249254, 2.0665117276926273, 2.9706864235520194, 4.270470720691168, 6.138958333567515]

>>> fsteps(math.exp,0,3,3)
[1.0, 2.0, 4.0]

    
