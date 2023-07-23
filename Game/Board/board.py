#imports:
import numpy as np
from Game.GameToken.game_token import GameToken






class Board:

    def __init__(self, rows = 6, cols = 7):
        self.rows, self.cols = rows, cols
        self.board = self.generate_board(self.rows, self.cols)



    def generate_board(self, rows, cols):
        return np.full((rows, cols), None, dtype=GameToken)




    def display_board(self):
        for row in range(self.rows):
            curr_row = ""

            for col in range(self.cols):
                token = self.board[row][col]

                if token is None:
                    curr_row += "- "
                
                elif token.color == GameToken.Color.RED:
                    curr_row += "R "

                elif token.color == GameToken.Color.YELLOW:
                    curr_row += "Y "


            print(curr_row)

        print("")

            


           
                
            






