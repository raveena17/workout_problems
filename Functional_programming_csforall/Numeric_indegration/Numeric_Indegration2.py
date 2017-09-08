2." Step 1: Calculating the x values to be evaluated"
   "Take a look at how unitfracs(N) works:"

def unitfracs( N ):
    pass


def unitfracs1(N):
     return [ float(x)/2 *2/N   for x in range(N) ]



#output:
>>> unitfracs(2)

>>> unitfracs1(2)
[0.0, 0.5]

>>> unitfracs1(4)
[0.0, 0.25, 0.5, 0.75]

>>> unitfracs1(3)
[0.0, 0.3333333333333333, 0.6666666666666666]

>>> unitfracs1(10)
[0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]




