def guess( hidden ):
    """ a #-guessing example
        to highlight using the
        random library
    """

    comp_guess = choice(range(100)) # 0 to 99, incl.

    if comp_guess == hidden:
        print("I got it! It was", comp_guess)
        print("Total guesses:")
        return 1

    else:
        print("Aargh. I guessed", comp_guess)
        time.sleep(0.1)
        return 1 + guess( hidden )
