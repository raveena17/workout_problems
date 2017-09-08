# wordcounter, wc

# to make this work, create a text file named
#
# a.txt
#
# in the same directory as this .py file!

def wc( filename ):
    """ word-counting function """
    # we use the latin1 encoding, because it much more expansive than ASCII
    f = open( filename, encoding='latin1' )
    text = f.read()
    f.close()

    LoW = text.split()    
    print("There are", len(LoW), "words.")

    return len(LoW)

# call this with    wc('a.txt')



def vc( filename ):
    """ vocabulary-counting function """
    # we use the latin1 encoding, because it much more expansive than ASCII
    f = open( filename, encoding='latin1' )
    text = f.read()
    f.close()

    LoW = text.split()    
    print("There are", len(LoW), "words.")

    d = {}
    for w in LoW:
        if w not in d:
            d[w] = 1
        else:
            d[w] += 1
            
    print("There are", len(d), "*distinct* words.\n")
    return d   # this way we can use the data in d later!

# call this with     vc('a.txt')






