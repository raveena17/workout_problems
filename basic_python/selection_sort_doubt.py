def selectionSort(listToSort):
    '''sorts listToSort iteratively and in-place'''
    for starting_index in range(len(listToSort)):
        min_elem_index = index_of_min(listToSort, starting_index)
        # now swap the elements!
        swap(listToSort[starting_index], listToSort[min_elem_index])

def swap(a, b):
    '''swaps the values of a and b'''
    temp = a
    a = b
    b = temp




0r




#doubt

def selection_sort(A):
    for i in range(0, len(A)-1):
        minIndex=i
        for j in range(i+1, len(A)):
            if A[j] < A[minIndex]:
                minIndex=j

        if minIndex != i:
            A[i],A[minIndex]=A[minIndex],A[i]
