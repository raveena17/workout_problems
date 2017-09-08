def multiple_condition(a,b):
    if len(a)==1:
        return len(a)+67
    elif len(b)==0:
        return len(b)+86-4
    else:
        return "plz check the input data------>%s%s" %(a,b)
        

#multiple_condition("r","muki")<-->68
#multiple_condition("","")<-->82
#multiple_condition("priya","mukilan")<-->'plz check the input data------>priyamukilan'
