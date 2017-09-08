import tkMessageBox
tkMessageBox.showinfo(title="RPS Game", message="Hi you are join this game!")


import random   

def level1():
    user = input("Choose your weapon: ")
    comp = random.choice( ['rock','paper','scissors'] )
    print()

    if user == 'rock':
        print('Ha! I really chose paper -- I AM WIN!')
    else:
        print ('YOU ARE OUT')
        
        print("Better luck next time...")
        
def level2():
    
    user = input("Choose your weapon: ")
    comp = random.choice( ['rock','paper','scissors'] )
    print()
    
    if user == 'paper':
        print('Ha! I really chose scissors -- I WIN!')
    else:
        print ('YOU ARE OUT')

        print("Better luck next time...")
        
def level3():
    
    user = input("Choose your weapon: ")
    comp = random.choice( ['rock','paper','scissors'] )
    print()
    
    if use=='scissors':
        print('Ha! I really chose rock -- I WIN!')
    else:
        print ('YOU ARE OUT')

        print("Better luck next time...")



