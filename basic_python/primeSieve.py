def primeSieve(numberList):
  
    if numberList == []:      
        return []              
    else:
        prime = numberList[0]  
        return [prime] + primeSieve(sift(prime, numberList[1:]))

 #call-------   primeSieve(range(2, 100))




    
# output:------[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
