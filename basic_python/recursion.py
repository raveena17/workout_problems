#recursion: ex:

def is_even(x):
    if x==0:
        return True
    else:
        return is_odd(x-1)


def is_odd(x):
    return not is_even(x)




#is_even(5)---------False
#is_even(4)----------True
# is_odd(6)--------False
