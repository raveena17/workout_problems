def div(a,b):
    try:
	return a/b
    except ZeroDivisionError:
	print "you are trying to divide the value by 0"
    except TypeError:
	print "please check the input data type"



