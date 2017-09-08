class ComplexNumber:

    """Arithmetic operation"""
    print("(0) Continue!")
    print("(1) __add__")
    print("(2) __sub__")
    print("(3) __mul__")
    print("(4) __div__")
    print("(5) Break!  (quit)")
    print()

    
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


def main(self):

        while True:
            print ("self.a,self.b",self.a,self.b)
            userchoice=input("Choose an option: ")

            if userchoice == 5:
                break

            elif userchoice == 0:
                continue

            elif userchoice == 1:
                a = c1.__add__(self.a,self.b)
                print("Adding two value:",a)

            elif userchoice == 2:
                b = c1.__sub__(self.a,self.b)
                print("Subtraction two value:",b)

            elif userchoice == 3:
                c = c1.__mul__(self.a,self.b)
                print("Multiplication two value:",c)

            elif userchoice == 4:
                d = c1.__div__(self.a,self.b)
                print("Division two value:",d)

            else:
                print(userchoice, "?")

        print()
        print("Thank you")



c1 = ComplexNumber(4,5)


#OUTPUT:


