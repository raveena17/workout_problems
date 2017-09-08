def factorial(n):
    '''Recursive function for computing the factorial of n.'''
	
    if n==1:
        return n
    else:
        fact= n*factorial(n-1)
        return fact


or


def factorial(n):
    if n == 0:
        return 1
    else:
        answer = factorial(n - 1)
        return n * answer
