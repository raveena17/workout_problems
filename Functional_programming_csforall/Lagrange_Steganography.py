import random

def randint():
    ans=random.randint(1,100)
    return ans


#output:

>>> randint()
77
>>> randint()
14
>>> randint()
100
>>> randint()
62



def sample():
    res=random.sample([10,20,30,40],3)
    return res

#output:

>>> sample()
[40, 30, 10]
>>> sample()
[10, 20, 40]
>>> sample()
[10, 40, 30]
>>> sample()
[40, 20, 30]

def ano_sample():
    res=random.sample(range(1,100),4)
    return res

#output:

>>> ano_sample()
[78, 82, 57, 88]
>>> ano_sample()
[26, 24, 90, 79]
>>> ano_sample()
[45, 50, 7, 92]
>>> ano_sample()
[71, 93, 38, 26]

