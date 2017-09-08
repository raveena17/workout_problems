def findBestUser(userPrefs, allUsersPrefs):
    ''' Given a list of user artist preferences and a
        list of lists represented all stored users'
        preferences, return the index of the stored
        user with the most matches to the current user. '''
    max_matches = 0
    best_index = 0
    for i in range(len(allUsersPrefs)):
        curr_matches = countMatches(userPrefs,
                                    allUsersPrefs[i])
        if curr_matches > max_matches:
            best_index = i
            max_matches = curr_matches
    return best_index


def countMatches(userPrefs,allUsersPrefs):
    ''' return the number of elements that match between
        listA and listB '''
    count = 0
    for item in userPrefs:
        if item in allUsersPrefs:
            count += 1
    return count



