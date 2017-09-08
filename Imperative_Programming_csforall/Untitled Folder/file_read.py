def wc( filename ):
    """ word-counting function """
    # we use the latin1 encoding, because it much more expansive than ASCII
    f = open( filename, encoding='latin1' )
    text = f.read()
    f.close()

    LoW = text.split()    
    print("There are", len(LoW), "words.")

    return len(LoW)


