def primeSieve(numberList):
    
    if numberList == []:      
        return []              
    else:
        prime = numberList[0] 
        return [prime] + primeSieve(sift(prime, numberList[1:]))

def makeEncoderDecoder():
   
    p, q = random.sample(primeSieve(range(2, 10)), 2)
    n = p*q          
    m = (p-1)*(q-1)  
    print ("Maximum number that can be encrypted is ", n-1)

    e = random.choice(primeSieve(range(2, m)))
    if m % e == 0: 
        print ("Please try again")
        return
    else:
        d = inverse(e, m)               
        encoder = lambda x: (x**e) % n  
        decoder = lambda y: (y**d) % n  
        return [encoder, decoder]
