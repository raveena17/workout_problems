import random          # imports the library named random

def rps():
    
    user = input("Choose your weapon: ")
    comp = random.choice( ['rock','paper','scissors'] )
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



