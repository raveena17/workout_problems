def recursive_sort(alist):
    def helper(sorting,already):
        list_box =[]
        
        if len(sorting)==0:
            return already
        else:
            x=min(sorting)
            sorting.remove(x)
            list_box.append(x)
            return helper(sorting,already+list_box)
        
    return helper(alist,[])




#output:

>>> recursive_sort([2,3,4,3,2,4,3,2])
[2, 2, 2, 3, 3, 3, 4, 4]

>>> recursive_sort([1,9,8,7,8,9,5,3,2,45,76,876])
[1, 2, 3, 5, 7, 8, 8, 9, 9, 45, 76, 876]
