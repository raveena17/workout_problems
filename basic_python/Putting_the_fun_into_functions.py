def y():
	return 1

def w(x):
	return 3*(x+1)

def t(x):
	return 3*x+1

def r(x,y):
	return (x**2 % y)+2

def f(a,b):
	if a<b:
		return (b-1)*(b-2)
	else:
		return (a+42)*(b+42)






#output:


>>> #1a What is the value of y()?
>>> y()
1

>>> #1b What is w(3)?
>>> w(3)
12

>>> #1c What is t(3)?
>>> t(3)
10

>>> #1d Explain in a few words how t(3) is different from t(3.0).
>>> t(3)
10
>>> t(3.0)
10.0

>>> #1e What is r(7,8)?
>>> r(7,8)
3

>>> #1f What is r(4,10)?
>>> r(4,10)
8

>>> #1g What is f(0,0)?
>>> f(0,0)
1764

>>> #1h What is f(t(y()),r(8,5))?
>>> f(t(y()),r(8,5))
20

