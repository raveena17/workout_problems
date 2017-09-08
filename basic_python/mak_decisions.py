def matchFirst ( s1 , s2 ):
    '''Compare the first characters in s1 and s2
    and return True if they are the same.
    False if not'''

    if len(s1) == 0 or len(s2) == 0:
        return False
    else :
        return s1[0] == s2[0]









#matchFirst("ravina","ravi")
#True
#matchFirst("raveena","d")
#False
