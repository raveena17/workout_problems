def operation():
    """Arithmetic operation"""
    print("(0) Continue!")
    print("(1)main(add_five,x,y)")
    print("(2)main(sub_five,x,y)")
    print("(3)main(mul_five,x,y)")
    print("(4)main(div_five,x,y)")
    print("(5) Break!  (quit)")
    print()


    x=10
    y=5


def add_five(x,y):
    return x+y

def sub_five(x,y):
    return x-y

def mul_five(x,y):
    return x*y

def div_five(x,y):
    return x/y

def main(func,x,y):
    return(func(x,y))

    while True:
        print ("x and y value",x,y)
        operation()
        userchoice=input("Choose an option: ")

        if userchoice == 5:
            break

        elif userchoice == 0:
            continue

        elif userchoice == 1:
            return Addition(x,y)
            print("Adding two value:")

        elif userchoice == 2:
            b = Subtraction(x,y)
            print("Subtraction two value:")

        elif userchoice == 3:
            c = Multiplication(x,y)
            print("Multiplication two value:")

        elif userchoice == 4:
            d = Division(x,y)
            print("Division two value:")

        else:
            print(userchoice, "?")

    print()
    print("Thank you")
