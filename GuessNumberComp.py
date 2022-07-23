import random

class Computer:
    
    def __init__(self, name, max_guess,curr_guess, range_max):
        self.name = name
        self.max_guess = max_guess
        self.curr_guess = curr_guess
        self.range_max = range_max
        
    def __repr__(self):
        return " Computer stats " +  self.name + " " + str(self.max_guess) + " " + str(self.curr_guess) + " " + str(self.range_one) + " " + str(self.range_two)
        
    
class Game:
    
    def __init__(self, computer):
        self.computer = computer 
        
        
    def play(self):
        max
        
    
    
    
    
    
def main():
    
    #Computer obj
    comp = Computer("Computer 1", 5, 0,0, 0)
    
    #Game obj
    game = Game(comp)


    print(game.computer.name)
    
    
    


if __name__ == "__main__":
    main()
    
    
    


        
        