import random

class Computer:
    
    
    def __init__(self, name, max_guess,curr_guess, range_max, win_flag):
        self.name = name
        self.max_guess = max_guess
        self.curr_guess = curr_guess
        self.range_max = range_max
        self.win_flag = win_flag
        
    def __repr__(self):
        return " Computer stats " +  self.name + " " + str(self.max_guess) + " " + str(self.curr_guess) + " "  + str(self.range_max) 
        
class Game:
    
    def __init__(self, computer):
        self.computer = computer 
         
    def play(self):
        
        comp = self.computer
        self.computer.range_max = random.randint(0, 100)
        ANS = random.randint(0,  self.computer.range_max)

        print(f"Computer: Guess a number between 0 and {self.computer.range_max} \n")
        
        while(self.computer.curr_guess < self.computer.max_guess):
            new_num = random.randint(0,  self.computer.range_max)
            
            if new_num < ANS:
                print("Pick is TOO LOW! Pick again\n")
                new_num = random.randrange(new_num + 1,self.computer.range_max )
                self.computer.curr_guess += 1
            elif new_num > ANS:
                print("Pick is TOO HIGH! Pick again\n")
                new_num = random.randrange(1,new_num)
                self.computer.curr_guess += 1
            else:
                self.computer.win_flag = True
                break
    
        if self.computer.win_flag == True:
            print("YOU WIN COMPUTER!!!!!")
        else:
            print("YOU LOSE COMPUTER!!!!!")

def main():
    
    #Computer obj
    comp = Computer("Computer 1", 5, 0,0, False)
    
    #Game obj
    game = Game(comp)


    game.play()    
    
if __name__ == "__main__":
    main()    