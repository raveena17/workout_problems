def sq(x):
    return x**2
def sq1(x):
    return [sq(x) for x  in range(5)]

def sqmd(x):
    return x%4
def sqmd1(x):
    return [sqmd(x) for x in range(5)]

def mini(x):
    return  (x / 4.0)
def mini1(x):
    return[mini(x) for x in range(4)]


#output:

>>> sq1(5)
[0, 1, 4, 9, 16]
>>> sqmd1(5)
[0, 1, 2, 3, 0]
>>> mini1(4)
[0.0, 0.25, 0.5, 0.75]
