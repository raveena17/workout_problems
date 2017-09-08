def standardizeAll(storedPrefs):
    standardStoredPrefs = []
    for storedUser in storedPrefs:
        standardStoredUser = []
        for artist in storedUser:
            standardStoredUser.append(artist.strip().title())
        standardStoredPrefs.append(standardStoredUser)
    return standardStoredPrefs







#OUTPUT:


standardizeAll([['rAVEENA','mOM','dAD'], ['mOON']])
[['Raveena', 'Mom', 'Dad'], ['Moon']]


# But using 1 list
standardizeAll(["RAVeena","PriYA"])
[['R', 'A', 'V', 'E', 'E', 'N', 'A'], ['P', 'R', 'I', 'Y', 'A']]
