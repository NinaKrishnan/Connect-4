import sys
import queue
from typing import List
from Game.Board.board import Board
from Game.Players.Human_Player.human_player import Human_Player
from Game.GameToken.game_token import GameToken



class Game:

##################################################################################################

    def __init__(self):
        self.board = Board()
        self.players = {}
        self.get_player_names()

##################################################################################################        

    def get_available_color(self) -> GameToken.Color:
        GameToken.reset_colors()
        
        
##################################################################################################

    def get_player_names(self):
        '''
        Prompt user for player names before starting game.
        '''
        color1: GameToken.Color = GameToken.get_available_colors()
        color2: GameToken.Color = GameToken.get_available_colors()

        self.players[1] = Human_Player(input("Enter the name for Player 1: ") or "Player1", color1)
        self.players[2] = Human_Player(input("Enter the name for Player 2: ") or "Player2", color2)

    def token_matches(self, row: int, col: int, color: GameToken.Color) -> bool:
        if self.board.board[row][col] is None or self.board.board[row][col].color != color:
            return False
        return True

##################################################################################################

    def check_win_horizontal(self, row: int, col: int, color: GameToken.Color) -> bool:
        #params = index of token after player has made a move.
        connected = 1

        #First check to the left
        for c in range(col-1, col-4, -1):
            if c < 0 or not self.token_matches(row, c, color):
                break
            connected+=1

            if connected >= 4:
                return True

        for c in range(col+1, col+4):
            if c >= self.board.cols or not self.token_matches(row, c, color):
                break
            connected += 1

        return connected >= 4
    
##################################################################################################

    def check_win_vertical(self, row: int, col: int, color: GameToken.Color) -> bool:
        connected = 1

        #first check up
        for r in range(row-1, row-4, -1):
            if r < 0 or not self.token_matches(r, col, color):
                break
            connected += 1


            if connected >= 4:
                return True
            
        #then check down
        for r in range(row+1, row+4):
            if r > self.board.rows-1 or not self.token_matches(r, col, color):
                break
            connected += 1

        return connected >= 4

##################################################################################################

    def check_win_diagonal_right_to_left(self, row: int, col: int, color: GameToken.Color) -> bool:
        #Check top left to bottom right
        
        #Start with down+right from token
        if row+3 < self.board.rows and col+3 < self.board.cols:
            for i in range(4):
                if not self.token_matches(row+i, col+i, color):
                    break
        
                else: 
                    return True
                
        #Then check up+left from token
        if row-3 >= 0 and col-3 >= 0:
            for i in range(4):
                if not self.token_matches(row-i, col-i, color):
                    break

                else:
                    return True


        return False

##################################################################################################

    def check_all_wins(self, row: int, col: int, color: GameToken.Color) -> bool:
        return (self.check_win_horizontal(row, col, color) or self.check_win_vertical(row, col, color) or \
            self.check_win_diagonal_left_to_right(row, col, color) or \
                self.check_win_diagonal_right_to_left(row, col, color))

##################################################################################################

    def check_win_diagonal_left_to_right(self, row: int, col: int, color: GameToken.Color) -> bool:
        #Check top right to bottom left

        #first check down+let from token
        if row+3 < self.board.rows and col-3 > 0:
            for i in range(4):
                if self.board.board[row+i][col-i] != color:
                    break
                else:
                    return True
                
        #Then check up+right from token
        if row-3 > 0 and col+3 < self.board.cols:
            for i in range(4):
                if self.board.board[row-i][col+i] != color:
                    break

                else:
                    return True


        return False
    
##################################################################################################



    def play_game(self) -> Human_Player:
        player_queue = queue.Queue()
        player_queue.put(self.players.get(1))
        player_queue.put(self.players.get(2))
        

        
        while True:
            try:
                curr_player: Human_Player = player_queue.get()
                print("\n"+curr_player.name+"'s Turn!\n")
                row, col = curr_player.make_move(self.board)

                if self.check_all_wins(row, col, curr_player.color):
                    print(curr_player.name, " wins!!")
                    break

                else:
                    player_queue.put(curr_player)
            except KeyboardInterrupt:
                sys.exit(0)

        print(curr_player.name, " wins!!")
        return curr_player
            
            









                    

            
            



        







        

        



    


    




