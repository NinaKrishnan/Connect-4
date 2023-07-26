#imports:
import numpy as np
from Game.GameToken.game_token import GameToken
from Game.color import Color






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
                token: GameToken = self.board[row][col]

                if token is None:
                    curr_row += "-"
                else:
                    curr_row += token.color.value


            print(curr_row)

        print("")


    def is_valid_column(self, col: int) -> bool:
        return 1 <= col <= 7 and self.board[0][col-1] is None
            


           
                
            






