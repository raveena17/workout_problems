#prime_number using for loop , if statement,and using break stmnt.

for n in range(2,10):
    for x in range(2,n):
	if(n%x)==0:
	    print n,'is a not prime by',x,'*',n/x #n value are divided by x
	    break
    else:
	print n,'is a prime number'
	    
