def divisors (n, low, high):
    '''Returns True if n has a divisor in the range from low to high.
    Otherwise returns False.'''
    if low > high:
        return False
    elif n % low == 0: # Is n divisible by low?
        return True
    else:
        return divisors (n , low + 1, high)
