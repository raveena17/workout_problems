def printFileToScreen( fileName ):
    """ simply prints the contents of the file to the screen
        input: fileName, a string with the file's name
    """
    f = file( fileName )      
    text = f.read()            
    f.close()                  
    
    print 'The file contains:' 
    print                      
    print text   




#output:
    
>>> printFileToScreen('cow.txt')
The file contains:

The cow is of the bovine ilk.
One end is moo, the other milk.
