def writeToFile(fileName):
    """ a function demonstrating how to create a new file and
        write to it. If the file (named fileName) already
        exists, it will be overwritten
    """
    f = file( fileName, 'w')
    print f
    print text

    f.close()

   
