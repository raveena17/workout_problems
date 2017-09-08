class Vector2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)


    

first=Vector2D(2,4)
second=Vector2D(5,6)
result=first+second
print(result.x)
print(result.y)

        

#manual:

x,y=(2,4)
other x,y=(5,6)

__add__:
    return (2
