def divisors (n, low, high):
    '''Returns True if n has a divisor in the range from low to high.
    Otherwise returns False.'''
    if low > high:
        return False
    elif n % low == 0: # Is n divisible by low?
        return True
    else:
        return divisors (n , low + 1, high)
    

def listPrimes (n, limit):
    '''Returns a list of prime numbers between n and limit.'''
    if n == limit:
        return []
    elif isPrime (n):
        return [n] + listPrimes (n+1, limit)
    else:
        return listPrimes (n+1, limit)

    
def isPrime (n):
    '''For any n greater than or equal to 2,
    Returns True if n is prime. False if not.'''
    if divisors (n, 2, n-1):
        return False
    else :
        return True
