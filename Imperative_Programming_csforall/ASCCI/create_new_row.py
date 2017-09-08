def ascci3(n):
   i=0
   for k in range(n):
      print "%"*n
      i+=1


#output:

>>> ascci3(6)
%%%%%%
%%%%%%
%%%%%%
%%%%%%
%%%%%%
%%%%%%
>>> 



def createdonerow(width, height):
    A=''
    row=''
    for row in range(height):
        row=''
        for col in range(width):
           row+='*'
        A+='*'   
        print row


#OUTPUT:


>>> createdonerow(10,6)
**********
**********
**********
**********
**********
**********



