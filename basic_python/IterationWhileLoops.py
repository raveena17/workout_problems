# Iteration: while Loops:



def IterationWhileLoops():
    prefs=[]
    print ('WELCOME')
   
    newPref = raw_input("Please enter the name of an \ artist or band that you like: " )

    while newPref != '':
        prefs.append(newPref)
        newPref = raw_input("Please enter an artist or band \that you like, or just press enter to see recommendations: ")

        print('Thanks for your input!')

    return prefs



#output:

>>> IterationWhileLoops()
WELCOME
Please enter the name of an \ artist or band that you like: "Ravivarman"
Please enter an artist or band 	hat you like, or just press enter to see recommendations: 
Thanks for your input!
['"Ravivarman"']







