# What composition of the functions w and t (above),
# along with the the literal value 0 will return the value 6?
# (No other literal values may be used.)
# Solution to this example: w(t(0)) 

def t(x):
    return 3*(x+1)

def w(x):
    return t(0)*2 or factorial(3)




>>> t(0)
3
>>> w(3)
6
>>> w(t(0))
6



# 1i What composition of the functions w and t (above),
# along with the the literal value 0 will return the value 10?

def t(x):
    return (3*(x+3))+1

>>> t(0)
10
