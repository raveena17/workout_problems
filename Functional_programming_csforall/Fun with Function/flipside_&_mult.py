def flipside(s):
  
  x = len(s)//2
  return s[x:] + s[:x]



#output:

>>> flipside('carpets')
'petscar'
>>> flipside('python')
'honpyt'
>>> flipside('flipside')
'sideflip'
>>> flipside('az')
'za'
>>> flipside('a')
'a'
>>> flipside('')
''


def mult(n, m):
  return n * m

#output:

>>> mult(6, 7)
42
>>> mult(6, -7)
-42
>>> mult(-6, -7)
42
>>> mult(0, 7)
0
>>> mult(0, 0)
0

