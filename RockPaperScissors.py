import random 


def main():
    rps = ["rock", "paper", "scissors"]
    comp_pick = rps[random.randint(0, len(rps))]
    
    user_pick = rps[int(input("Enter rock paper or scissors"))]
    
    winner(user_pick, comp_pick)

    
def winner(upick, cpick):
    if upick =='rock' and  cpick == 'scissors':
        print("rock win! Player 1")
    elif  upick == 'scissors' and cpick == 'paper':
        print("scissors win! Player 1")
    elif upick == 'paper' and cpick ==  'rock':
        print('paper win! Player 1')
    else:
        print("Player 2 Wins " + cpick)
        
if __name__ == '__main__':
    main()