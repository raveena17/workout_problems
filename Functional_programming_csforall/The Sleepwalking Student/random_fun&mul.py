#A reminder on string multiplication

def string_mul():
    res=('start|' + '_'*10 + '|end')
    res1=('spam'*3)
    return res, res1



#write a function named rwpos (start ,nsteps):


import random
def rwpos(start, nsteps):
    
    comp =  random.choice(range(start-nsteps, start+nsteps))
    if comp == start:
        print("start is", comp)
        return 1
    else:
        print("start is", comp)
        return 1 + rwpos(start, nsteps)



#output:

>>> string_mul()
('start|__________|end', 'spamspamspam')
>>> rwpos(40,4)
('start is', 40)
1
>>> rwpos(65,8)
('start is', 57)
('start is', 68)
('start is', 60)
('start is', 66)
('start is', 66)
('start is', 65)
6
