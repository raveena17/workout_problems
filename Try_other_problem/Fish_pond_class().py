import random

class Fish:
    def __init__(self, fish_name, fish_size):
        self.fish_name = fish_name
        self.fish_size = fish_size


Pike = Fish('Pike', 5)
Sushi = Fish('Sushi', 2)
Bubbles = Fish('Bubbles', 4)
Casper = Fish('Casper', 6)
Shadow = Fish('Shadow',8 )
Comet = Fish('Comet', 3)
Charlie = Fish('Charlie', 7)
Goldie = Fish('Goldie',1 )
Nemo = Fish('Nemo',2 )
Pumpkin = Fish('Pumpkin', 5)


class Pond:

    list=[]
    def __add__(self,fish):
        self.list.append(fish)
        #return list

    def catch(self):
        fish = random.choice(self.list)
        self.list.remove(fish)
        return fish
        
    def  display(self):
        print len(self.list)
        for Fish in range(len(self.list)):
            fish = self.list[Fish]
            print fish.fish_name, fish.fish_size

              
pond = Pond()
pond.__add__(Pike)
pond.__add__(Sushi)
pond.__add__(Bubbles)
pond.__add__(Casper)
pond.__add__(Shadow)
pond.__add__(Comet)
pond.__add__(Charlie)
pond.__add__(Goldie)
pond.__add__(Nemo)
pond.__add__(Pumpkin)

nile = Pond()
nile.__add__(Sushi)
nile.display()

