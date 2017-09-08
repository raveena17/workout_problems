def Jotto_scoring(string1, string2):
    if len(string1) == 0:
        return 0
     
    if string1[0] in string2:
        return 1 + Jotto_scoring(string1[1:], string2[0:])
    
    if string1[0] not in string2:
        return 0 + Jotto_scoring(string1[1:], string2[0:])

    


#output:
    
>>> Jotto_scoring('geese', 'elate')
3
>>> Jotto_scoring('dinner', 'syrup')
1
>>> Jotto_scoring('gattaca', 'aggtccaggcgc')
7
>>> 
