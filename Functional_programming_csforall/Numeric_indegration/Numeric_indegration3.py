3."Take a look at how scaledfracs(low,hi,N) works:"


def scaledfracs(low,high,N):
    return [ float ( low + ( i * float ( high - low ) / N ) ) for i in range ( N )]




#OUTPUT:

>>> scaledfracs(10,30,5)
[10.0, 14.0, 18.0, 22.0, 26.0]

>>> scaledfracs(41,43,8)
[41.0, 41.25, 41.5, 41.75, 42.0, 42.25, 42.5, 42.75]

>>> scaledfracs(0,10,4)
[0.0, 2.5, 5.0, 7.5]




4."Write a function sqfracs(low,hi,N) that works as follows:"

def sqfracs(low,high,n):
    return[ float(low +(i*(high - low)/n))*float(low +(i*(high - low)/n)) for i in range(n) ]


#OUTPUT:

>>> sqfracs(4,10,6)
[16.0, 25.0, 36.0, 49.0, 64.0, 81.0]
>>> sqfracs(0,10,5)
[0.0, 4.0, 16.0, 36.0, 64.0]




