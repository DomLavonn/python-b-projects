class Game:
        

    def __init__(self):
        # creates 2d array
        self.board = [["#" for i in range(3)]  for i in range(3)] 


    def play_game(self):
        print("Welcome to tictactoe!\n\n")
        while(1):
            pick = input("Enter x or o.\n")
            board_index = ("Enter the index of arr")
            self.show_board(self.board, pick, board_index)
    
    
    def show_board(self, board, pick):
        
        for i in board:
            print(i)
                
    def tictac(self):
        
        player1 = input("Enter your pick")
        
        
        

        