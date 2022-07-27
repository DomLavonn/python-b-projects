from Person import Person
import random 

class Game:
    
    words = ['domanik', 'couch', 'computer', 'pluto']
    
    def __init__(self):
        self.person = None
        self.person_string = ""
        self.win_flag = False


    def play_game(self):
        
        name = input("Enter your name?\n")
        
        self.person = Person(name, 0)
        
        # Gets random word
        player_guess_str = self.shuffle_word()
        
        
        while(self.person.count < len(player_guess_str) and len(self.person_string) != len(player_guess_str)):
            letter = input("Guess your letter? Current count {}\n".format(self.person.count))

            self.show_screen(letter, player_guess_str )
            
        if self.win_flag:
            print("You win!")
        else:
            print("Sorry you lose!")
            
    
    def show_screen(self, letter,player_guess_str):
       if letter not in player_guess_str and letter not in self.person_string:
           
           # Adding player count
           self.person.count += 1
           
           print("Please guess another letter! {} remaining".format(len(player_guess_str) -  self.person.count ))
         
       elif letter in player_guess_str and letter not in self.person_string:
           self.person_string+=letter
           if len(self.person_string) == len(player_guess_str):
               print("You win! {} break!".format(self.person.name))
               self.win_flag = True
               return 
           
           print("Correct Letter {}! {} remaining".format(letter,len(player_guess_str)))

           
        

    def check_letter(self, letter):
        pass
        
    def shuffle_word(self):
        num = random.randint(0, len(self.words))
        return self.words[num-1]
        
        