def operation():
    """Arithmetic operation"""
    print("(0) Continue!")
    print("(1) Addition")
    print("(2) Subtraction")
    print("(3) Multiplication")
    print("(4) Division")
    print("(5) Break!  (quit)")
    print()



def Addition(x,y):
    return x+y

def Subtraction(x,y):
    return x-y

def Multiplication(x,y):
    return x*y

def Division(x,y):
    return x/y


def main():
    #initial x value and y valu
    x=8
    y=5

    while True:
        print ("x and y value",x,y)
        operation()
        userchoice=input("Choose an option: ")

        if userchoice == 5:
            break

        elif userchoice == 0:
            continue

        elif userchoice == 1:
            a = Addition(x,y)
            print("Adding two value:",a)

        elif userchoice == 2:
            b = Subtraction(x,y)
            print("Subtraction two value:",b)

        elif userchoice == 3:
            c = Multiplication(x,y)
            print("Multiplication two value:",c)

        elif userchoice == 4:
            d = Division(x,y)
            print("Division two value:",d)

        else:
            print(userchoice, "?")

    print()
    print("Thank you")
