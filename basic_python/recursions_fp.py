def distance(s1, s2):
    '''Return the distance between two strings,
       each of which is of length four.'''
    editDist = 0
    if s1[0] != s2[0]:
        editDist = editDist + 1
    if s1[1] != s2[1]:
        editDist = editDist + 1
    if s1[2] != s2[2]:
        editDist = editDist + 1
    if s1[3] == s2[3]:
        editDist = editDist + 1
    return editDist




#distance("raveena","ravi")------------->0
#distance("muki","ravi")--------->4
