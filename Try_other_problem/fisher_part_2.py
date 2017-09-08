class Fish:
    def __init__(self,fish_name, fish_size):
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
    pond_name= raw_input("Enter the pond name:")
    pond_size=raw_input("Enter the pond size:")
    fish_type=raw_input("How many types of fishes in that pond:")
    display=raw_input("display/not:")
    
    list=[]
    def __add__(self,fish):
        self.list.append(fish)
        #return list

    def catch(self):
        fish = random.choice(self.list)
        self.list.remove(fish)
        #print fish
        return fish
        
    def display(self):
        x = len(self.list)
        #print x
        for k in range(x):
            fish = self.list[k]
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
nile.display()

class Fisher:
    
    Fisher_name=raw_input("Enter the Fisher name:")
    
    def go(self):
         for fishing in range(3):
              self.go_fishing(self)
    fisher_list=[]
    #def add_fish(self, fish):
          #self.fisher_list.append(fish)
          #return self.fisher_list

    def display_gotfish(self):   
         for Fish in range(len(self.fisher_list)):
              fish = self.fisher_list[Fish]
              print fish.fish_name, fish.fish_size
    
    def go_fishing(self):
        catch_fish  = self.catch()
        if catch_fish.fish_size >=6:
             self.__add__(catch_fish)
             self.display_gotfish()
             #return catch_fish
        else:
             pond_name.add_fish(catch_fish)           


    def go(self):
         for fishing in range(3):
              self.go_fishing(self)



    
    
#mathu = Fisher()
#mathu.fishing()
#mathu.go(nile,5)
#mathu.go(nile,8)
