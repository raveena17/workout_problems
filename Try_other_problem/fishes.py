class Pond:

    fish_list = []
    def add_fish(self,fish):
        #self.fish_list = []
        self.fish_list.append(fish)
        #return self.fish_list
    
    def catch(self):
        fish = random.choice(self.fish_list)
        self.fish_list.remove(fish)
        return fish

    def  display_fish(self):
         print len(self.fish_list)
         for Fish in range(len(self.fish_list)):
              fish = self.fish_list[Fish]
              print fish.fish_name, fish.fish_size



lotus = Pond()
lotus.add_fish(Pike)
lotus.add_fish(Boss)
lotus.add_fish(SunFish)
lotus.add_fish(Star)
lotus.add_fish(GoldFish)
lotus.add_fish(Angler)
nile = Pond()
nile.add_fish(Pike)
nile.display_fish()
'''nile.add_fish(Boss)
nile.add_fish(SunFish)
nile.add_fish(Star)
nile.add_fish(GoldFish)
nile.add_fish(Angler)'''
