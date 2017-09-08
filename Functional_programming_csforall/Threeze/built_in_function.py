def f(L):
    list1=map(lambda x : x/2,L)
    return list1


def fo(L):
    list2=filter(lambda X: X>42, L)
    return list2

def foo(L):
  """foo(L) takes a list L of integers as input and returns a weird list"""
  List1 = map(lambda X : X/2, L)  
  List2 = filter(lambda X: X>42, List1) 
  return List2


#output:

>>> f([5,3,89,65,34,29,7])
[2, 1, 44, 32, 17, 14, 3]

>>> fo([4,65,34,8,9,34])
[65]

>>> foo([5,3,3,5,6,29,7])
[]




def f():
    lst=[[X, Y] for X in range(0, 3) for Y in range(5, 8)]
    return lst


#output:
>>> f()
[[0, 5], [0, 6], [0, 7], [1, 5], [1, 6], [1, 7], [2, 5], [2, 6], [2, 7]]



def square():
    res=[X**2 for X in range(0, 10)]
    return res


#output:

>>> [X**2 for X in range(0, 10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
