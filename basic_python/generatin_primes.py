def division(n,low,high):
    if low>high:
        return False
    elif n % low==0:
        return True
    else:
        return division(n,low+1,high)




# division(3,4,7)----False
# division(3,3,9)----True
