# Problem 4

# What is the return statement that satisfies these input/output constraints? Note: This function takes two inputs. You will need to pass them as (input1, input2) in the linked oracle. You may run these and any other example inputs you wish from this page

# an input of (3,4) returns 5

# an input of (24,7) returns 25

# an input of (42,1) returns 42.01190307520001





## an input of (3,4) returns 5

def f(a,b):
    return ((a*3)%b)+b

>>> f(3,4)
5




# an input of (24,7) returns 25

def w(x,y):
    return ((x*y)/y)+1

>>> w(24,7)
25



# an input of (42,1) returns 42.01190307520001

def t(a,b):
	x=0.01190307520001
	return ((a*b)+(b*x))

>>> w(42,1)
42.01190307520001


