def scrabbleScore(a):
    itr = 'abcdefghijklmnopqrstuvwxyz'
    itr1 = ('a', 'e', 'i', 'l', 'n', 'o', 'r', 's', 't', 'u') 
    itr2 = ('d', 'g') 
    itr3 = ('b','c', 'm', 'p') 
    itr4 = ('f', 'h', 'v', 'w', 'y') 
    itr5 = ('k') 
    itr6 = ('j', 'x') 
    itr7 = ('q','z')
    if len(a) == 0:  
        return 0
    if a[0] not in itr:
        return 0
    if a[0] in itr1:
       return 1 + scrableScore(a[1:])
    if a[0] in itr2:
        return 2 + scrableScore(a[1:])
    if a[0] in itr3:
        return 3 + scrableScore(a[1:]) 
    if a[0] in itr4:
        return 4 + scrableScore(a[1:]) 
    if a[0] in itr5:
        return 5 + scrableScore(a[1:]) 
    if a[0] in itr6:
        return 8 + scrableScore(a[1:]) 
    if a[0] in itr7:
        return 10 + scrableScore(a[1:])
    


#output
>>>scrabbleScore('quetzal')
25
>>> scrabbleScore('jonquil')
23
>>> scrabbleScore('syzygy')
25
>>> scrabbleScore('abcdefghijklmnopqrstuvwxyz')
87
>>> scrabbleScore('?!@#$%^&*()')
0
>>> scrabbleScore('')
0

