def add(a,b):
    return a+b

def triple(a):
    return 3*a

def MapReduce(MapFunction,ReduceFunction,Mylist):
    newlist=map(MapFunction,Mylist)
    value=reduce(ReduceFunction,newlist)
    return value


#output:

#  MapReduce(triple,add, [9,5,4,7,6])---------93
