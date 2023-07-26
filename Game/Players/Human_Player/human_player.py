from typing import List
import numpy as np
import Game.game
from Game.Board.board import Board
from Game.GameToken.game_token import GameToken



class Human_Player:
    
    def __init__(self, name: str, color: GameToken.Color):
        self.name = name
        self.color: GameToken.Color = color
        self.tokens: List[GameToken] = self.generate_token_pool()
        



    def generate_token_pool(self, n_tokens: int = 21) -> List[GameToken]:

        token_stack: List[GameToken] = []

        for i in range(n_tokens):
            token_stack.append(GameToken(self.color))

        return token_stack
    



    def make_move(self, board: Board):
        col, row = None, None
        while True:
            col: int = int(input("Enter the column you want to drop your token into: "))
            if board.is_valid_column(col):
                break
            

        for row in range(board.rows-1, -1, -1):
            if board.board[row][col-1] == None:
                board.board[row][col-1] = self.tokens.pop()
                break
            
        print("\n")
        board.display_board()
        return row, col-1

    







