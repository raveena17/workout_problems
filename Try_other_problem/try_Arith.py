class Arithmetic():
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
            
    def __add__(self):
        print("Addition = {0}+{1}".format(self.a,self.b))
        x = self.a+self.b
        return x

    def __sub__(self):
        print("Subtraction = {0}-{1}".format(self.a,self.b))
        x = self.a-self.b
        return x


    def __mul__(self):
        print("Multiplication = {0}*{1}".format(self.a,self.b))
        x = self.a*self.b
        return x


    def __div__(self):
        print("Divition = {0}/{1}".format(self.a,self.b))
        x = self.a/self.b
        return x


def main():
        """Arithmetic operation"""
        m= Arithmetic(5,7)
        print("(0) Continue!")
        print("(1) __add__")
        print("(2) __sub__")
        print("(3) __mul__")
        print("(4) __div__")
        print("(5) Break!  (quit)")
        print()
    
        
        while True:
            
            
            userchoice=input("Choose an option: ")

            if userchoice == 5:
                break

            elif userchoice == 0:
                continue

            elif userchoice == 1:
                a = m.__add__()
                print("Adding two value:",a)

            elif userchoice == 2:
                b = m.__sub__()
                print("Subtraction two value:",b)

            elif userchoice == 3:
                c = m.__mul__()
                print("Multiplication two value:",c)

            elif userchoice == 4:
                d = m.__div__()
                print("Division two value:",d)

            else:
                print(userchoice, "?")

        print()
        print("Thank you")




