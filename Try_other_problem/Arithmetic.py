def add_five(x,y):
    return x+y

def sub_five(x,y):
    return x-y

def mul_five(x,y):
    return x*y

def div_five(x,y):
    return x/y


def main():
    print("(0) Continue!")
    print("(1) Addition")
    print("(2) Subtraction")
    print("(3) Multiplication")
    print("(4) Division")
    print("(5) Break!  (quit)")
    print()
    userchoice=input("Choose an option: ")
    #initial x value and y valu
    x=8
    y=5

    while switch(userchoice):
        
        if  case(1):
            print add_five(x,y)
            break
        if case(2):
            add_five(x,y)
            break
        
    
    

        

       

    print()
    print("Thank you")
