def remove_all(x,s):
    while s!=[]:
        if x == s[0]:
            a = [s[1]] + remove_all(x,s[2:])
            return a
        else:
            s1 = [s[0]] + remove_all(x, s[1:])
            return s1
    if s==[]:
        return s


#output:

>>> remove_all(3,[4,3,5,6,3,2,1])
[4, 5, 6, 2, 1]
>>> remove_all(42, [ 55, 77, 42, 11, 42, 88 ])
[55, 77, 11, 88]
>>> remove_all(42, [ 55, [77, 42], [11, 42], 88 ])
[55, [77, 42], [11, 42], 88]
>>> remove_all([77, 42], [ 55, [77, 42], [11, 42], 88 ])
[55, [11, 42], 88]



