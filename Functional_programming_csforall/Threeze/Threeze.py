def even(x):
    if x % 2 == 0:
        return True
    else:
        return False


#output:
    
>>> filter(even, [0, 1, 2, 3, 4, 5, 6])
[0, 2, 4, 6]



def sublist(a, b):
    d = len(a)
    print(d)
    if d < b:
        return []
    else:
        c = a[0:b-1] + a[b:d-1]
        d = a[b-1:b] + a[d-1:d+1]
        f = a[b-1:b+1]
        h = a[0:1] + a[3:4]
        return a[:b], a[b:], c, d, f, h


#output:

>>> sublist([1, 2, 3, 4], 3)
4
([1, 2, 3], [4], [1, 2], [3, 4], [3, 4], [1, 4])   




def sb(a):
    str=''
    for i in range(len(a)):
      if len(a) == 0:
        return 0
      else:
        b = a[i]
        str+=b
    print str


#output:

>>> sb(['s', 'p', 'a', 'm'])
spam

