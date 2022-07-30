from numbers import Number
from Game import Game


if __name__ == "__main__":
    # creates 2d array3
    number_board = [  [i for i in range( (j * 3), (j + 1)* 3) ] for j in range(3)]   
    print(number_board)
     for row in number_board:
        print('| ' + ' | '.join(row) + ' |')
 

    # game = Game()
    
    
    # game.play_game()