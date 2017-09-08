def demo(x):
    r = f(x+6) + x
    return r

def f(x):
    r = g(x-1)
    x = 1
    return r + x

def g(x):
    r = x + 10
    return r


#output:
#demo(2)-----------20

#demo(13)-----------42


Manual:
    
def demo(13):
   r=f(13+6)+13
   r=f(19)+13
   r=f(32)
   
def f(32):
   r=g(32-1)
   r=31
   x=1
   r+x=31+1=32

def g(32):
   r=32+10
   r=42
#demo(13)-----------42
    
