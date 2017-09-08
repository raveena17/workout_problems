def scrabbleScore(a):
    itr = 'abcdefghijklmnopqrstuvwxyz'
    itr1 = ('aeilnorstu') 
    itr2 = ('dg') 
    itr3 = ('bcmp') 
    itr4 = ('fhvwy') 
    itr5 = ('k') 
    itr6 = ('jx') 
    itr7 = ('qz') 
    if a in itr1:
       return 1 
    if a in itr2:
        return 2 
    if a in itr3:
        return 3  
    if a in itr4:
        return 4  
    if a in itr5:
        return 5  
    if a in itr6:
        return 8  
    if a in itr7:
        return 10  


#output:

>>> scrabbleScore('bcmp')
3
