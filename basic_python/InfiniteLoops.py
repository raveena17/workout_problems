def InfiniteLoops():
    prefs=[]

    numCorrect = 0

    while True:    
        newPref = raw_input("Please enter an artist or band that you like, \
                 or just press enter to see recommendations: ")
        if newPref:
            prefs.append(newPref)
        else:
            break

        print('Thanks for your input!')
        numCorrect += 1
        print numCorrect

    return prefs




#output:


>>> InfiniteLoops()

Please enter an artist or band that you like,                  or just press enter to see recommendations: "ravivarman"
Thanks for your input!
1
Please enter an artist or band that you like,                  or just press enter to see recommendations: "gaya"
Thanks for your input!
2
Please enter an artist or band that you like,                  or just press enter to see recommendations: "raveena"
Thanks for your input!
3
Please enter an artist or band that you like,                  or just press enter to see recommendations: "yazhu"
Thanks for your input!
4
Please enter an artist or band that you like,                  or just press enter to see recommendations: 
['"ravivarman"', '"gaya"', '"raveena"', '"yazhu"']
