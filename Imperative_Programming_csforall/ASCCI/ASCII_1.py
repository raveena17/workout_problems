def ASCII(n):

   for k in range(n-1):
      print((n-k) * ' ' + (2*k+1) * '&')

      
   for k in range(n-1, -1, -1):
      print((n-k) * ' ' + (2*k+1) * '&')

#output:


>>> ASCII(6)
      &
     &&&
    &&&&&
   &&&&&&&
  &&&&&&&&&
 &&&&&&&&&&&
  &&&&&&&&&
   &&&&&&&
    &&&&&
     &&&
      &
