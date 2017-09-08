def twod(array):

      e=len(array)
      a=[]
      for row in range(e):
           a.append(sum(col[row] for col in array))
      a1=((sum(a)/float(e)))

      
      b=[]
      for col in range(e):
            b.append (sum(row[col] for row in array))
      b1=((sum(b))/float(e))
      
      
      c=0
      for row in range(len(array)):
          for col in range(len(array)):
                if row==col:
                  c=c+(array[row][col])
                  
      d=0
      for row in range(len(array)):
           for col in range((e-1),-1,-1): 
                d = d + array[row][col]
                break
      if a1==b1==c==d:
         return True
      else:
        return False



#OUTPUT:

>>> twod([[1,2,3], [4,5,6], [7,8,9]])
False

>>> twod([[7,12,1,14], [2,13,8,11], [16,3,10,5], [9,6,15,4]])
True
>>> 

    
