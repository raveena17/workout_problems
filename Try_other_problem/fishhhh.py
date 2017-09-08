class 
    fisher_list=[]
    def add_fish(self, fish):
          self.fisher_list.append(fish)
          return self.fisher_list

    def display_gotfish(self):   
         for Fish in range(len(self.fisher_list)):
              fish = self.fisher_list[Fish]
              print fish.fish_name, fish.fish_size
    
    def go_fishing(self, pond_name, size):
       #size = input('enter the size of fish: ')
        catch_fish  = self.pond_name.catch()
        if catch_fish.fish_size >= self.size:
             self.add_fish(catch_fish)
             self.display_gotfish()
             #return catch_fish
        else:
             pond_name.add_fish(catch_fish)           


    def go(self, pond_name, size):
         self.pond_name = pond_name
         self.size = size
         for fishing in range(3):
              self.go_fishing(pond_name, size)
