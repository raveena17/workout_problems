import random
def rwpos(a, b):
    
    compgs =  random.choice(range(a-b, a+b))
    if compgs == a:
        print("start is", compgs)
        return 1
    else:
        print("start is", compgs)
        return 1 + rwpos(a, b)





#output:
    
>>> rwpos(40, 4)
('start is', 39)
('start is', 43)
('start is', 42)
('start is', 38)
('start is', 39)
('start is', 40)
6
