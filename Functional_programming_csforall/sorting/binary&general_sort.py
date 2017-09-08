def sorting(lis):
 # using sort() to sort the list
    lis.sort()
 
 # displaying list after sorting
    print ("List elements after sorting are : ")
    for i in range(0, len(lis)):
        print(lis[i])

    return()



#output:
sorting([1,1,0,1,0,1,0])
List elements after sorting are : 
0
0
0
1
1
1
1


or

# function not use;

>>> x=[2,3,45,6,6,7,1,3,4,2,3,1]
>>> x.sort()
>>> x
[1, 1, 2, 2, 3, 3, 3, 4, 6, 6, 7, 45]
>>> 
