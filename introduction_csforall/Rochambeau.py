#Simple Game in python:

import tkMessageBox
tkMessageBox.showinfo(title="RPS Game", message="Hi you are join this game, type rps()!")


import random   

def rps():
    
    user = input("Choose your weapon: ")
    comp = random.choice( ['rock','paper','scissors'] )
    print()

    print('the user (you) choose', user)
    print('the comp (I)   choose', comp)
    print()


    if user=='rock':
        if comp=='paper':
            print "COMPUTER WIN (*.*)"
        elif comp=='rock':
            print "equal value"
        else:
            print "USER WIN (*.*)"

    if user=='paper':
        if comp=='scissors':
            print "COMPUTER WIN (*.*)"
        elif comp=='paper':
            print "equal value"
        else:
            print "USER WIN (*.*)"

    if user=='scissors':
        if comp=='rock':
            print "COMPUTER WIN (*.*)"
        elif comp=='scissors':
            print "equal value"
        else:
            print "USER WIN (*.*)"
        

#output:
            >>> rps()
Choose your weapon: 'rock'
()
('the user (you) choose', 'rock')
('the comp (I)   choose', 'paper')
()
COMPUTER WIN (*.*)
>>> rps()
Choose your weapon: 'paper'
()
('the user (you) choose', 'paper')
('the comp (I)   choose', 'rock')
()
USER WIN (*.*)
>>> rps()
Choose your weapon: 'scissors'
()
('the user (you) choose', 'scissors')
('the comp (I)   choose', 'rock')
()
COMPUTER WIN (*.*)
>>> rps()
Choose your weapon: 'rock'
()
('the user (you) choose', 'rock')
('the comp (I)   choose', 'rock')
()
equal value
>>> rps()
Choose your weapon: 'paper'
()
('the user (you) choose', 'paper')
('the comp (I)   choose', 'scissors')
()
COMPUTER WIN (*.*)
>>> rps()
Choose your weapon: 'scissors'
()
('the user (you) choose', 'scissors')
('the comp (I)   choose', 'scissors')
()
equal value
