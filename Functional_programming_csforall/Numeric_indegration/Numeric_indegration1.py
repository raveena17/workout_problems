from math import *



# two more functions (not in the math library above)
def dbl(x):
    return 2*x

def sq(x):
    return x**2


# 1.. examples for getting used to list comprehensions...

def lc_mult( N ):
    """ this example takes in an int N
    and returns a list of integers from 0 to N-1,
    **each multiplied by 2**"""
    return [ 2*x for x in range(N) ]


def lc_idiv( N ):
    """ this example takes in an int N
    and returns a list of integers from 0 to N-1,
    **each divided by 2**
        WARNING: this is INTEGER division...!"""
    return [ x/2 for x in range(N) ] or  return [ float(x/2) for x in range(N) ]
    #output can't change


def lc_fdiv( N ):
    """ this example takes in an int N
        and returns a list of integers
        from 0 to N-1, **each divided by 2**
        NOTE: this is floating-point division...!
    """
    return [ float(x)/2 for x in range(N) ]



# Trying out list comprehensions:


>>> dbl(4)
8
>>> sq(7)
49
>>> lc_mult(10)
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
>>> lc_mult(5)
[0, 2, 4, 6, 8]
>>> lc_idiv(10)
[0, 0, 1, 1, 2, 2, 3, 3, 4, 4]
>>> lc_fdiv(10)
[0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5]



    












































