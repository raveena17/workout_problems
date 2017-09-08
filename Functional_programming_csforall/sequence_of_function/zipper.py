def zipper(a ,b):
     c = zip(a, b)
     return c

#output:
>>> zipper([1,2], ['a','b','c'])
[(1, 'a'), (2, 'b')]
>>> zipper([], [1,2,3])
[]
>>> zipper([42]*3, [ 'tiles in scrabble', 'km in a '\
'marathon' ])
[(42, 'tiles in scrabble'), (42, 'km in a marathon')]
>>> 


