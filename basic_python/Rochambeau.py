import tkMessageBox
tkMessageBox.showinfo(title="RPS Game", message="Hi you are join this game, type rps()!")


import random   

def rps():
    
    user = input("Choose your weapon: ")
    comp = random.choice( ['rock','paper','scissors'] )
    print()

    print('the user (you) chose', user)
    print('the comp (I)   chose', comp)
    print()

    if user == 'rock':
        print('Ha! I really chose paper -- I WIN!')


        print("Better luck next time...")
        
    elif user == 'paper':
        
        print('Ha! I really chose scissors -- I WIN!')

        print("Better luck next time...")

    else:
        print('Ha! I really chose rock -- I WIN!')

        print("Better luck next time...")


#output:

>>> rps()
Choose your weapon: 'rock'
()
('the user (you) chose', 'rock')
('the comp (I)   chose', 'paper')
()
Ha! I really chose paper -- I WIN!
Better luck next time...
>>> ================================ RESTART ================================
>>> 
>>> rps()
Choose your weapon: 'paper'
()
('the user (you) chose', 'paper')
('the comp (I)   chose', 'scissors')
()
Ha! I really chose scissors -- I WIN!
Better luck next time...
>>> ================================ RESTART ================================
>>> 
>>> rps()
Choose your weapon: 'scissors'
()
('the user (you) chose', 'scissors')
('the comp (I)   chose', 'rock')
()
Ha! I really chose rock -- I WIN!
Better luck next time...







