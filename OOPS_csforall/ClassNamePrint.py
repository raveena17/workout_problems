#class_name is print


class point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def __del__(self):
        class_name=self.__class__.__name__
        print class_name, "it's class name"


p1=point()
p2=p1
p3=p1
print id(p1),id(p2),id(p3)
del p1
del p2
del p3


#OUTPUT:

139761284658744 139761284658744 139761284658744
point is class name
