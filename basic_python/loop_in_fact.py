#iteration loop :

def factorial(n):
    answerSoFar = 1
    for factor in range(1, n+1):
        answerSoFar = answerSoFar * factor
    return answerSoFar



#output:

>>> factorial(10)
3628800


                    (or)


                    
#Accumulating Answers:
                    
def listDoubler(aList):
	    doubledList = []
	    for elem in aList:
	        # append the value 2*elem to doubledList
	        doubledList.append(5*elem)
	    return doubledList


#output:
	
>>> listDoubler([20,21,22])
[100, 105, 110]
