def standardizeAll(storedPrefs):
    standardStoredPrefs = []
    for storedUser in storedPrefs:
        standardStoredUser = []
        for artist in storedUser:
            standardStoredUser.append(artist.strip().title())
        standardStoredPrefs.append(standardStoredUser)
    return standardStoredPrefs







#OUTPUT:
#  standardizeAll([[' adele', 'lAdY GAGA'], ['maROON 5']])
# [['Adele', 'Lady Gaga'], ['Maroon 5']]
#standardizeAll([['rAVEENA','mOM','dAD'], ['maROON 5']])
#[['Raveena', 'Mom', 'Dad'], ['Maroon 5']]
