def dot(a, b):
  if len(a) != len(b):
    return float(0)
  elif a == ' ' and b == ' ':
    return float(0)
  else:
    ab = [a[i]*b[i] for i in range(len(a))]
    c = sum(ab)
    return float (c)



#output:

>>> dot([5, 3], [6, 4])
42.0
>>> dot([1, 2, 3, 4], [10, 100, 1000, 10000])
43210.0
>>> dot([5, 3], [6])
0.0
>>> dot([], [6])
0.0
>>> dot([], [])
0.0

