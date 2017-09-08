def numMatches(listA, listB):
    count = 0
    for item in listA:
        if item in listB:
            count += 1
    return count




#output:

>>> listA=[4,7,5,6,9,2]
>>> listB=[4,5,6,2,3,8]
>>> numMatches(listA,listB)
4
