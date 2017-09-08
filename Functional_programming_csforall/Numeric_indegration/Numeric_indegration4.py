def dbl(x):
    return 2*x

def sq(x):
    return x**2

def f_of_fracs(dbl,low,high,n):
    res=[ float (low +(i*(high - low)/n)) for i in range(n) ]
    return [ dbl(x) for x in res ]

def f_of_fracs(sq,low,high,n):
    res=[ float (low +(i*(high - low)/n)) for i in range(n) ]
    return [ sq(x) for x in res ]




#OUTPUT:


>>> f_of_fracs(dbl, 10, 20, 5)
[20.0, 24.0, 28.0, 32.0, 36.0]

>>> f_of_fracs(sq, 4, 10, 6)
[16.0, 25.0, 36.0, 49.0, 64.0, 81.0]


