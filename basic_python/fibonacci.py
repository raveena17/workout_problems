def fibo(n):    #  Fibonacci series
     a, b = 0, 1
     while a < n:
         print a,
         a, b = b, a+b

fibo(100)
