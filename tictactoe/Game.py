class Game:
        
    def __init__(self):
        # creates 2d array
        self.board = [["#" for i in range(3)]  for i in range(3)] 
        self.win_flag = False


    def play_game(self):
        print("Welcome to tictactoe!\n\n")
        while(not self.win_flag):
            pick = input("Enter x or o.\n")
            board_index = input("Enter the index of arr ex: 00, 01, 02 etc..")
            self.show_board(self.board, pick, board_index)
            
    
    def create_board(self,pick, board_index, board):
        
        board[int(board_index[0])] [int(board_index[1])] = pick
        flag = self.check_match(board)    
        return flag  
              
              
    def show_board(self, board, pick, board_index):
        
        flag = self.create_board(pick, board_index, board)
       
        for i in board:
           print(i)
                  
        if flag:
            print("You win\n")
            self.win_flag = True 
                     
    def check_match(self, board):
            if( (board[0][0] == "x" and board[0][1] == "x" and board[0][2] == "x" )  or 
               ( board[0][0] == "o" and board[0][1] == "o" and board[0][2] == "o")  ):
                print("X wins")
                return True
            if( (board[1][0] == "x" and board[1][1] == "x" and board[1][2] == "x" )  or 
               ( board[1][0] == "o" and board[1][1] == "o" and board[1][2] == "o")  ):
                print("X wins")
                return True
            if( (board[2][0] == "x" and board[2][1] == "x" and board[2][2] == "x" )  or 
               ( board[2][0] == "o" and board[2][1] == "o" and board[2][2] == "o")  ):
                print("X wins")
                return True
            if( (board[0][0] == "x" and board[1][0] == "x" and board[2][0] == "x" )  or 
               ( board[0][0] == "o" and board[1][0] == "o" and board[2][0] == "o")  ):
                print("X wins")
                return True
            if( (board[1][0] == "x" and board[1][0] == "x" and board[1][0] == "x" )  or 
               ( board[1][0] == "o" and board[1][0] == "o" and board[1][0] == "o")  ):
                print("X wins")
                return True
            if( (board[2][0] == "x" and board[2][0] == "x" and board[2][0] == "x" )  or 
               ( board[2][0] == "o" and board[2][0] == "o" and board[2][0] == "o")  ):
                print("X wins")
                return True
                        
    def tictac(self):
        
        player1 = input("Enter your pick")
        
        
        

        