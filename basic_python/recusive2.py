def recursive_create(s1,s2):
    if len(s1)==0:
        return 0
    elif s1[0]!=s2[0]:
        return 1+recursive_create(s1[1:],s2[1:])
    else:
        return recursive_create(s1[1:],s2[1:])
        



# recursive_create("apple","mango")-------5
#recursive_create("ravina","vanith")-------4