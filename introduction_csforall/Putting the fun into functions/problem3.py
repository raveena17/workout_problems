# Problem 3

# What is the return statement that satisfies these input/output constraints? You may run these and any other example inputs you wish from this page

# an input of 3 returns 0

# an input of 42 returns 0

# an input of 37 returns 1

# an input of 128 returns 2





# an input of 3 returns 0

def f1(x):
    return x-3 or x%3

>>> f1(3)
0



# an input of 42 returns 0

def t(x):
    return x%2

>>> t(42)
0


# an input of 37 returns 1

def f2(x):
    return x%2

>>> f2(37)
1



# an input of 128 returns 2

def w(x):
    return x-(factorial(5)+factorial(3))

>>>w(128)
2

or

>>>128-(factorial(5)+factorial(3))
2
    

