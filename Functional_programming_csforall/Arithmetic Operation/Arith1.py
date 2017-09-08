def erdos(n):
    if n%2 ==0:
        a = (n/2)
        return a
    else:
        a = (3*n + 1)
        return a



#output:

>>> erdos(84)
42
>>> erdos(1413)
4240
>>> erdos(1)
4
>>>
