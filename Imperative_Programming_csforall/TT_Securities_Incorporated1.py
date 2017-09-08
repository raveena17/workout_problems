#
# example user-interaction looping program
#  (a variant of the one done in class)
#

def menu():
    """ a function that simply prints the menu """
    print()
    print("(0) Continue!")
    print("(1) Enter a new list")
    print("(2) Predict the next element")
    print("(9) Break! (quit)")
    print()

def predict(L):
    """ predict ignores its input and returns
        what the next element should have been
    """
    return 42

def find_min(L):
    """ find min uses a loop to return the minimum of L
        input L: a nonempty list of numbers
        output:  the smallest value in L
    """
    result = L[0]
    for x in L:
        if x < result:
            result = x
    return result

def find_min_loc(L):
    """ find min loc uses a loop to return the minimum of L
             and the location (index or day) of that minimum
        input L: a nonempty list of numbers
        outputs:  the smallest value in L, its location (index)
    """
    minval = L[0]
    minloc = 0

    for i in list(range(len(L))):
        if L[i] < minval:  # a smaller one was found!
            minval = L[i]
            minloc = i

    return minval, minloc

def main():
    """ the main user-interaction loop """
    secret_value = 4.2

    L = [30,10,20]  # an initial list

    while True:     # the user-interaction loop
        print("\n\nThe list is", L)
        menu()
        uc = input( "Choose an option: " )

        # "clean and check" the user's input
        # 
        try:
            uc = int(uc)   # make into an int!
        except:
            print("I didn't understand your input! Continuing...")
            continue

        # run the appropriate menu option
        #
        if uc == 9:    # we want to quit
            break      # leaves the while loop altogether

        elif uc == 0:  # we want to continue...
            continue   # goes back to the top of the while loop

        elif uc == 1:  # we want to enter a new list
            newL = input("Enter a new list: ")    # enter _something_
            
            # "clean and check" the user's input
            #
            try: 
                newL = eval(newL)   # eval runs Python's interpreter! Note: Danger!
                if type(newL) != type([]): 
                    print("That didn't seem like a list. Not changing L.")
                else: 
                    L = newL  # here, things were OK, so let's set our list, L
            except:
                print("I didn't understand your input. Not changing L.")

        elif uc == 2:        # predict and add the next element
            n = predict(L)   # get the next element from the predict function
            print("The next element is", n)
            print("Adding it to your list...")
            L = L + [n]      # and add it to the list

        elif uc == 3:  # unannounced menu option!
            pass       # this is the "nop" (do-nothing) statement in Python

        elif uc == 4:  # unannounced menu option (slightly more interesting...)
            m = find_min(L)
            print("The minimum value in L is", m)

        elif uc == 5:  # another unannounced menu option (even more interesting...)
            minval, minloc = find_min_loc(L)
            print("The minimum value in L is", minval, "at day #", minloc)

        else:
            print(uc, " ?      That's not on the menu!")

    print()
    print("See you yesterday!")
