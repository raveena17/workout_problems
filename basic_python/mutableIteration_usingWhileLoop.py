#Mutable Data + Iteration: Sorting out Artists


def numMatches( list1, list2 ):
    '''return the number of elements that match between two sorted lists'''
    
    matches = 0
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            matches += 1
            i += 1
            j += 1
        elif len(list1[i]) <len(list2[j]):    # or elif list1[i] < list2[j]  "len is not use"
            i += 1
        else:
            j += 1

	          
	            
    return matches,i,j



#OUTPUT:

>>> list1=['a', 'l', 'i', 's', 'o', 'n']
>>> list2=['a', 'k', 'h', 'i', 'l']
>>> numMatches(list1,list2)
(2, 2, 5)

	
