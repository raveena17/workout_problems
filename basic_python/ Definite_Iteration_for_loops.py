def IterationForLoop():
    
    artists = []

    for i in [0, 1, 2]:   # using range[1,10] or ["i","lke","mom"] or [42,42,42]         

        next_artist = raw_input('Enter an artist that you like:')
        artists.append(next_artist)

        print ("Thank you!  We'll work on your recommendations now.")

        
        
    return artists





#output:

>>> IterationForLoop()  #call

Enter an artist that you like:"Ravivarma"
Thank you!  We'll work on your recommendations now.
Enter an artist that you like:"Newton souza"
Thank you!  We'll work on your recommendations now.
Enter an artist that you like:"Gill"
Thank you!  We'll work on your recommendations now.
['"Ravivarma"', '"Newton souza"', '"Gill"']

