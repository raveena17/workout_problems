import random

class Fish:
    def __init__(self, Fish_name, Fish_size):
        self.Fish_name = Fish_name
        self.Fish_size = Fish_size


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



class pond():

    list=[]
    def __add__(self,Fish):
        list.append(Fish)

    def catch(self):
        Fish = random.choice(list)
        list.remove(Fish)
        return Fish

    def display(self):
        x= len(list)
        print x
        for fish in range(x):
            Fish = x[Fish]
            print Fish.Fish_name, Fish.Fish_size



p1=pond()
p1.__add__("pike")
p1.__add__("Sushi")
p1.__add__("Bubbles")
p1.__add__("Casper")
p1.__add__("Shadow")
p1.__add__("Comet")
p1.__add__("Charlie")
p1.__add__("Goldie")
p1.__add__("Nemo")
p1.__add__("Pumpkin")
p2 = pond()
p2.__add__("pike")
p2.display()




class Fisher():

    Fisher_list=[]
    def __add__(self, Fish):
        self.Fisher_list.append(Fish)
        return self.Fisher_list

    def display_gotFish(self):
        y=len(self.Fisher_list)
        for fish in range(y):
            Fish = self.Fisher_list[fish]
            print Fish.Fish_name, Fish.Fish_size

    def go_Fishing(self, pond_name, size):
        catch_Fish= self.pond_name.catch()
        if catch_Fish.Fish_size >= self.size:
            self.__add__(catch_Fish)
            self.display_gotFish()

        else:
            pond_name.__add__(catch_fish)


    def go(self, pond_name, size):
        self.pond_name = pond_name
        self.size = size
        for Fishing in range(6):
            self.go_Fishing(pond_name, size)




