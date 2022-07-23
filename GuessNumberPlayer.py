import random
import math

def getGuesses(max_guesses, curr_guess, name, range):
    
    while(curr_guess <= max_guesses):
        print(f"Please enter your guess between {range[0]} and {range[1]}")
        
        answer = random.randrange(range[0], range[1])
        
        try:
            pick =  int(input("Please enter your guess!\n"))
             
            if pick < range[0] or pick > range[1]:
                print(f"Please enter a different guess between {range[0]} and {range[1]}")
            else:
                if pick > answer:
                    print(f"Guess again! Lower!\n" )
                    curr_guess+=1
                elif pick < answer:
                    print(f"Guess again! Higher!\n" )
                    curr_guess+=1
                else:
                    print(f"{name} You won!!!!!!!!! ")

        except Exception as e: 
            print("Please enter a valid guess (Int) only!\n")
            
    print("Sorry you lost! Try Again!")

max_guesses = 5
curr_guess = 0

name = input("Please enter your name?\n")

print("\nPlease enter your range of values to guess from: ex) 20 - 100 (not inclusive)\n")


start_range = int(input("Pleae enter lower range? (inclusive)\n"))
end_range = int(input("Please enter upper range? (not inclusive)\n"))

tup_range = (start_range, end_range)

getGuesses(max_guesses, curr_guess, name, tup_range)

print("\n================================")