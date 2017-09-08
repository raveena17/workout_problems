import tkMessageBox
tkMessageBox.showinfo(title="RPS Game", message="Hi you are join this game!")


import random   

def rps():
    
    user = input("Choose your weapon: ")
    comp = random.choice( ['rock','paper','scissors'] )
    print()

    if user == 'rock':
        print('Ha! I really chose paper -- I AM WIN!')
        
        print("Better luck next time...")
   
    elif user == 'paper':
        print('Ha! I really chose scissors -- I WIN!')

        print("Better luck next time...")

    else:
        print('Ha! I really chose rock -- I WIN!')

        print("Better luck next time...")



